from .. import db, flask_bcrypt


class Person(db.Model):
    """ Person Model """
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(25), unique=True, nullable=True)
    # language = db.Column(db.String(25), nullable=True)
    # country = db.Column(db.String(255), nullable=True)
    # company = db.Column(db.String(255), nullable=True)
    # currency = db.Column(db.String(255), nullable=True)
    # role = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255), nullable=True)
    created_date = db.Column(db.DateTime, nullable=True)
    created_user = db.Column(db.String(100), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True)
    updated_user = db.Column(db.String(100), nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=True)
