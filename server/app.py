#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
from models import User, Recipe

class Signup(Resource):
  def post(self):
    json = request.get_json()
    
    user = User(
       username=json.get('username'),
       image_url=json.get('image_url'),
       bio = json.get('bio'))
    
    user.password_hash = json.get('password')

    try:
      db.session.add(user)
      db.session.commit()
      session['user_id'] = user.id
      return user.to_dict(), 201
    except IntegrityError:
       return {'error': 'Unproccessable Entity'}, 422
    
class CheckSession(Resource):
    pass

class Login(Resource):
    pass

class Logout(Resource):
    pass

class RecipeIndex(Resource):
    pass

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(RecipeIndex, '/recipes', endpoint='recipes')


if __name__ == '__main__':
    app.run(port=5555, debug=True)