from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'Usuarios/usuarios.html', {'usuarios': usuarios})
