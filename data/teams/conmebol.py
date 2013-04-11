#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    {
        'name': 'EC Bahia',
        'founded': datetime.datetime(1931, 1, 1),
        'city': 'Salvador, Brazil',
        },

    {
        'name': 'Nacional Táchira',
        'founded': 1996,
        'city': 'Tachira, Venezuela',
        },

    {
        'name': 'Paulista FC',
        'founded': datetime.datetime(1909, 5, 17),
        'city': 'Jundiai, Brazil',
        },

    {
        'name': 'Sportivo Luqueño',
        'founded': datetime.datetime(1921, 5, 1),
        'city': 'Luque, Paraguay',
        },

    {
        'name': 'Juan Aurich',
        'founded': datetime.datetime(1922, 9, 3),
        'city': 'Chiclayo, Peru',
        },

    {
        'name': 'EC Vitória',
        'founded': datetime.datetime(1899, 5, 13),
        'city': 'Salvador, Brazil',
        },

    {
        'name': 'CD Santa Fe',
        'founded': datetime.datetime(1941, 2, 28),
        'city': 'Bogota, Colombia',
        },

    {
        'name': 'Deportivo Portugués',
        'founded': 1985,
        'city': 'Caracas, Venezuela',
        },

    {
        'name': 'Atlético Zulia',
        'founded': 1996,
        'city': 'Maracaibo, Venezuela',
        },

    {
        'name': 'Deportivo Galicia',
        'founded': 1985,
        'city': 'Aragua, Venezuela', # moved from Caracas
        },

    {
        'name': 'Cortuluá',
        'founded': datetime.datetime(1967, 10, 6),
        'city': 'Tulua, Colombia',
        },

    {
        'name': 'Paysandu',
        'founded': 1914,
        'city': 'Belem, Brazil',
        },

    {
        'name': 'Rocha FC',
        'founded': 1999,
        'city': 'Rocha, Uruguay',
        },


    {
        'name': 'São Caetano',
        'founded': datetime.datetime(1989, 12, 4),
        'city': 'Sao Caetano, Brazil',
        },


    {
        'name': 'Universidad César Vallejo',
        'founded': datetime.datetime(1996, 1, 6),
        'city': 'Trujillo, Peru',
        },

    {
        'name': 'Avaí FC',
        'founded': datetime.datetime(1923, 9, 1),
        'city': 'Florianopolis, Brazil',
        },

    {
        'name': 'Cucuta Deportivo',
        'founded': datetime.datetime(1924, 9, 10),
        'city': 'Cucuta, Colombia',
        },

    {
        'name': 'Zamora FC',
        'founded': 1977,
        'city': 'Barinas, Venezuela',
        },
    {
        'name': 'Ñublense',
        'founded': datetime.datetime(1916, 8, 20),
        'city': 'Chillán, Chile',
        },

    {
        'name': 'León de Huánuco',
        'founded': datetime.datetime(1946, 6, 29),
        'city': 'Huanuco, Peru',
        },

    {
        'name': 'La Paz FC',
        'founded': datetime.datetime(1989, 5, 30),
        'city': 'La Paz, Bolivia',
        },

    {
        'name': 'Atlético Bucaramanga',
        'founded': 1949,
        'city': 'Bucaramanga, Colombia',
        },
    {
        'name': 'CA Colón',
        'founded': datetime.datetime(1905, 5, 5),
        'city': 'Santa Fe, Argentina',
        },
    {
        'name': 'Estudiantes de Mérida',
        'founded': datetime.datetime(1971, 4, 4),
        'city': 'Merida, Venezuela',
        },
    {
        'name': 'Atlético Paranaense',
        'founded': datetime.datetime(1924, 5, 26),
        'city': 'Curitiba, Brazil',
        },

    {
        'name': 'La Equidad',
        'founded': datetime.datetime(1990, 10, 12),
        'city': 'Bogota, Colombia',
        },

    {
        'name': 'Sport Áncash',
        'founded': datetime.datetime(1967, 4, 22),
        'city': 'Huaraz, Peru',
        },
    {
        'name': 'Club Universitario',
        'founded': datetime.datetime(1962, 4, 5),
        'city': 'Sucre, Bolivia',
        },
    {
        'name': 'Tacuary',
        'founded': 1923,
        'city': 'Asuncion, Paraguay',
        },

    {
        'name': 'Mineros de Guayana',
        'founded': 1981,
        'city': 'Puerto Ordaz, Venezuela',
        },
    {
        'name': 'Olmedo',
        'founded': datetime.datetime(1919, 11, 11),
        'city': 'Riobamba, Ecuador',
        },
    {
        'name': 'Deportes Concepción',
        'founded': datetime.datetime(1966, 2, 28), # 2, 29),
        'city': 'Concepcion, Chile',
        },

    {
        'name': 'Atlético Torino',
        'founded': 1946, 
        'city': 'Talara, Peru',
        },
    {
        'name': 'Cobresal',
        'founded': datetime.datetime(1979, 5, 5),
        'city': 'El Salvador, Chile',
        },
    {
        'name': 'Náutico',
        'founded': datetime.datetime(1901, 4, 7),
        'city': 'Recife, Brazil',
        },
    {
        'name': 'Deportivo Municipal',
        'founded': datetime.datetime(1935, 7, 27),
        'city': 'Lima, Peru',
        },
    {
        'name': 'Sport Huancayo',
        'founded': datetime.datetime(2007, 2, 7),
        'city': 'Huancayo, Peru',
        },
    {
        'name': 'Real Potosí',
        'founded': 1941,
        'city': 'Potosi, Bolivia',
        },
    {
        'name': 'Monagas SC',
        'founded': datetime.datetime(1987, 9, 23),
        'city': 'Maturin, Venezuela',
        },
    {
        'name': 'AC Minervén FC',
        'founded': 1985,
        'city': 'Puerto Ordaz, Venezuela',
        },

    {
        'name': 'Club Sport Marítimo de Venezuela',
        'founded': 1959,
        'city': 'Caracas, Venezuela',
        },

    {
        'name': 'SC Recife',
        'founded': datetime.datetime(1905, 5, 13),
        'city': 'Recife, Brazil',
        },
    {
        'name': 'Club Bolívar',
        'founded': datetime.datetime(1925, 4, 12),
        'city': 'La Paz, Bolivia',
        },
    {
        'name': 'Defensor SC',
        'founded': datetime.datetime(1913, 3, 15),
        'city': 'Montevideo, Uruguay',
        },
    {
        'name': 'Independiente Medellín',
        'founded': datetime.datetime(1913, 11, 14),
        'city': 'Medellin, Colombia',
        },

    {
        'name': 'Club Always Ready',
        'founded': datetime.datetime(1933, 4, 13),
        'city': 'La Paz, Bolivia',
        },

    {
        'name': 'Defensor Arica',
        'founded': 1929,
        'city': 'Lima, Peru',
        },

    {
        'name': 'C.S.D. Rangers',
        'founded': datetime.datetime(1902, 9, 2),
        'city': 'Talca, Chile',
        },

    {
        'name': 'Chaco Petrolero',
        'founded': 1944,
        'city': 'La Paz, Bolivia',
        },

    {
        'name': 'Alfonso Ugarte',
        'founded': datetime.datetime(1917, 8, 1),
        'city': 'Trujillo, Peru',
        },

    {
        'name': 'Deportivo Cuenca',
        'founded': datetime.datetime(1971, 3, 4),
        'city': 'Cuenca, Ecuador',
        },

    {
        'name': 'Danubio F.C.',
        'founded': datetime.datetime(1932, 3, 1),
        'city': 'Montevideo, Uruguay',
        },

    {
        'name': 'Gimnasia y Esgrima',
        'founded': datetime.datetime(1887, 6, 3),
        'city': 'La Plata, Argentina',
        },

    {
        'name': 'Alianza Atlético',
        'founded': 1920,
        'city': 'Sullana, Peru',
        },

    {
        'name': 'Goiás EC',
        'founded': datetime.datetime(1943, 4, 6),
        'city': 'Goiania, Brazil',
        },

    {
        'name': 'Paraná Clube',
        'founded': datetime.datetime(1989, 12, 19),
        'city': 'Curitiba, Brazil',
        },

    {
        'name': 'CD Everest',
        'founded': datetime.datetime(1931, 2, 2),
        'city': 'Guayaquil, Ecuador'
        },

    {
        'name': 'Everton de Viña del Mar',
        'founded': datetime.datetime(1909, 6, 24),
        'city': 'Vina del Mar, Chile',
        },

    {
        'name': 'O\'Higgins F.C.',
        'founded': datetime.datetime(1955, 4, 7),
        'city': 'Rancagua, Chile',
        },

    {
        'name': 'Atlético Chalaco',
        'founded': datetime.datetime(1899, 6, 9),
        'city': 'Callao, Peru',
        },

    {
        'name': 'Cobreloa',
        'founded': 1977,
        'city': 'Calama, Chile',
        },

    {
        'name': 'Mariano Melgar',
        'founded': datetime.datetime(1915, 3, 25),
        'city': 'Arequipa, Peru',
        },

    {
        'name': 'Ferro Carril Oeste',
        'founded': datetime.datetime(1904, 7, 28),
        'city': 'Buenos Aires, Argentina',
        },

    {
        'name': 'Aragua FC',
        'founded': datetime.datetime(2002, 8, 20),
        'city': 'Maracay, Venezuela',
        },

    {
        'name': 'Boyacá Chicó',
        'founded': datetime.datetime(2002, 3, 26),
        'city': 'Tunja, Colombia',
        },
    {
        'name': 'CD Palestino',
        'founded': datetime.datetime(1920, 8, 20),
        'city': 'Santiago, Chile',
        },

    {
        'name': 'National Fast Clube',
        'founded': 1930,
        'city': 'Manaus, Brazil',
        },
    {
        'name': 'Deportivo Anzoátegui',
        'founded': datetime.datetime(2002, 11, 9),
        'city': 'Puerto La Cruz, Venezuela',
        },
    {
        'name': 'Liverpool FC (Montevideo)',
        'founded': datetime.datetime(1915, 2, 12),
        'city': 'Montevideo, Uruguay',
        },

    {
        'name': 'Racing Club de Montevideo',
        'founded': datetime.datetime(1919, 4, 6),
        'city': 'Montevideo, Uruguay',
        },

    {
        'name': 'Atlético Huila',
        'founded': 1990,
        'city': 'Neiva, Colombia',
        },

    {
        'name': 'Argentinos Juniors',
        'founded': datetime.datetime(1904, 8, 15),
        'city': 'Buenos Aires, Argentina',
        },

    {
        'name': 'Arsenal de Sarandí',
        'founded': datetime.datetime(1957, 1, 11),
        'city': 'Avellaneda Partido, Argentina',
        },

    {
        'name': 'Atlético Nacional',
        'founded': 1947,
        'city': 'Medellin, Colombia',
        },

    {
        'name': 'Cienciano',
        'founded': datetime.datetime(1901, 7, 8),
        'city': 'Cuzco, Peru',
        },

    {
        'name': 'Internacional',
        'founded': datetime.datetime(1909, 4, 4),
        'city': 'Porto Alegre, Brazil',
        },

    {
        'name': 'Club Litoral',
        'founded': 1936,
        'city': 'Cochabamba, Bolivia',
        },

    {
        'name': 'Club Olimpia',
        'founded': datetime.datetime(1902, 7, 25),
        'city': 'Asuncion, Paraguay',
        },
    {
        'name': 'Estudiantes de La Plata',
        'founded': datetime.datetime(1905, 8, 4),
        'city': 'La Plata, Argentina',
        },
    {
        'name': 'Gremio',
        'founded': datetime.datetime(1903, 9, 15),
        'city': 'Porto Alegre, Brazil',
        },
    {
        'name': 'LDU Quito',
        'founded': datetime.datetime(1930, 1, 11),
        'city': 'Quito, Ecuador',
        },
    {
        'name': 'CD El Nacional',
        'founded': datetime.datetime(1964, 6, 1),
        'city': 'Quito, Ecuador',
        },

    {
        'name': 'América de Quito',
        'founded': datetime.datetime(1939, 11, 25),
        'city': 'Quito, Ecuador',
        },
    {
        'name': 'Deportiva Canarias',
        'founded': 1963,
        'city': 'Caracas, Venezuela',
        },
    {
        'name': 'Once Caldas',
        'founded': datetime.datetime(1959, 3, 17),
        'city': 'Manizales, Colombia',
        },
    {
        'name': 'River Plate',
        'founded': datetime.datetime(1901, 5, 25),
        'city': 'Buenos Aires, Argentina',
        },
    {
        'name': 'Sao Paulo FC',
        'founded': datetime.datetime(1935, 12, 16),
        'city': 'Sao Paulo, Brazil',
        },
    {
        'name': 'Universidad de Chile',
        'founded': datetime.datetime(1927, 5, 24),
        'city': 'Santiago, Chile',
        },
    {
        'name': 'Velez Sarsfield',
        'founded': datetime.datetime(1910, 1, 1),
        'city': 'Buenos Aires, Argentina',
        },
    {
        'name': 'The Strongest',
        'founded': datetime.datetime(1908, 4, 8),
        'city': 'La Paz, Bolivia',
        },
    {
        'name': 'Caracas FC',
        'founded': 1967,
        'city': 'Caracas, Venezuela',
        },
    {
        'name': 'Talleres de Córdoba',
        'founded': datetime.datetime(1913, 10, 12),
        'city': 'Cordoba, Argentina',
        },


    {
        'name': 'Universidad Catolica',
        'founded': datetime.datetime(1937, 4, 21),
        'city': 'Santiago, Chile',
        },

    {
        'name': 'Tiro Federal',
        'founded': datetime.datetime(1905, 3, 29),
        'city': 'Rosario, Argentina',
        },

    {
        'name': 'Club Tijuana',
        'founded': datetime.datetime(2007, 1, 10),
        'city': 'Tijuana, Mexico',
        },

    {
        'name': 'Emelec',
        'founded': datetime.datetime(1929, 4, 28),
        'city': 'Guayaquil, Ecuador',
        },

    {
        'name': 'Guabirá',
        'founded':1962,
        'city': 'Montero, Bolivia',
        },
    {
        'name': 'Independiente Santa Fe',
        'founded': datetime.datetime(1941, 2, 28),
        'city': 'Bogota, Colombia',
        },
    # Mineros?
    #{
    #    'name': 'Atletico Mineiro',
    #    'founded': datetime.datetime(1908, 3, 25),
    #    'city': 'Santa Cruz, Bolivia',
    #    },
    {
        'name': 'Rosario Central',
        'founded': datetime.datetime(1889, 12, 24),
        'city': 'Rosario, Argentina',
        },
    {
        'name': 'SD Aucas',
        'founded': datetime.datetime(1945, 2, 6),
        'city': 'Quito, Ecuador',
        },
    {
        'name': 'Blooming',
        'founded': datetime.datetime(1946, 5, 1),
        'city': 'Santa Cruz, Bolivia',
        },
    {
        'name': 'Newell\'s Old Boys',
        'founded': datetime.datetime(1903, 11, 3),
        'city': 'Rosario, Argentina',
        },
    {
        'name': 'Huracan',
        'founded': datetime.datetime(1908, 11, 11),
        'city': 'Buenos Aires, Argentina',
        },
    {
        'name': 'Rampla Juniors',
        'founded': datetime.datetime(1914, 1, 7),
        'city': 'Montevideo, Uruguay',
        },
    {
        'name': 'Central Cordoba',
        'founded': datetime.datetime(1906, 10, 20),
        'city': 'Rosario, Argentina',
        },
    {
        'name': 'Godoy Cruz',
        'founded': datetime.datetime(1921, 6, 21),
        'city': 'Godoy Cruz, Argentina',
        },
    {
        'name': 'Club Aurora',
        'founded': datetime.datetime(1935, 5, 27),
        'city': 'Cochabamba, Bolivia',
        },
    {
        'name': 'Cerro Largo',
        'founded': datetime.datetime(2002, 11, 19),
        'city': 'Melo, Uruguay',
        },

    {
        'name': 'Cerro',
        'founded': datetime.datetime(1922, 12, 1),
        'city': 'Montevideo, Uruguay',
        },

    {
        'name': 'U.T. Cajamarca',
        'founded': datetime.datetime(1964, 7, 14),
        'city': 'Cajamarca, Peru',
        },

    {
        'name': 'Deportivo Táchira',
        'founded': datetime.datetime(1974, 1, 11),
        'city': 'San Cristobal, Venezuela',
        },
    {
        'name': 'Banfield',
        'founded': datetime.datetime(1896, 1, 21),
        'city': 'Buenos Aires, Argentina',
        },
    {
        'name': 'Quilmes',
        'founded': datetime.datetime(1897, 11, 27),
        'city': 'Buenos Aires, Argentina',
        },
    {
        'name': 'Junior de Barranquilla',
        'founded': 1924,
        'city': 'Barranquilla, Colombia',
        },
    {
        'name': 'Huachipato',
        'founded': datetime.datetime(1947, 6, 7),
        'city': 'Talcahuano, Chile',
        },
    {
        'name': 'Universidad de Los Andes',
        'founded': 1977,
        'city': 'Merida, Venezuela',
        },
    {
        'name': 'Trujillanos FC',
        'founded': 1981, 
        'city': 'Valera, Venezuela',
        },

    {
        'name': 'Valdez SC',
        'founded': datetime.datetime(1991, 1, 21),
        'dissolved': datetime.datetime(1997, 8, 20),
        'city': 'Milagro, Ecuador',
        },
    {
        'name': 'Lanus',
        'founded': datetime.datetime(1915, 1, 3),
        'city': 'Lanus, Argentina',
        },
    {
        'name': 'Audax Italiano',
        'founded': datetime.datetime(1910, 11, 30),
        'city': 'La Florida, Chile',
        },
    {
        'name': 'Jorge Wilstermann',
        'founded': datetime.datetime(1949, 11, 24),
        'city': 'Cochabama, Bolivia',
        },
    {
        'name': 'LDU Loja',
        'founded': datetime.datetime(1987, 10, 23),
        'city': 'Loja, Ecuador',
        },
    {
        'name': 'Real Garcilaso',
        'founded': datetime.datetime(2009, 7, 28),
        'city': 'Cuzco, Peru',
        },
    {
        'name': 'Deportivo Lara',
        'founded': 2006,
        'city': 'Barquisimeto, Venezuela',
        },
    {
        'name': 'Inti Gas',
        'founded': 1972,
        'city': 'Ayacucho, Peru',
        },
    {
        'name': 'River Plate (Montevideo)',
        'founded': datetime.datetime(1932, 5, 11),
        'city': 'Montevideo, Uruguay',
        },
    {
        'name': 'Deportivo Quito',
        'founded': datetime.datetime(1955, 2, 27),
        'city': 'Quito, Ecuador',
        },
    {
        'name': 'Tigre',
        'founded': datetime.datetime(1902, 8, 3),
        'city': 'Buenos Airse, Argentina',
        },
    {
        'name': 'Club Destroyers',
        'founded': datetime.datetime(1948, 9, 14),
        'city': 'Santa Cruz, Bolivia',
        },


    {
        'name': 'Oriente Petrolero',
        'founded': datetime.datetime(1955, 11, 5),
        'city': 'Santa Cruz, Bolivia',
        },

    # Venezuela

    {
        'name': 'Deportivo Petare',
        'founded': datetime.datetime(1948, 8, 18),
        'city': 'Caracas, Venezuela',
        },

    # Colombia

    {
        'name': 'America de Cali',
        'founded': datetime.datetime(1918, 12, 21),
        'city': 'Santiago de Cali, Colombia',
        },

    {
        'name': 'Santo André',
        'founded': datetime.datetime(1967, 9, 18),
        'city': 'Santo Andre, Brazil',
        },

    {
        'name': 'Deportivo Cali',
        'founded': 1912,
        'city': 'Santiago de Cali, Colombia',
        },

    {
        'name': 'Millonarios',
        'founded': datetime.datetime(1946, 6, 18),
        'city': 'Bogota, Colombia',
        },

    {
        'name': 'Barcelona Sporting Club',
        'founded': datetime.datetime(1925, 5, 1),
        'city': 'Guayaquil, Ecuador',
        },

    # Peru

    {
        'name': 'Alianza Lima',
        'founded': datetime.datetime(1901, 2, 15),
        'city': 'Lima, Peru',
        },

    {
        'name': 'Sporting Cristal',
        'founded': datetime.datetime(1955, 12, 13),
        'city': 'Lima, Peru',
        },

    # Paraguay

    {
    'name': 'Cerro Porteño',
    'founded': datetime.datetime(1912, 10, 1),
    'city': 'Asuncion, Paraguay',
    },




    # Chile

    {
        'name': 'Colo-Colo',
        'founded': datetime.datetime(1925, 4, 19),
        'city': 'Santiago, Chile',
        },



    {
        'name': 'Unión Magdalena',
        'founded': datetime.datetime(1950, 4, 19),
        'city': 'Santa Marta, Colombia',
        },

    {
        'name': 'Unión Huaral',
        'founded': 1947,
        'city': 'Huaral, Peru',
        },

    {
        'name': 'Filanbanco',
        'founded': datetime.datetime(1979, 1, 29),
        'dissolved': datetime.datetime(1991, 1, 21),
        'city': 'Guayaquil, Ecuador',
        },

    {
        'name': 'Pepeganga',
        'founded': 1985,
        'city': 'Porlamar, Venezuela',
        },

    {
        'name': 'Magallanes',
        'founded': datetime.datetime(1897, 10, 27),
        'city': 'Santiago, Chile',
        },

    {
        'name': 'Club Universidad de Chile',
        'founded': datetime.datetime(1927, 5, 24),
        'city': 'Santiago, Chile',
        },

    {
        'name': 'Universitario',
        'founded': datetime.datetime(1924, 8, 7),
        'city': 'Lima, Peru',
        },



    {
        'name': 'Union San Felipe',
        'founded': datetime.datetime(1956, 10, 16),
        'city': 'San Felipe, Chile',
        },


    # Uruguay

    {
        'name': 'Club Nacional de Football',
        'founded': datetime.datetime(1899, 5, 14),
        'city': 'Montevideo, Uruguay',
        },

    {
        'name': 'Peñarol',
        'founded': datetime.datetime(1891, 9, 28),
        'city': 'Montevideo, Uruguay',
        },

    # Argentina

    {
        'name': 'Belgrano',
        'founded': datetime.datetime(1905, 3, 19),
        'city': 'Cordoba, Argentina',
        },

    {
        'name': 'Deportivo Moron',
        'founded': datetime.datetime(1947, 6, 20),
        'city': 'Buenos Aires, Argentina',
        },

    {
        'name': 'CA Independiente',
        'founded': datetime.datetime(1905, 1, 1),
        'city': 'Buenos Aires, Argentina',
        },

    {
        'name': 'Boca Juniors',
        'founded': datetime.datetime(1905, 4, 3),
        'city': 'Buenos Aires, Argentina',
        },

    {
        'name': 'EC Juventude',
        'founded': datetime.datetime(1913, 6, 29),
        'city': 'Caxias do Sul, Brazil',
        },

    {
        'name': 'Racing Club de Avellaneda',
        'founded': datetime.datetime(1903, 3, 25),
        'city': 'Buenos Aires, Argentina',
        },

    {
        'name': 'Sacachispas',
        'founded': datetime.datetime(1948, 10, 17),
        'city': 'Buenos Aires, Argentina',
        },

    {
        'name': 'San Lorenzo',
        'founded': datetime.datetime(1908, 4, 1),
        'city': 'Buenos Aires, Argentina',
        },

    # Brazil

    {
        'name': 'America Rio',
        'founded': datetime.datetime(1904, 9, 18),
        'city': 'Rio de Janerio, Brazil',
        },

    {
        'name': 'Bangu',
        'founded': datetime.datetime(1904, 4, 17),
        'city': 'Rio de Janerio, Brazil',
        },

    {
        'name': 'Bonsucesso FC',
        'founded': datetime.datetime(1913, 8, 12),
        'city': 'Rio de Janerio, Brazil',
        },

    {
        'name': 'Cruzeiro',
        'founded': 1921,
        'city': 'Belo Horizonte, Brazil',
        },
    {
        'name': 'Atlético Mineiro',
        'founded': datetime.datetime(1908, 3, 25),
        'city': 'Belo Horizonte, Brazil',
        },

    {
        'name': 'Provincial Osorno',
        'founded': 1983,
        'city': 'Osorno, Chile',
        },

    {
        'name': 'CA Progreso',
        'founded': datetime.datetime(1917, 4, 30),
        'city': 'Montevideo, Uruguay',
        },

    {
        'name': 'ESPOLI',
        'founded': datetime.datetime(1986, 2, 5),
        'city': 'Quito, Ecuador',
        },
    {
        'name': 'UA Maracaibo',
        'founded': datetime.datetime(2001, 1, 16),
        'city': 'Maracaibo, Venezuela',
        },

    {
        'name': 'Grêmio Barueri',
        'founded': datetime.datetime(1989, 3, 26),
        'city': 'Barueri, Brazil',
        },
    {
        'name': 'Unión Comercio',
        'founded': datetime.datetime(1994, 6, 15),
        'city': 'Nueva Cajamarca, Peru',
        },

    {
        'name': 'Envigado',
        'founded': datetime.datetime(1989, 10, 14),
        'city': 'Medellin, Colombia',
        },

    {
        'name': 'Deportes Iquique',
        'founded': datetime.datetime(1978, 5, 21),
        'city': 'Iquique, Chile',
        },
    {
        'name': 'Atlético Goianiense',
        'founded': datetime.datetime(1937, 4, 2),
        'city': 'Goiania, Brazil',
        },
    {
        'name': 'Coritiba FC',
        'founded': datetime.datetime(1909, 10, 12),
        'city': 'Curitiba, Brazil',
        },

    {
        'name': 'Universidad de Concepción',
        'founded': datetime.datetime(1994, 8, 8),
        'city': 'Concepcion, Chile',
        },


    {
        'name': 'Central Español',
        'founded': datetime.datetime(1905, 1, 5),
        'city': 'Montevideo, Uruguay',
        },
    {
        'name': 'Carabobo FC',
        'founded': datetime.datetime(1964, 7, 24),
        'city': 'Valencia, Venezuela',
        },
    {
        'name': 'Coronel Bolognesi',
        'founded': 1998,
        'city': 'Tacna, Peru',
        },

    {
        'name': 'Flamengo',
        'founded': datetime.datetime(1895, 11, 17),
        'city': 'Rio de Janerio, Brazil',
        },
    {
        'name': 'Figueirense',
        'founded': datetime.datetime(1921, 6, 12),
        'city': 'Florianopolis, Brazil',
        },

    {
        'name': 'Fluminense',
        'founded': datetime.datetime(1902, 7, 21),
        'city': 'Rio de Janerio, Brazil',
        },

    {
        'name': 'Bonsucesso',
        'founded': datetime.datetime(1913, 8, 12),
        'city': 'Rio de Janerio, Brazil',
        },

    {
        'name': 'Botafogo',
        'founded': datetime.datetime(1894, 7, 1),
        'city': 'Rio de Janerio, Brazil',
        },

    {
        'name': 'Palmeiras',
        'founded': datetime.datetime(1914, 8, 26),
        'city': 'Sao Paulo, Brazil',
        },

    {
        'name': 'Santos FC',
        'founded': datetime.datetime(1912, 4, 14),
        'city': 'Sao Paulo, Brazil',
        },

    {
        'name': 'Universidad San Martín',
        'founded': 2004,
        'city': 'Lima, Peru',
        },

    {
        'name': 'Penarol',
        'founded': datetime.datetime(1891, 9, 28),
        'city': 'Montevideo, Uruguay',
        },

    {
        'name': 'Club Libertad',
        'founded': 1905,
        'city': 'Asuncion, Paraguay',
        },

    {
        'name': 'Uberlandia',
        'founded': 1922,
        'city': 'Uberlândia, Brazil',
        },

    {
        'name': 'Club Guaraní',
        'founded': 1903,
        'city': 'Asuncion, Paraguay',
        },

    {
        'name': '12 de Octubre',
        'founded': datetime.datetime(1914, 8, 14),
        'city': 'Itaugua, Paraguay',
        },

    {
        'name': '31 de Octubre',
        'founded': 1954,
        'city': 'La Paz, Bolivia',
        },

    {
        'name': 'Sport Boys',
        'founded': datetime.datetime(1927, 7, 27),
        'city': 'Callao, Peru',
        },

    {
        'name': 'CR Vasco da Gama',
        'founded': datetime.datetime(1898, 8, 21),
        'city': 'Rio de Janerio, Brazil',
        },
    {
        'name': 'Montevideo Wanderers',
        'founded': datetime.datetime(1902, 8, 15),
        'city': 'Montevideo, Uruguay',
        },
    {
        'name': 'Santiago Wanderers',
        'founded': datetime.datetime(1892, 8, 15),
        'city': 'Santiago, Chile',
        },
    {
        'name': 'CD Olmedo',
        'founded': datetime.datetime(1919, 11, 11),
        'city': 'Riobamba, Ecuador',
        },
    {
        'name': 'Paysandu SC',
        'founded': datetime.datetime(1914, 2, 2),
        'city': 'Belem, Brazil',
        },
    {
        'name': 'Deportes Tolima',
        'founded': 1954,
        'city': 'Ibague, Colombia',
        },
    {
        'name': 'Deportivo Pasto',
        'founded': 1949,
        'city': 'Pasto, Colombia',
        },

]
