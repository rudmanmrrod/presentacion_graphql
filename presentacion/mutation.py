import graphene
from .models import *
from .types import *

class CreatePresentacionMutation(graphene.Mutation):
    class Input:
        titulo = graphene.String()
        texto = graphene.String()

    presentacion = graphene.Field(PresentacionType)

    @staticmethod
    def mutate(root, info, **kwargs):
        titulo = kwargs.get('titulo', '').strip()
        texto = kwargs.get('texto', '').strip()

        obj = Presentacion.objects.create(titulo=titulo,texto=texto)

        return CreatePresentacionMutation(presentacion=obj)

class Mutation(graphene.AbstractType):
  crear_presentacion = CreatePresentacionMutation.Field()