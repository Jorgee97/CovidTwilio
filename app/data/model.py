from app import db

class DayImage(db.Document):
    title = db.StringField(required=True)
    url = db.StringField(required=True)