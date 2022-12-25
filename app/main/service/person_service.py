import uuid
import datetime

from sqlalchemy import or_

from app.main import db
from app.main.model.Person import Person
from marshmallow import ValidationError


def get_all_persons():
    return None


def create_person(data):
    person = Person.query.filter_by(
        email=data['email']
    ).first()
    if not person:
        new_person = Person(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            address=data['address'],
            phone=data['phone'],
            avatar=data['avatar'],
            created_date=datetime.datetime.utcnow(),
            created_user="",
            updated_date=datetime.datetime.utcnow(),
            updated_user="",
            is_deleted=False,
        )
        save_changes(new_person)
        response = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response, 201
    else:
        response = {
            'status': 'false',
            'message': 'Person already exists. Please Log in.'
        }
    return response, 400


def get_person(id):
    return None


def save_changes(data):
    db.session.add(data)
    db.session.commit()
