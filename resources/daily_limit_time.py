from flask_smorest import Blueprint

from resources.resource import ResourceModel
from schemas.daily_limit_time import DailyLimitTimeQueryParamsSchema, DailyLimitTimeResponseSchema, DailyLimitTimeParamsSchema
from models.daily_limit_time import DailyLimitTime
from utils.decorators.handle_exceptions import handle_exceptions
from utils.decorators.is_logged_in import is_logged_in

blp = Blueprint("DailyLimitTimes", __name__, description="Operations on DailyLimitTimes")

@blp.route("/daily_limit_time")
class DailyLimitTimeList(ResourceModel): 
    
    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyLimitTimeParamsSchema)
    @blp.response(201)
    def post(self, new_daily_limit_time_data):
        if (DailyLimitTime.query.filter_by(team_id=new_daily_limit_time_data["team_id"]).first()):
            return {"message": "Já existe um Tempo Limite de Daily's nesse time, tente editar o que ja existe."}, 409
        new_daily_limit_time = DailyLimitTime(**new_daily_limit_time_data)
        self.save_data(new_daily_limit_time)
        return {"message": "Item de formulário adicionado com sucesso a um usuário."}, 201

@blp.route("/daily_limit_time/<int:team_id>")
class DailyLimitTimeId(ResourceModel):
    @is_logged_in
    @blp.response(200, DailyLimitTimeResponseSchema)
    def get(self, team_id):
        daily_limit_time = DailyLimitTime.query.filter_by(team_id=team_id).first()
        if not daily_limit_time:
            return {"code": 404, "status": "Not Found"}, 404
        return daily_limit_time, 200
 
    @is_logged_in
    @handle_exceptions
    @blp.arguments(DailyLimitTimeQueryParamsSchema, location="query")
    @blp.response(200)
    def patch(self, args, team_id):
        daily_limit_time = DailyLimitTime.query.filter_by(team_id=team_id).first()
        if not daily_limit_time:
            return {"code": 404, "status": "Not Found"}, 404

        for key, value in args.items():
            if value is not None:
                setattr(daily_limit_time, key, value)

        self.save_data(daily_limit_time)
        return {"message": "Tempo limite de daily do time editado com sucesso"}, 200   
    @is_logged_in
    @handle_exceptions
    def delete(self, id):
        daily_limit_time = DailyLimitTime.query.get_or_404(id)
        self.delete_data(daily_limit_time)
        return {"message": "Tempo limite de daily do time removido com sucesso de um usuário."}, 200


