from flask import Blueprint, request
from flask_restful import Api, Resource
from api.models import User
from api.schemas import UserSchema

users_v1_bp = Blueprint('users_v1_bp', __name__)
user_schema = UserSchema()
api = Api(users_v1_bp)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return user_schema.dump(user)


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return user_schema.dump(users, many=True)

    def post(self):
        data = request.get_json()
        user_dict = user_schema.load(data)
        password = user_dict.pop('password')

        user = User(**user_dict)
        user.password = password
        user.save()

        return user_schema.dump(user)


api.add_resource(UserResource, '/api/v1/users/<int:user_id>/')
api.add_resource(UserListResource, '/api/v1/users/')
