from app import db

class DayImage(db.Document):
    title = db.StringField(required=True)
    url = db.StringField(required=True)

class Covid(db.Document):
    id_caso = db.StringField(required=True)
    fecha_diagnostico = db.StringField(required=True)
    ciudad_ubicacion = db.StringField(required=True)
    departamento = db.StringField(required=True)
    atencion = db.StringField(required=True)
    edad = db.StringField(required=True)
    sexo = db.StringField(required=True)
    tipo = db.StringField(required=True)
    pais_procedencia = db.StringField(required=True)
