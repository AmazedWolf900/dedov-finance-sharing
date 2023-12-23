from app.extensions import db
from sqlalchemy.sql import func

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))

    payments = db.relationship('Payment', cascade="all, delete-orphan")

    created_at = db.Column(db.DateTime(timezone = True),
                           server_default=func.now())

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)

    attachments = db.relationship('Attachment', cascade="all, delete-orphan")
    items = db.relationship('Item', cascade="all, delete-orphan")

    created_at = db.Column(db.DateTime(timezone = True),
                           server_default=func.now())

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    cost = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Float)

    project_id = db.Column(db.Integer, db.ForeignKey("project.id", ondelete='cascade'), nullable=False)

    attachments = db.relationship('Attachment', cascade="all, delete-orphan")
    payments = db.relationship('Payment', cascade="all, delete-orphan")

    created_at = db.Column(db.DateTime(timezone = True),
                           server_default=func.now())

class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(255), nullable=False, unique=True)
    file_name = db.Column(db.String(255), nullable=False, unique=True)
    file_extension = db.Column(db.String(5), nullable=False)
    common_name = db.Column(db.String(255), nullable=False)
    file_size = db.Column(db.Float, nullable=False)

    payment_id = db.Column(db.Integer, db.ForeignKey("payment.id", ondelete='cascade'))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id", ondelete='cascade'))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id", ondelete='cascade')) 

    created_at = db.Column(db.DateTime(timezone = True),
                           server_default=func.now())

class Paymentmethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)

    payment_method_id = db.Column(db.Integer, db.ForeignKey("paymentmethod.id", ondelete='cascade'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id", ondelete='cascade'), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete='cascade'),  nullable=False)

    attachments = db.relationship('Attachment', cascade="all, delete-orphan")

    created_at = db.Column(db.DateTime(timezone = True),
                           server_default=func.now())