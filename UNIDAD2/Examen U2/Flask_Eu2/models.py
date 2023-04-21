from app import db

class Personal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

class Titulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Oficina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion=db.Column(db.String(100), nullable=False)

class Area(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    

class Cargo(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    nombre =db.Column(db.String(50), nullable=False)


