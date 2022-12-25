from flask_restplus import Api
from flask import Blueprint

from .main.controller.user.user import api as user_ns
from .main.controller.person.person import api as person_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='SWAGGER',
          version='1.0',
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(person_ns, path='/person')
