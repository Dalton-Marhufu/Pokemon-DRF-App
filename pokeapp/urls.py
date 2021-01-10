from django.urls import path
from .views import Pokeapp, RandomPokemon, HpPokemon

app_name = 'Pokeapp'

urlpatterns = [

    path('',Pokeapp.as_view(), name='pokeapp'),
    path('random/', RandomPokemon.as_view(), name='test'),
    path('hp/', HpPokemon.as_view(), name='test1'),

]
