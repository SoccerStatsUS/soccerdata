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
        'name': 'Estadio Manuel Ferreira',
        'location': 'Asunción, Paraguay',
        'opened': 1964,
        'capacity': 18000,
        },


    {
        'name': 'Estádio Urbano Caldeira',
        'location': 'Santos, Brazil',
        'opened': datetime.datetime(1916, 10, 12),
        'capacity': 16798,
        },


    {
        'name': 'Estadio José Antonio Anzoátegui',
        'location': 'Puerto La Cruz, Venezuela',
        'opened': datetime.datetime(1965, 12, 8),
        'capacity': 37485,
        'cost': 60400000,
        },


    {
        'name': 'Estadio Miguel Grau (Piura)',
        'location': 'Piura, Peru',
        'opened': datetime.datetime(1958, 6, 7),
        'capacity': 25000,
        },


    {
        'name': 'Estadio Metropolitano Roberto Meléndez',
        'location': 'Barranquilla, Colombia',
        'opened': 1986,
        'capacity': 49612,
        },

    {
        'name': 'Estadio Feliciano Cáceres',
        'location': 'Luque, Paraguay',
        'opened': 1999,
        'capacity': 25000
        },

    {
        'name': 'Estadio General Pablo Rojas',
        'location': 'Asunción, Paraguay',
        'opened': 1992,
        'capacity': 32910,
        },


    {
        'name': 'Estadio San Juan del Bicentenario',
        'location': 'San Juan, Argentina',
        'opened': datetime.datetime(2011, 3, 16),
        'capacity': 25286,
        },

    {
        'name': 'Centro Esportivo Miécimo da Silva',
        'location': 'Rio de Janeiro, Brazil',
        'opened': 1997,
        'capacity': 1953,
        },

    {
        'name': 'Estadio Valparaiso Sporting Club',
        'location': 'Viña del Mar, Chile',
        'opened': 1882,
        },




    {
        'name': 'Estadio Guillermo Plazas Alcid',
        'location': 'Neiva, Colombia',
        'opened': datetime.datetime(1980, 11, 28),
        'capacity': 22000,
        },


    {
        'name': 'Estadio Olímpico de la UCV',
        'location': 'Caracas, Venezuela',
        'opened': 1951,
        'cost': 16000000,
        'capacity': 24900,
        },

    {
        'name': 'Estadio Elías Aguirre',
        'location': 'Chiclayo, Peru',
        'opened': 1970,
        'capacity': 24500,
        },

    {
        'name': 'Estadio Mansiche',
        'location': 'Trujillo, Peru',
        'opened': datetime.datetime(1946, 10, 12),
        'capacity': 24000,
        },


    {
        'name': 'Estadio Jorge Basadre',
        'location': 'Tacna, Peru',
        'opened': 2000,
        'capacity': 19850,
        },


    {
        'name': 'Estadio Hernán Ramírez Villegas',
        'location': 'Pereira, Colombia',
        'opened': 1971,
        'capacity': 30313,
        },



    {
        'name': 'Estadio Alberto J. Armando',
        'location': 'Buenos Aires, Argentina',
        'opened': datetime.datetime(1940, 5, 25),
        'capacity': 49000,
        },


    {
        'name': 'Estadio de Independiente',
        'location': 'Avellaneda, Argentina',
        'opened': 1928,
        'capacity': 40000,
        },


    {
        'name': 'Estadio Brígido Iriarte',
        'location': 'Caracas, Venezuela',
        'opened': 1983,
        'capacity': 10000
        },

    {
        'name': 'Estadio Malvinas Argentinas',
        'location': 'Mendoza, Argentina',
        'opened': 1978,
        'capacity': 45268,
        },


    {
        'name': 'Estadio Padre Ernesto Martearena',
        'location': 'Salta, Argentina',
        'opened': 2001,
        'capacity': 20408,
        },

    {
        'name': 'Estadio San Juan del Bicentenario',
        'location': 'San Juan, Argentina',
        'opened': datetime.datetime(2011, 3, 16),
        'capacity': 25286,
        },


    {
        'name': 'Estadio Brigadier General Estanislao López',
        'location': 'Santa Fe, Argentina',
        'opened': datetime.datetime(1946, 7, 9),
        'capacity': 47000,
        },


    {
        'name': 'Estadio Ciudad de La Plata',
        'location': 'La Plata, Argentina',
        'opened': datetime.datetime(2003, 6, 7),
        'capacity': 36000,
        'cost': 100000000,
        'architect': 'Roberto Ferreira',
        },

    {
        'name': 'Estadio 23 de Agosto',
        'location': 'San Salvador de Jujuy',
        'opened': datetime.datetime(1973, 3, 18),
        'capacity': 24000,
        },

    {
        'name': 'Estádio São Januário',
        'location': 'Rio de Janeiro, Brazil',
        'opened': datetime.datetime(1927, 4, 21),
        'capacity': 25000,
        },

    {
        'name': 'Estadio G.E.B.A.',
        'address': '3600 Dorrego Avenue',
        'location': 'Buenos Aires, Argentina',
        'capacity': 18000,
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
        'name': 'Estadio Parque Artigas',
        'location': 'Paysandú, Uruguay',
        'opened': 1994,
        'capacity': 25000,
        },


    {
        'name': 'Estádio General Severiano',
        'location': 'Rio de Janeiro, Brazil',
        'opened': datetime.datetime(1913, 5, 13), 
        'capacity': 20000,
        },


    {
        'name': 'Estádio Parque do Sabiá',
        'location': 'Uberlândia, Brazil',
        'opened': datetime.datetime(1982, 5, 27),
        'capacity': 50000,
        },




    {
        'name': 'Estádio do Morumbi',
        'location': 'Sao Paulo, Brazil',
        'opened': datetime.datetime(1960, 10, 2),
        'capacity': 67428,
        },


    {
        'name': 'Estadio 9 de Mayo',
        'location': 'Machala, Ecuador',
        'opened': datetime.datetime(1955, 5, 9),
        'capacity': 16500,
        },


    {
        'name': 'Estadio Municipal de Concepción',
        'location': 'Concepción, Chile',
        'opened': datetime.datetime(1962, 9, 16),
        'capacity': 29000,
        },


    {
        'name': 'Estadio Monumental Isidro Romero Carbo',
        'location': 'Guayaquil, Ecuador',
        'opened': datetime.datetime(1987, 12, 27),
        'capacity': 90283,
        'cost': 70000000,
        },

    {
        'name': 'Estadio George Capwell',
        'opened': datetime.datetime(1945, 10, 21),
        'location': 'Guayaquil, Ecuador',
        'capacity': 24019,
        },

    {
        'name': 'Estadio El Campín',
        'location': 'Bogotá, Colombia',
        'opened': datetime.datetime(1938, 8, 14),
        'capacity': 40343,
        },


    {
        'name': 'Estadío Centenario',
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
        'name': 'Parque Pereira',
        'location': 'Montevideo, Uruguay',
        'capacity': 40000,
        },

    {
        'name': 'Estadio Pocitos',
        'location': 'Montevideo, Uruguay',
        'opened': datetime.datetime(1921, 11, 6),
        'capacity': 1000,
        },

    {
        'name': 'Estádio Independência',
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
        'name': 'Estadio Metropolitano de Mérida',
        'location': 'Mérida, Venezuela',
        'opened': 2005,
        'cost': 107000000,
        'capacity': 42200,
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
        'name': 'Estadio Nacional de Peru',
        'location': 'Lima, Peru',
        'opened': datetime.datetime(1952, 10, 27),
        'capacity': 40000,
        },

    {
        'name': 'Estádio das Laranjeiras',
        'location': 'Rio de Janeiro, Brazil',
        },

    {
        'name': 'Estadio Sportivo Barracas',
        'opened': datetime.datetime(1913, 10, 30),
        'location': 'Buenos Aires, Argentina',
        'capacity': 30000,
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
        'name': 'Estadio Modelo Alberto Spencer Herrera',
        'location': 'Guayaquil, Ecuador',
        'opened': 1959,
        'capacity': 42000,
        },

    {
        'name': 'Estadio Hernando Siles',
        'location': 'La Paz, Bolivia',
        'opened': 1930,
        'capacity': 42000,
        },

    {
        'name': 'Estadio Félix Capriles',
        'location': 'Cochabamba, Bolivia',
        'opened': 1938,
        'capacity': 32000,
        },


    {
        'name': 'Estadio Alejandro Villanueva',
        'location': 'Lima, Peru',
        'opened': datetime.datetime(1974, 12, 27),
        'capacity': 40000,
        },

    {
        'name': 'Estadio Olímpico Atahualpa',
        'location': 'Quito, Ecuador',
        'opened': datetime.datetime(1951, 11, 25),
        'capacity': 39816,
        },

    {
        'name': 'Estadio Alejandro Serrano Aguilar',
        'location': 'Cuenca, Ecuador',
        'opened': 1945,
        'capacity': 22000,
        },

    {
        'name': 'Estadio Reales Tamarindos',
        'location': 'Portoviejo, Ecuador',
        'opened': 1970,
        'capacity': 18000,
        },


    {
        'name': 'Estadio Atilio Paiva Olivera',
        'location': 'Rivera, Uruguay',
        'opened': 1927,
        'capacity': 26000,
        },


    {
        'name': 'Estadio Ramón Tahuichi Aguilera',
        'location': 'Santa Cruz de la Sierra, Bolivia',
        'opened': datetime.datetime(1940, 5, 25),
        'capacity': 38000,
        },


    {
        'name': 'Estadio Defensores del Chaco',
        'location': 'Asunción, Paraguay',
        'opened': 1917,
        'capacity': 36000,
        },


    {
        'name': 'Estadio Monumental Antonio Vespucio Liberti',
        'location': 'Buenos Aires, Argentina',
        'opened': datetime.datetime(1938, 5, 25),
        'capacity': 67664,
        },


    {
        'name': 'Estadio Jesús Bermúdez',
        'location': 'Oruro, Bolivia',
        'capacity': 28000,
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
        'name': 'Estadio Campos de Sports de Ñuñoa',
        'location': 'Santiago, Chile',
        'opened': 1938,
        'capacity': 20000,
        },


    {
        'name': 'Mineirão',
        'location': 'Belo Horizonte, Brazil',
        'opened': datetime.datetime(1965, 9, 5),
        'capacity': 62160,
        },

    {
        'name': 'Estadio Gasómetro',
        'location': 'Buenos Aires, Argentina',
        'capacity': 75000,
        },

    {
        'name': 'Estadio Alvear y Tagle',
        'location': 'Buenos Aires, Argentina',
        'capacity': 40000,
        'closed': 1938,
        },

    {
        'name': 'Estadio Ministro Brin y Senguel',
        'location': 'Buenos Aires, Argentina',
        'opened': 1916,
        'closed': 1938,
        'capacity': 25000,
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
        'name': 'Estadio Polideportivo de Pueblo Nuevo',
        'location': 'San Cristóbal, Venezuela',
        'opened': datetime.datetime(1976, 1, 11),
        'capacity': 38755,
        },


    {
        'name': 'Polideportivo Cachamay',
        'location': 'Puerto Ordaz, Venezuela',
        'opened': 1990,
        'capacity': 41600,
        'cost': 74400000,
        },


    {
        'name': 'Estadio José Pachencho Romero',
        'location': 'Maracaibo, Venezuela',
        'opened': 1971,
        'capacity': 40800,
        'cost': 14100000,
        },

    {
        'name': 'Estadio Monumental de Maturín',
        'location': 'Maturín, Venezuela',
        'opened': datetime.datetime(2007, 6, 17),
        'capacity': 52000,
        'cost': 85000000,
        },

    {
        'name': 'Estadio Metropolitano de Fútbol de Lara',
        'location': 'Barquisimeto, Venezuela',
        'opened': 2007,
        'capacity': 45312,
        'cost': 74400000
        },

    {
        'name': 'Estadio Garcilaso',
        'location': 'Cusco, Peru',
        'opened': 1960,
        'capacity': 45000,
        },


    {
        'name': 'Estadio Atanasio Girardot',
        'location': 'Medellín, Colombia',
        'opened': datetime.datetime(1953, 3, 19),
        'capacity': 45943,
        },


    {
        'name': 'Estádio Fonte Nova',
        'location': 'Salvador, Brazil',
        'opened': 1951,
        'capacity': 60000,
        },

    {
        'name': 'Estádio Serra Dourada',
        'location': 'Goiânia, Brazil',
        'opened': 1975,
        'capacity': 41574,
        },


    {
        'name': 'Estádio do Arruda',
        'location': 'Recife, Brazil',
        'opened': 1972,
        'capacity': 60044,
        },



    {
        'name': 'Estadio Elías Figueroa Brander',
        'location': 'Valparaíso, Chile',
        'opened': datetime.datetime(1931, 12, 25),
        'capacity': 18500,
        },

    {
        'name': 'Estadio Monumental Virgen de Chapi',
        'location': 'Arequipa, Peru',
        'opened': 1993,
        'capacity': 60000,
        'cost': 7000000,
        },


    {
        'name': 'Estadio Olímpico Pascual Guerrero',
        'location': 'Cali, Colombia',
        'opened': datetime.datetime(1937, 7, 20),
        'capacity': 35694
        },


    {
        'name': 'Estadio Antonio Oddone Sarubbi',
        'location': 'Ciudad del Este, Paraguay',
        'opened': 1973,
        'capacity': 23500,
        },


    {
        'name': 'Estadio Olímpico Patria',
        'location': 'Sucre, Bolivia',
        'opened': 1992,
        'capacity': 32000,
        },


    {
        'name': 'Estadio Suppici',
        'location': 'Colonia del Sacramento, Uruguay',
        'capacity': 12000,
        },


    {
        'name': 'Monumental Río Parapití',
        'location': 'Pedro Juan Caballero, Paraguay',
        'opened': 1999,
        'capacity': 18000,
        },


    {
        'name': 'Estádio Parque Antarctica',
        'location': 'Sao Paulo, Brazil',
        'opened': datetime.datetime(1902, 5, 3),
        'closed': datetime.datetime(2010, 7, 9),
        'capacity': 27650,
        },

    {
        'name': 'Estadio Palogrande',
        'location': 'Manizales, Colombia',
        'opened': 1936,
        'capacity': 42553,
        'cost': 5500000,
        'denomination': 'Colombian peso',
        },


    {
        'name': 'Estadio Centenario de Armenia',
        'location': 'Armenia, Colombia',
        'opened': 1988,
        'capacity': 29000,
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
