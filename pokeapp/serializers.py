from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = [

            'name',
            'type_1',
            'type_2',
            'lengendary',

        ]

class RandomPokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = [

            'name',
            'type_1',
            'type_2',
            'hp',
            'attack',
            'defense',
            'sp_atk',
            'sp_deffense',
            'speed',
            'generation',
            'lengendary',

        ]

class HpPokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = [

            'name',
            'hp',

        ]
