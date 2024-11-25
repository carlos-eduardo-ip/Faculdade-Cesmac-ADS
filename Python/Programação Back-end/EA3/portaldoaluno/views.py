from django.shortcuts import render, redirect
from .models import Usuario
from .forms import CreateUsuarioForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuariosSerializer

class UsuarioAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        usuario = Usuario.objects.all()
        serializer = UsuariosSerializer(usuario, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            usuario = Usuario.objects.get(id=pk)
            serializer = UsuariosSerializer(usuario)
            return Response(serializer.data)
        except usuario.DoesNotExist:
            return Response({"error": "Usuario não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
    
def home(request):
    return render(request, 'portaldoaluno/pages/home.html')

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'portaldoaluno/pages/listar_usuarios.html', {'usuarios': usuarios})

def create_usuario(request):
    if request.method == 'POST':
        form = CreateUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portaldoaluno:listar_usuarios')
    else:
        form = CreateUsuarioForm()
    return render(request, 'portaldoaluno/pages/create_usuario.html', {'form' : form})
