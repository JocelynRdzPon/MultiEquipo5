from flask import Blueprint, request,jsonify, render_template, url_for, redirect, g, make_response
from sqlalchemy import exc
from models import Tarea
from models import Usuario
from app import db,bcrypt
from auth import tokenCheck, obtenerInfo
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

apptask = Blueprint('apptask', __name__, template_folder="templates")

# @apptask.route('/form/agregar')
# def formulario_registrar():
#     token = request.args.get('token')
#     return render_template('Agregar.html', token=token)


@apptask.route('/agregarTarea', methods=['GET','POST'])
def agregar_tarea():
    token = request.args.get('token')
    usuario = obtenerInfo(token)

    if request.method == 'POST':
      tituloT = request.form['titulo']
      descT = request.form['descripcion']
      fechaT = request.form['fecha']
      tarea = Tarea(titulo=tituloT, descripcion=descT, fecha=fechaT)
      db.session.add(tarea)
      db.session.commit()
      
      return redirect(url_for('apptask.ver_Tareas_admin', token=token))
    return render_template('indexAdmin.html', token=token, usuario=usuario)



@apptask.route('/VerTareas')
def ver_Tareas():
    token = request.args.get('token')
    usuario = obtenerInfo(token)
    info_user = usuario.get('data')
    tareas = Tarea.query.order_by(Tarea.fecha.asc()).all()
    
    if tareas:
        output = []
        for tarea in tareas:
            tareaData = {}
            tareaData['id'] = tarea.id
            tareaData['titulo'] = tarea.titulo
            tareaData['descripcion'] = tarea.descripcion
            tareaData['fecha'] = tarea.fecha
            tareaData['estado'] = tarea.estado
            output.append(tareaData)
    else:
        output = []

    return render_template('indexUsuario.html', tareas=output, token=token, usuario=info_user)

@apptask.route('/VerTareasAdmin')
def ver_Tareas_admin():
    token = request.args.get('token')
    tareas = Tarea.query.order_by(Tarea.fecha.asc()).all()
    
    if tareas:
        output = []
        for tarea in tareas:
            tareaData = {}
            tareaData['id'] = tarea.id
            tareaData['titulo'] = tarea.titulo
            tareaData['descripcion'] = tarea.descripcion
            tareaData['fecha'] = tarea.fecha
            tareaData['estado'] = tarea.estado
            output.append(tareaData)
    else:
        output = []

    return render_template('indexAdmin.html', tareas=output, token=token)
    



@apptask.route('/eliminarTarea', methods=["POST"]) 
def eliminar_Tarea():
    token = request.args.get('token')
    tarea_id = request.form['id']
    tarea = Tarea.query.filter_by(id=tarea_id).first()
    output = []
    if tarea:
        db.session.delete(tarea)
        db.session.commit()
        mensaje = "Tarea eliminada"
    
    tareas = Tarea.query.all()
    for tarea in tareas:
        tareaData = {}
        tareaData['id'] = tarea.id
        tareaData['titulo'] = tarea.titulo
        tareaData['descripcion'] = tarea.descripcion
        tareaData['fecha'] = tarea.fecha
        tareaData['estado'] = tarea.estado
        output.append(tareaData)
    
    return render_template('IndexAdmin.html', tareas=output, token=token)

@apptask.route('/generarPdf', methods=['GET', 'POST'])
def crear_pdf():
    return render_template('indexPdf.html')

@apptask.route('/generatePdf')
def generatePdf():
    usuarios=Usuario.query.all()
    listaUsuarios=[["ID","EMAIL","REGISTRADO","ADMIN"]]
    for usuario in usuarios:
        listaUsuarios.append([
            usuario.id,
            usuario.nombre,
            usuario.apellido,
            usuario.email,
            usuario.registrado,
            usuario.admin
        ])
    doc = SimpleDocTemplate("users.pdf",pagesize=letter)
    table=Table(listaUsuarios)

    tableStyle = TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
        ('FONTSIZE',(0,0),(-1,0),16),
        ('BOTTOMPADDING',(0,0),(-1,0),12),
        ('BACKGROUND',(0,1),(-1,-1),colors.white),
        ('GRID',(0,0),(-1,-1),1,colors.black)
        ])
    table.setStyle(tableStyle)

    text="LISTADO DE USUARIOS"
    textStyle = getSampleStyleSheet()["Normal"]
    textStyle.alignment=TA_CENTER
    paragraph=Paragraph(text,textStyle)
    elementos=[paragraph,table]
    doc.build(elementos)

    response =make_response(open("users.pdf","rb").read())
    response.headers['Content-Type']="application/pdf"
    response.headers['Content-Disposition']='inline;filename=users.pdf'
    return response
