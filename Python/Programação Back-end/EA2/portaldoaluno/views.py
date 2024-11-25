from django.shortcuts import render, redirect
from .models import Produto
from .forms import CreateProdutoForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProdutoSerializer

class ProdutoAPIView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProdutoDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            produto = Produto.objects.get(id=pk)
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        except produto.DoesNotExist:
            return Response({"error": "Produto não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
    

def home(request):
    return render(request, 'portaldoaluno/pages/home.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'portaldoaluno/pages/listar_produtos.html', {'produtos': produtos})

def create_produtos(request):
    if request.method == 'POST':
        form = CreateProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portaldoaluno:listar_produtos')
    else:
        form = CreateProdutoForm()
    return render(request, 'portaldoaluno/pages/create_produto.html', {'form' : form})
