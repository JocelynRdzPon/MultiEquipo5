from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import db
from flask_migrate import Migrate
from config import BasicConfig
from models import Usuario, Producto, Paqueteria
from Forms import UsuarioForm, ProductoForm, PaqueteriaForm
import logging

app = Flask(__name__)
app.config.from_object(BasicConfig)
db.init_app(app)

#Migraciones

migrate = Migrate()
migrate.init_app(app,db)

logging.basicConfig(level=logging.DEBUG, filename='debug.log') # El logging sirve para saber los errores que llega a tener la app

@app.route('/')
@app.route('/index.html')

def inicio():
    usuarios=Usuario.query.all()
    productos=Producto.query.all()
    return render_template('index.html', usuarios=usuarios, productos=productos)
    


@app.route('/agregar', methods=['GET','POST'])
def agregar():
    try:
        usuario=Usuario()
        usuarioForm = UsuarioForm(obj=usuario)
        if request.method == 'POST':
            if usuarioForm.validate_on_submit():
                usuarioForm.populate_obj(usuario)
                db.session.add(usuario)
                db.session.commit()
                return redirect(url_for('inicio'))
        return render_template('agregar.html', forma = usuarioForm)
    except:
        return jsonify({"status":400,"mensaje":"ERROR"})
        

@app.route('/Producto', methods=['GET','POST'])
def agregarProducto():
    try:
        producto=Producto()
        productoForm = ProductoForm(obj=producto)
        if request.method == 'POST':
            if productoForm.validate_on_submit():
                productoForm.populate_obj(producto)
                db.session.add(producto)
                db.session.commit()
                return redirect(url_for('inicio'))
        return render_template('agregarProducto.html', forma = productoForm)
    except:
        return jsonify({"status":400,"mensaje":"ERROR"})


@app.route('/paqueteria', methods=['GET','POST'])
def agregarPaqueteria():
    try:
        paqueteria=Paqueteria()
        paqueteriaForm = PaqueteriaForm(obj=paqueteria)
        if request.method == 'POST':
            if paqueteriaForm.validate_on_submit():
                paqueteriaForm.populate_obj(paqueteria)
                db.session.add(paqueteria)
                db.session.commit()
                return redirect(url_for('inicio'))
        return render_template('agregarPaqueteria.html', forma = paqueteriaForm)
    except:
        return jsonify({"status":400,"mensaje":"ERROR"})
    
@app.route('/ver/<int:id>')
def verDetalle(id):
    usuario = Usuario.query.get_or_404(id)
    return render_template('ver.html',usuario=usuario)

@app.route('/verProduct/<int:id>')
def verProducto(id):
    producto = Producto.query.get_or_404(id)
    return render_template('verProducto.html',producto=producto)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarProducto/<int:id>')
def eliminarProducto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('inicio'))


@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    usuarioForm = UsuarioForm(obj=usuario)
    if request.method == "POST":
        if usuarioForm.validate_on_submit():
            usuarioForm.populate_obj(usuario)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html',forma=usuarioForm)
    

@app.route('/editarProducto/<int:id>',methods=['GET','POST'])
def editarProducto(id):
    producto = Producto.query.get_or_404(id)
    productoForm = ProductoForm(obj=producto)
    if request.method == "POST":
        if productoForm.validate_on_submit():
            productoForm.populate_obj(producto)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarProducto.html',forma=productoForm)
