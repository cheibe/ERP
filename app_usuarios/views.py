from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from app_usuarios.models import CustomUser
from app_usuarios.forms import CustomUserCreationForm, EditCustomUserCreationForm, EditPasswordCustomUserForm
from app_usuarios.tables import UsuarioTable
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User

def usuarios_view(request):
    usuarios = CustomUser.objects.all()
    table = UsuarioTable(usuarios)
    return render(request, 'pages/usuarios.html', context={
        'title': 'Usuários',
        'table': table
    })

def adicionar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            messages.success(request, f'O novo usuário "{novo_usuario.nome}" foi adicionado com sucesso! ')
            return redirect('usuarios:usuarios')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/adicionar_usuario.html', context={
        'title': 'Adicionar usuário',
        'form': form
    })

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, pk=usuario_id)
    if request.method == 'POST':
        form = EditCustomUserCreationForm(request.POST, instance=usuario)
        if form.is_valid():
            edit_usuario = form.save()
            messages.success(request, f'O usuário "{edit_usuario.nome}" foi editado com sucesso!')
            return redirect('usuarios:usuarios')
    else:
        form = EditCustomUserCreationForm(instance=usuario)
    return render(request, 'pages/adicionar_usuario.html', context={
        'title': 'Editar usuario',
        'form': form
    })

def editar_senha_usuario(request, usuario_id):
    usuario = CustomUser.objects.get(pk=usuario_id)
    if request.method == 'POST':
        form = SetPasswordForm(user=usuario, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'A senha do usuário foi alterada com sucesso!')
            return redirect('usuarios:usuarios')
    else:
        form = SetPasswordForm(user=usuario)
    return render(request, 'pages/adicionar_usuario.html', context={
        'title': f'Editar senha do usuário {CustomUser.nome}',
        'form': form
    })

def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, pk=usuario_id)

    usuario.delete()
    messages.success(request, f'O usuário foi deletado com sucesso!')
    return redirect('usuarios:usuarios')