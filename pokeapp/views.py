from django.shortcuts import render
from .models import Pokemon
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PokemonSerializer, RandomPokemonSerializer, HpPokemonSerializer


class Pokeapp(generics.ListAPIView):

    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()

class RandomPokemon(generics.ListAPIView):

    serializer_class = RandomPokemonSerializer
    queryset = Pokemon.objects.order_by('?')[:5]

#class HpPokemon(generics.ListAPIView):

    #serializer_class = HpPokemonSerializer
    #queryset = Pokemon.objects.filter(type_1='fire')

class HpPokemon(generics.ListAPIView):

    def get(self,request,Format=None, **kwargs):
        question = Pokemon.objects.filter(name=kwargs).order_by('?')[:1]
        serializer = HpPokemonSerializer(question)
        return Response(serializer.data)
