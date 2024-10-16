import folium
import json
from .models import Pokemon, PokemonEntity
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    time = localtime()
    pokemons = PokemonEntity.objects.filter(appeared_at__lt=time, disappeared_at__gt=time)
    for pokemon in pokemons:
        print("pokemon:", pokemon)
        add_pokemon(
            folium_map,
            pokemon.lat,
            pokemon.lon,
            request.build_absolute_uri(pokemon.pokemon.photo.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    print("pokemons")
    print(pokemons)
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo,
            'title_ru': pokemon.title,
        })
    print("pokemons_on_page")
    print(pokemons_on_page)
    
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    time = localtime()
    pokemon = Pokemon.objects.get(id=pokemon_id)
    print("pokemon1:", pokemon)
    pokemon_entities =  PokemonEntity.objects.filter(pokemon=pokemon, appeared_at__lt=time, disappeared_at__gt=time)
    print("pokemon_entities:", pokemon_entities)
    for pokemon_entity in pokemon_entities:
        print("pokemon_entity:", pokemon_entity)
        add_pokemon(
                folium_map, 
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
            )
        break
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    pokemon = {
        "title_ru": pokemon.title,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description
    }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
