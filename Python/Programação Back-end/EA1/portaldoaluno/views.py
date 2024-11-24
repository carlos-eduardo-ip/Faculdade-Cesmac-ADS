from django.shortcuts import render, redirect
from .models import Aluno, Curso
from .forms import CreateAlunoForm, CreateCursoForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlunoSerializer, CursoSerializer

class AlunoAPIView(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    
class AlunoDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            aluno = Aluno.objects.get(id=pk)
            serializer = AlunoSerializer(aluno)
            return Response(serializer.data)
        except Aluno.DoesNotExist:
            return Response({"error": "Aluno não encontrado!"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

def home(request):
    return render(request, 'portaldoaluno/pages/home.html')

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'portaldoaluno/pages/listar_alunos.html', {'alunos': alunos})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'portaldoaluno/pages/listar_cursos.html', {'cursos': cursos})

def create_aluno(request):
    if request.method == 'POST':
        form = CreateAlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portaldoaluno:listar_alunos')
    else:
        form = CreateAlunoForm()
    return render(request, 'portaldoaluno/pages/create_aluno.html', {'form' : form})

def create_curso(request):
    if request.method == 'POST':
        form = CreateCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portaldoaluno:listar_cursos')
    else:
        form = CreateCursoForm()
    return render(request, 'portaldoaluno/pages/create_curso.html', {'form' : form})
