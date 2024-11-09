from flask_smorest import Blueprint

from datetime import datetime, timedelta
from calendar import monthrange
from resources.resource import ResourceModel
from schemas.daily import DailyQueryParamsSchema, DailyResponseSchema, DailyParamsSchema
from models.daily import Daily
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present
from utils.functions.add_nested_params import add_nested_params, add_nested_params_to_list
blp = Blueprint("Dailies", __name__, description="Operations on Dailies")

@blp.route("/daily")
class DailyList(ResourceModel): 
    @is_logged_in
    @blp.arguments(DailyQueryParamsSchema, location="query")
    @blp.response(200, DailyResponseSchema(many=True))
    def get(self, args):
        query = filter_query(Daily, args)
        dailies = query.order_by(Daily.id.desc()).all()
        return add_nested_params_to_list(dailies, ["items", "user_team"])
    
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
        daily_dict = add_nested_params(daily, ["items", "user_team"])
        return daily_dict, 200
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, id):
        daily = Daily.query.get_or_404(id)
        update_if_present(daily, args)
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
        return add_nested_params_to_list(dailies, ["items", "user_team"])

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
        return add_nested_params_to_list(dailies, ["items", "user_team"])

