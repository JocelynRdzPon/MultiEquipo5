from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import db
from flask_migrate import Migrate
from config import BasicConfig
from models import Personal, Area, Titulo, Oficina, Cargo
from Forms import PersonalForm, OficinaForm, TituloForm, AreaForm, CargoForm

app = Flask(__name__)
app.config.from_object(BasicConfig)
db.init_app(app)

migrate = Migrate()
migrate.init_app(app,db)

@app.route('/')
@app.route('/index.html')

def inicio():
    personals=Personal.query.all()
    
    return render_template('index.html', personals=personals)

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    try:
        personal=Personal()
        personalForm = PersonalForm(obj=personal)
        if request.method == 'POST':
            if personalForm.validate_on_submit():
                personalForm.populate_obj(personal)
                db.session.add(personal)
                db.session.commit()
                return redirect(url_for('inicio'))
        return render_template('agregar.html', forma = personalForm)
    except:
        return jsonify({"status":400,"mensaje":"ERROR"})
    

@app.route('/ver/<int:id>')
def verDetalle(id):
    personal = Personal.query.get_or_404(id)
    return render_template('ver.html',personal=personal)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    personal = Personal.query.get_or_404(id)
    db.session.delete(personal)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    personal = Personal.query.get_or_404(id)
    personalForm = PersonalForm(obj=personal)
    if request.method == "POST":
        if personalForm.validate_on_submit():
            personalForm.populate_obj(personal)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html',forma=personalForm)
