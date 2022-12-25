from flask import request
from flask_restplus import Resource

from app.main.service.person_service import get_all_persons, create_person
from app.main.util.person_dto import PersonDto

api = PersonDto.api
_person = PersonDto.user


@api.route('/')
class PersonList(Resource):
    @api.doc('list_of_registered_persons')
    @api.marshal_list_with(_person, envelope='data')
    def get(self):
        """List all person"""
        return get_all_persons()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_person, validate=True)
    def post(self):
        """Creates a new person """
        data = request.json
        return create_person(data=data)


@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class Person(Resource):
    @api.doc('get a user')
    @api.marshal_with(_person)
    def get(self, id):
        """get a person by id"""
        return None
