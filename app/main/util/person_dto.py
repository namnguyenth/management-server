from flask_restplus import Namespace, fields


class PersonDto:
    api = Namespace('person', description='person related operations')
    user = api.model(
        'person',
        {
            'first_name': fields.String(),
            'last_name': fields.String(),
            'email': fields.String(),
            'address': fields.String(),
            'phone': fields.String(),
            # language : fields.Integer(),
            # country : fields.Integer(),
            # company : fields.Integer(),
            # currency : fields.Integer(),
            # role : fields.Integer(),
            'avatar': fields.String(),
            'created_date': fields.DateTime(),
            'created_user': fields.String(),
            'updated_date': fields.DateTime(),
            'updated_user': fields.String(),
            'is_deleted': fields.Boolean()
        }
    )
