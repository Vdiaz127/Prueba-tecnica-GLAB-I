from PruebaTecnicaGLAB.templeates import *
from django.shortcuts import render, redirect
from reservations.models import *
from django.contrib.auth import authenticate, login, logout
from .backend import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def inicio(request):
    return redirect('formulario de reservacion')

def cerrar_sesion(request):
    logout(request)
    return redirect('formulario de reservacion')

def inicio_sesion(request):
    next_page = request.GET.get('next')

    if request.method == 'POST':
        correo = request.POST['correo']
        clave = request.POST['contraseña']

        if usuario_admin(correo)==False:
            error_login = 'Correo corresponde a un usuario comun, no a un administrador'
            return render(request, 'login.html', {'error': error_login})
        
        usuario = authenticate(request, correo_id=correo, contraseña=clave)

        if usuario is not None:
            login(request, usuario)
            if next_page:
                return redirect(next_page)  # Redirigir al usuario a la página 'next' después de iniciar sesión
            else:
                return redirect('lista de reservaciones')
        else:
            error_login = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render(request, 'login.html', {'error': error_login})
        
    return render(request, 'login.html',{'next_page': next_page})

def registrar_administrador(request):
    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        correo = request.POST['email']
        password = request.POST['password']
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']

        if verificar_correo(correo):
            messages.error(request, 'Correo ya esta en uso, utilice otro', extra_tags='register_denied')
            redirect('registrar admin')
        
        else:
            usuario = Usuario(
                nombres=nombres,
                apellidos=apellidos,
                correo=correo,
                tipo_documento=tipo_documento,
                numero_documento=numero_documento,
                rol = 'administrador'
            )

            usuario.save()

            Usuario_Admin.objects.create_user(
                correo=usuario,
                clave=password,
            )

            messages.error(request, 'Usuario administrador registrado, ahora por favor loguese', extra_tags='register_succesfull ')
            return redirect('login')

    return render(request, 'registrar_admin.html')

def registrar_reserva(request):
    if request.method == 'POST':

        #Usuario Reservacion:
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']
        correo = request.POST['correo']

        #Reservacion:
        fecha_r = request.POST['fecha']
        t_r = request.POST['tipo_reserva']
        cant = request.POST['cantidad_personas']
        desc = request.POST['descripcion']

        usuario_nuevo = Usuario(
            nombres = nombres,
            apellidos = apellidos,
            tipo_documento = tipo_documento,
            numero_documento=numero_documento,
            correo = correo
        )

        if verificar_correo(correo)==False:
            usuario_nuevo.save()
            messages.error(request, 'Usuario y reserva registrados', extra_tags='registro_ambos')
        else:
            messages.error(request, 'Se registro la reserva nueva pero no el ususario, esto debido a que el correo ya esta registrado.', extra_tags='correo_duplicado')
            
        reservacion_n = Reservacion(
            usuario = usuario_nuevo,
            fecha_reservacion = fecha_r,
            tipo_reserva = t_r,
            cantidad_personas = cant,
            descripcion = desc
        )

        reservacion_n.save()
        
        return redirect('formulario de reservacion')

    return render(request, 'formulario_reserva.html')


@login_required(login_url='login')
def listar_reservaciones(request):
    listadoReservas = Reservacion.objects.all()
    return render(request, "listado_de_reservas(admin).html",{"listaReserva":listadoReservas})

def editar_datos(request):
    if request.method == 'POST':
        
        id_u = request.POST['reserva_id']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        tipo_documento = request.POST['tipo_documento']
        numero_documento = request.POST['numero_documento']
        fecha_r = request.POST['fecha']
        t_r = request.POST['tipo_reserva']
        cant = request.POST['cantidad_personas']
        desc = request.POST['descripcion']

        r_e = Reservacion.objects.get(id=id_u)

        Reservacion.objects.filter(id=id_u).update(
            fecha_reservacion=fecha_r,
            tipo_reserva=t_r,
            cantidad_personas=cant,
            descripcion=desc
        )

        Usuario.objects.filter(correo=r_e.usuario.correo).update(
            nombres=nombres,
            apellidos=apellidos,
            tipo_documento=tipo_documento,
            numero_documento=numero_documento
        )

        return redirect('lista de reservaciones')

    return render(request, 'listado_de_reservas(admin).html')

def confirmar_reserva(request):
    if request.method == 'POST':
        id_reserva = request.POST['r_id']
        actualizar_r = Reservacion.objects.get(id=id_reserva)
        if actualizar_r is not None:
            actualizar_r.reservado = True
            actualizar_r.save()
            return redirect('lista de reservaciones')
        else:
            print('error')





