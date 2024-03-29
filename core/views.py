from rest_framework.viewsets import ModelViewSet
from Livraria.core.models import Livro
from Livraria.core.serializers import LivroDetailSerializer, LivroSerializer

from core.models import Categoria, Editora
from core.serializers import CategoriaSerializer, EditoraSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroDetailSerializer
        return LivroSerializer