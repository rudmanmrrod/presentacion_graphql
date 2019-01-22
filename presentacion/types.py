import graphene
from graphene_django.types import DjangoObjectType

from .models import Presentacion

class PresentacionType(DjangoObjectType):
    class Meta:
        model = Presentacion


class Query(object):
    presentacion = graphene.Field(PresentacionType,
    id=graphene.Int())
    presentaciones = graphene.List(PresentacionType)

    def resolve_presentaciones(self, info, **kwargs):
        return Presentacion.objects.all()

    def resolve_presentacion(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Presentacion.objects.get(pk=id)

        return None