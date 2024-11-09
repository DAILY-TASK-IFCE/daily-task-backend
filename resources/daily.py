from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.daily import DailyQueryParamsSchema, DailyResponseSchema, DailyParamsSchema
from models.daily import Daily
from models.team_user import TeamUser
from datetime import datetime
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in
from utils.functions.filter_query import filter_query
from utils.functions.update_if_present import update_if_present
from utils.functions.add_nested_params import add_nested_params, add_nested_params_to_list
from utils.functions.date_filter import apply_date_filter
blp = Blueprint("Dailies", __name__, description="Operations on Dailies")

@blp.route("/daily")
class DailyList(ResourceModel): 
    @is_logged_in
    @blp.arguments(DailyQueryParamsSchema, location="query")
    @blp.response(200, DailyResponseSchema(many=True))
    def get(self, args):
        filter_by = args.get("filterBy")
        order_by = args.get("orderBy", "desc")
        team_id = args.get("team_id")
        query = filter_query(Daily, args)
        if team_id:
            query = query.join(TeamUser).filter(TeamUser.team_id == team_id, Daily.team_user_id == TeamUser.id)
        query = apply_date_filter(query, filter_by, args)
        query = query.order_by(Daily.id.asc() if order_by == "asc" else Daily.id.desc())
        dailies = query.all()
        return add_nested_params_to_list(dailies, ["items", "team_user"])
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyParamsSchema)
    @blp.response(201)
    def post(self, new_daily_data):
        new_daily_data["date"] = datetime.today()
        if Daily.query.filter_by(date=new_daily_data["date"], team_user_id=new_daily_data["team_user_id"]).first():
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
        daily_dict = add_nested_params(daily, ["items", "team_user"])
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

