#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


import datetime

l = [
    {
        'name': 'Stadio Luigi Ferraris',
        'location': 'Genoa, Italy',
        'opened': datetime.datetime(1997, 4, 11),
        'capacity': 10000,
        'cost': 26000000,
        'architect': 'HOK Sport',
        },

    
    {
        'name': 'Estadío Ramón Aguilera', 
        'location': 'Santa Cruz, Bolivia',
        'opened': datetime.datetime(1940, 5, 25),
        'capacity': 38000,
        },

    {
        'name': 'Estadio Nacional Julio Martínez Prádanos',
        'location': 'Santiago, Chile',
        'opened': datetime.datetime(1938, 12, 3),
        'capacity': 47000,
        },


    {
        'name': 'Estadío Francisco Sánchez Rumoros', 
        'location': 'Coquimbo, Chile',
        'opened': datetime.datetime(1970, 1, 7),
        'capacity': 17750,
        },


    {
        'name': 'General Artigas Stadium', 
        'location': 'Paysandú, Uruguay',
        },

    {
        'name': 'Estadio El Campín',
        'location': 'Bogotá, Colombia',
        'opened': datetime.datetime(1938, 8, 14),
        'capacity': 40343,
        },


    {
        'name': 'Estadio Centenario',
        'location': 'Montevideo, Uruguay',
        'opened': datetime.datetime(1930, 7, 21),
        'architect': 'Juan Antonio Scasso',
        'cost': 1000000,
        'capacity': 65235,
        },




    {
        'name': 'Parque Central',
        'location': 'Montevideo, Uruguay',
        'opened': 1900,
        'capacity': 25000,
        },

    {
        'name': 'Estadio Pocitos',
        'location': 'Montevideo, Uruguay',
        'opened': datetime.datetime(1921, 11, 6),
        'capacity': 1000,
        },

    {
        'name': 'Estadío Independencia', 
        'location': 'Belo Horizonte, Brazil',
        'opened': datetime.datetime(1950, 6, 25),
        'capacity': 25000,
        },

    {
        'name': 'Campus Municipal Stadium', 
        'location': 'Maldonado, Uruguay',
        },
    {
        'name': 'Estadio Bellavista', 
        'location': 'Ambato, Ecuador',
        'opened': datetime.datetime(1945, 7, 24),
        },

       {
        'name': 'Estadio Jose Panchencho Romero', 
        'location': 'Maracaibo, Venezuela',
        },


    {
        'name': 'Estadio Athagualpa de Quito',
        'location': 'Quito, Ecuador',
        'opened': datetime.datetime(1951, 11, 25),
        'capacity': 39816,
        },


    {
        'name': 'Estadio Metropolitano',
        'location': 'Barquisimeto, Venezuela',
        },

    {
        'name': 'Estadio Agustin Tovar',
        'location': 'Barinas, Venezuela',
        },

    {
        'name': 'Estadio Jose Panchenco Romero',
        'location': 'Maracaibo, Venezuela',
        },

    {
        'name': 'Estadío Parque Central',
        'location': 'Montevideo, Uruguay',
        },

    {
        'name': 'Estadío Durival de Brito', 
        'location': 'Curitiba, Brazil',
        },

    {
        'name': 'Estadío Esporte Clube Recife',
        'location': 'Recife, Brazil',
        },



    {
        'name': 'Estadío Centenario',
        'location': 'Montevideo, Uruguay',
        },

    {
        'name': 'Estadio Nacional de Peru',
        'location': 'Lima, Peru',
        'opened': datetime.datetime(1952, 10, 27),
        'capacity': 40000,
        },

    {
        'name': 'Stadío das Laranjeiras', 
        'location': 'Rio de Janeiro, Brazil',
        },


    
    {
        'name': 'Estadio Jose Panchenco Romero',
        'location': 'Maracaibo, Venezuela',
        },

    {
        'name': 'Estadio Sausalito',
        'location': 'Viña del Mar, Chile',
        'opened': 1929,
        'capacity': 18037,
        },

    {
        'name': 'Estadio Carlos Dittborn',
        'location': 'Arica, Chile',
        'opened': datetime.datetime(1962, 4, 15),
        'capacity': 14373
        },


    {
        'name': 'Estadio El Teniente',
        'location': 'Rancagua, Chile',
        'opened': 1945,
        'capacity': 14450,
        },

    {
        'name': 'Estadio Monumental Antonio Vespucio Liberti',
        'location': 'Buenos Aires, Argentina',
        'opened': datetime.datetime(1938, 5, 25),
        'capacity': 67664,
        },

    {
        'name': 'Estadio Gigante de Arroyito',
        'location': 'Rosario, Argentina',
        'opened': datetime.datetime(1929, 10, 27),
        'capacity': 41654,
        },

    {
        'name': 'Estadio José María Minella',
        'location': 'Mar del Plata, Argentina',
        'opened': 1978,
        'capacity': 35354,
        },



    {
        'name': 'Estadio Jose Amalfitani',
        'address': '9200 Juan B. Justo Av.',
        'location': 'Buenos Aires, Argentina',
        'opened': datetime.datetime(1943, 4, 11),
        'capacity': 49540,
        },

    {
        'name': 'Estadio Mario Alberto Kempes',
        'location': 'Cordoba, Argentina',
        'opened': datetime.datetime(1978, 5, 16),
        'capacity': 57000,
        },



    {
        'name': 'Estádio Ilha do Retiro',
        'location': 'Recife, Brazil',
        'opened': 1937,
        'capacity': 35020,
        },

    {
        'name': 'Estádio do Maracanã',
        'location': 'Rio de Janeiro, Brazil',
        'opened': datetime.datetime(1950, 6, 16),
        'capacity': 78838,
        },

    {
        'name': 'Estádio do Pacaembu',
        'location': 'Sao Paulo, Brazil',
        'opened': datetime.datetime(1940, 4, 27),
        'capacity': 40199,
        },

    {
        'name': 'Estádio Independência',
        'location': 'Belo Horizonte, Brazil',
        'opened': datetime.datetime(1950, 6, 25),
        'capacity': 25000,        
        },

    {
        'name': 'Estádio dos Eucaliptos',
        'location': 'Porto Alegre, Brazil',
        'opened': datetime.datetime(1931, 3, 15),
        'closed': 1969,
        'capacity': 20000,
        },

    {
        'name': 'Estádio Vila Capanema',
        'location': 'Curitiba, Brazil',
        'opened': datetime.datetime(1947, 1, 23),
        'capacity': 20000,
        },


    {
        'name': 'Estádio do Morumbi',
        'location': 'Sao Paulo, Brazil',
        'opened': datetime.datetime(1960, 10, 2),
        'capacity': 67428,
        },
    








]
