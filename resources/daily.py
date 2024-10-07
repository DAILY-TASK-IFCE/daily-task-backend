from flask_smorest import Blueprint

from datetime import datetime, timedelta
from calendar import monthrange
from resources.resource import ResourceModel
from schemas.daily import DailyQueryParamsSchema, DailyResponseSchema, DailyParamsSchema
from models.daily import Daily
from models.item import Item
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.nest_item import nest_item

blp = Blueprint("Dailies", __name__, description="Operations on Dailies")

@blp.route("/daily")
class DailyList(ResourceModel): 
    @is_logged_in
    @blp.arguments(DailyQueryParamsSchema, location="query")
    @blp.response(200, DailyResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Daily, args)
        dailys = query.order_by(Daily.id.desc()).all()
        daily_dicts = []
        for daily in dailys:
            daily_dict = daily.__dict__.copy()
            daily_dict["items"] = nest_item(daily)
            daily_dict["user_team"] = Item.query.get(daily.user_team_id)
            daily_dicts.append(daily_dict)
        return daily_dicts
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyParamsSchema)
    @blp.response(201)
    def post(self, new_daily_data):
        new_daily_data["date"] = datetime.today()
        if Daily.query.filter_by(date=new_daily_data["date"], user_team_id=new_daily_data["user_team_id"]).first():
            return {"message": "Esse usuário já fez uma daily hoje"}, 409
        
        new_daily = Daily(**new_daily_data)
        self.save_data(new_daily)
        return {"message": "Daily criada com sucesso"}, 201

@blp.route("/daily/<int:id>")
class DailyId(ResourceModel):
    @is_logged_in
    @blp.response(200, DailyResponseSchema)
    def get(self, id):
        daily = Daily.query.get_or_404(id)
        daily_dict = daily.__dict__.copy()
        daily_dict["items"] = nest_item(daily)
        daily_dict["user_team"] = Item.query.get(daily.user_team_id)
        return daily_dict, 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        daily = Daily.query.get_or_404(id)

        for key, value in args.items():
            if value is not None:
                setattr(daily, key, value)

        self.save_data(daily)
        return {"message": "Daily editada com sucesso"}, 200
    
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        daily = Daily.query.get_or_404(id)
        self.delete_data(daily)
        return {"message": "Daily deletada com sucesso"}, 200

@blp.route("/daily/week/<int:weeknum>")
class DailyWeekId(ResourceModel):
    @is_logged_in
    @blp.response(200, DailyResponseSchema(many=True))
    def get(self, weeknum):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday(), weeks=weeknum)
        end_of_week = start_of_week + timedelta(days=5)

        dailies = Daily.query.filter(Daily.date >= start_of_week, Daily.date <= end_of_week).all()
        daily_dicts = []
        for daily in dailies:
            daily_dict = daily.__dict__.copy()
            daily_dict["items"] = nest_item(daily)
            daily_dict["user_team"] = Item.query.get(daily.user_team_id)
            daily_dicts.append(daily_dict)
        
        return daily_dicts

@blp.route("/daily/month/<int:monthnum>")
class DailyMonthId(ResourceModel):
    @is_logged_in
    @blp.response(200, DailyResponseSchema(many=True))
    def get(self, monthnum):
        today = datetime.today()
        target_month = today.month - monthnum
        target_year = today.year
        if target_month <= 0:
            target_month += 12
            target_year -= 1
        num_days = monthrange(target_year, target_month)[1]
        month_days = []
        for day in range(1, num_days + 1):
            current_date = datetime(target_year, target_month, day)
            if current_date.weekday() < 5:
                month_days.append(current_date)
        dailies = Daily.query.filter(Daily.date.in_(month_days)).all()
        daily_dicts = []
        for daily in dailies:
            daily_dict = daily.__dict__.copy()
            daily_dict["items"] = nest_item(daily)
            daily_dict["user_team"] = Item.query.get(daily.user_team_id)
            daily_dicts.append(daily_dict)
        
        return daily_dicts

