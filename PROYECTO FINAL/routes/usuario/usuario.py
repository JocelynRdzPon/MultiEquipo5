from flask import Blueprint, request,jsonify, render_template, url_for, redirect, make_response
from sqlalchemy import exc
from models import Usuario
from models import Tarea
from app import db,bcrypt
from auth import tokenCheck, obtenerInfo
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

appuser = Blueprint('appuser', __name__, template_folder="templates")

@appuser.route('/registro', methods =['POST'])
def registro():
    
    nombreUser = request.form['nombre']
    ApellidoUser = request.form['apellido']
    emailUser= request.form['email']
    userPass = request.form['password']
    searchUser = Usuario.query.filter_by(email=emailUser).first()
    if searchUser:
        mensaje = "El usuario ya existe"
        msj2="Ingrese un nuevo correo electrónico"
    else:
        usuario = Usuario(nombre=nombreUser, apellido=ApellidoUser,email=emailUser, password=userPass)
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje = "Usuario creado"
            msj2 = "Bienvenido/a"
        except exc.SQLAlchemyError as e:
            mensaje = "Error"
            msj2= ""
    return render_template('MsjRegistro.html', mensaje=mensaje, msj2=msj2, nombre=nombreUser, apellido=ApellidoUser)


@appuser.route('/login', methods=['POST'])
def login():
    
    emailUser = request.form['email']
    userPass = request.form['password']
    searchUser = Usuario.query.filter_by(email=emailUser).first()
    if searchUser:
        validation = bcrypt.check_password_hash(searchUser.password,userPass)
        if validation:
            auth_token = searchUser.encode_auth_token(user_id=searchUser.id)
            print(auth_token)
            if searchUser.admin:
                return redirect(url_for('appuser.vista_admin', auth_token=auth_token))
            else:
                return redirect(url_for('appuser.vista_usuario', auth_token=auth_token))
    return render_template('401.html')


# vista de las funciones del usuario
@appuser.route('/vistaUsuario')
def vista_usuario():
    token = request.args['auth_token']
    usuario = obtenerInfo(token)
    info_user = usuario['data']
    return render_template('indexUsuario.html', token=token, usuario=info_user)


@appuser.route('/vistaAdmin')
def vista_admin():
    token = request.args['auth_token']
    usuario = obtenerInfo(token)
    info_user = usuario['data']
    print(token)
    return render_template('indexAdmin.html', token=token, usuario=info_user)


# Muestra todos los usuarios si recibe un token de usuario admin
@appuser.route('/usuarios') #get
def obtenerUsuarios():
    token = request.args.get('token')
    usuario = obtenerInfo(token)
    info_user = usuario['data']
    if info_user['admin']:
        output = []
        usuarios = Usuario.query.all()
        for usuario in usuarios:
            usuarioData = {}
            usuarioData['id'] = usuario.id
            usuarioData['email'] = usuario.email
            usuarioData['password'] = usuario.password
            usuarioData['registered_on'] = usuario.registered_on
            usuarioData['admin'] = usuario.admin
            output.append(usuarioData)
    return render_template('ListUsuarios.html', usuarios = output, token = token)

@appuser.route('/createUser', methods=['GET', 'POST'])
def crear_usuario():
    token = request.args['token']
    usuario = obtenerInfo(token)
    info_user = usuario['data']
    return render_template('createUser.html', token=token, usuario=info_user)

@appuser.route('/registroAdmin', methods =['POST'])
def registroUser():
    token = request.args.get('token')
    print(token)
    nombreUser = request.form['nombre']
    ApellidoUser = request.form['apellido']
    emailUser= request.form['email']
    userPass = request.form['password']
    
    if request.form.get("admin"):
        adminUser = True
    else:
        adminUser = False
   
    searchUser = Usuario.query.filter_by(email=emailUser).first()
    if searchUser:
        mensaje = "El usuario ya existe"
        msj2="Ingrese un nuevo correo electrónico"
    else:
        usuario = Usuario(nombre=nombreUser, apellido=ApellidoUser,email=emailUser, password=userPass, admin=adminUser)
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje = "Usuario Administrador"
            msj2 = "Registro exitoso"
        except exc.SQLAlchemyError as e:
            mensaje = "Error"
            msj2= e._message
    return render_template('LoginMensajeAdmin.html', mensaje=mensaje, msj2=msj2, nombre=nombreUser, apellido=ApellidoUser)


@appuser.route('/generarPdf', methods=['GET', 'POST'])
def crear_pdf():
    return render_template('indexPdf.html')

@appuser.route('/generatePdf')
def generatePdf():
    usuarios=Usuario.query.all()
    listaUsuarios=[["ID","EMAIL","NOMBRE","APELLIDO","ADMIN"]]
    for usuario in usuarios:
        listaUsuarios.append([
            usuario.id,
            usuario.email,
            usuario.nombre,
            usuario.apellido,
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
