import uuid
import datetime

from sqlalchemy import or_

from app.main import db
from app.main.model.Person import Person
from marshmallow import ValidationError


def get_all_persons():
    person = Person.query.all()
    response = [
        {
            "first_name": item.first_name,
            "last_name": item.last_name,
            "email": item.email,
            "address": item.address,
            "phone": item.phone,
            "avatar": item.avatar,
            "created_date": item.created_date,
            "created_user": item.created_user,
            "updated_date": item.updated_date,
            "updated_user": item.updated_user,
            "is_deleted": item.is_deleted
        }
        for item in person
    ]
    return response


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
