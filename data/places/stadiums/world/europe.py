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
        'name': 'Kazimierza Gorskiego Stadium', 
        'location': 'Plock, Poland',
        },

    {
        'name': 'Stade du Fort Carré',
        'location': 'Antibes, France',
        'capacity': 7000,
        },

    {
        'name': 'Råsunda Stadium',
        'location': 'Solna, Stockholm, Sweden',
        'capacity': 36608,
        'opened': datetime.datetime(1937, 5, 17),
        },

    {
        'name': 'Arosvallen',
        'location': 'Västerås, Sweden',
        },

    {
        'name': 'Idrottsparken',
        'location': 'Norrköping, Sweden',
        'opened': 1904,
        'capacity': 16700,
        },

    {
        'name': 'Jernvallen',
        'location': 'Sandviken, Sweden',
        'opened': 1938,
        'capacity': 7000,
        },

    {
        'name': 'Rimnersvallen',
        'location': 'Uddevalla, Sweden',
        'opened': datetime.datetime(1923, 5, 5),
        'capacity': 10605,
        },

    {
        'name': 'Ullevi',
        'location': 'Gothenburg, Sweden',
        'opened': datetime.datetime(1958, 5, 29),
        'capacity': 43000,
        },

    {
        'name': 'Olympiastadion',
        'location': 'Munich, Germany',
        'opened': datetime.datetime(1972, 5, 26),
        'capacity': 69250,
        'architect': 'Frei Otto',
        },

    {
        'name': 'Parkstadion',
        'location': 'Gelsenkirchen, Germany',
        'opened': datetime.datetime(1973, 8, 4),
        'closed': 2008,
        'capacity': 62008,
        },

    {
        'name': 'Stade Victor Boucquey',
        'location': 'Lille, France',
        'opened': 1902,
        'capacity': 15000,
        },

    {
        'name': 'AWD-Arena',
        'location': 'Hanover, Germany',
        'opened': datetime.datetime(1954, 9, 26),
        'capacity': 49000,
        },

    {
        'name': 'Mercedes-Benz Arena',
        'location': 'Stuttgart, Germany',
        'opened': datetime.datetime(1933, 7, 23),
        'capacity': 60441,
        },

    {
        'name': 'Volksparkstadion',
        'location': 'Hamburg, Germany',
        'opened': datetime.datetime(1953, 7, 12),
        'capacity': 57000,
        },

    {
        'name': 'Camp Nou',
        'location': 'Barcelona, Spain',
        'opened': datetime.datetime(1957, 9, 24),
        'capacity': 99354,
        },

    {
        'name': 'Estadio Santiago Bernabéu',
        'location': 'Madrid, Spain',
        'opened': datetime.datetime(1944, 10, 27),
        'capacity': 85454,
        },


    {
        'name': 'Estadio Vicente Calderón',
        'location': 'Madrid, Spain',
        'opened': datetime.datetime(1966, 10, 2),
        'capacity': 54960,
        },

    {
        'name': 'Estadio José Rico Pérez',
        'location': 'Alicante, Spain',
        'opened': 1974,
        'capacity': 30000,
        },

    {
        'name': 'El Molinon',
        'location': 'Gijón, Spain',
        'opened': 1908,
        'capacity': 30000,
        },

    {
        'name': 'Estadio Riazor',
        'location': 'A Coruña, Spain',
        'opened': datetime.datetime(1944, 10, 28),
        'capacity': 34600,
        },

    {
        'name': 'Estadio La Rosaleda',
        'location': 'Málaga, Spain',
        'opened': datetime.datetime(1941, 9, 15),
        'capacity': 28963,
        },

    {
        'name': 'La Romareda',
        'location': 'Zaragoza, Spain',
        'opened': datetime.datetime(1957, 9, 8),
        'capacity': 34596,
        },

    {
        'name': 'Stade de la Mosson',
        'location': 'Montpellier, France',
        'opened': datetime.datetime(1927, 1, 13),
        'capacity': 32900,
        },

    {
        'name': 'Stade de la Meinau',
        'location': 'Strasbourg, France',
        'address': '12, rue de l\'Extenwoerth',
        'opened': 1914,
        'capacity': 29320,
        },

    {
        'name': 'Stade de la Cavée verte',
        'location': 'Le Havre, France',
        'address': 'Rue de la Cavée Verte',
        'opened': 1918,
        'closed': 1970,
        'capacity': 22000
        },

    

    
    {
        'name': 'Stadion Galgenwaard',
        'location': 'Utrecht, Netherlands',
        'opened': datetime.datetime(2004, 8, 22),
        'capacity': 24426,
        },

    {
        'name': 'Parkstad Limburg Stadion',
        'location': 'Kerkrade, Netherlands',
        'opened': datetime.datetime(2000, 8, 15),
        'capacity': 19979,
        },

    {
        'name': 'De Vijverberg',
        'location': 'De Graafschap, Netherlands',
        'capacity': 12600,
        },


    {
        'name': 'Koning Willem II Stadion',
        'location': 'Tilburg, Netherlands',
        'capacity': 14637,
        'opened': 1995,
        },


    {
        'name': 'Stade Chaban-Delmas',
        'location': 'Bordeaux, France',
        'opened': datetime.datetime(1938, 6, 12),
        'capacity': 34694,
        },

    {
        'name': 'Dalymount Park',
        'location': 'Dublin, Ireland',
        'opened': datetime.datetime(1901, 9, 7),
        'capacity': 4300,

        },

    {
        'name': 'Ayresome Park',
        'opened': 1903,
        'closed': 1995,
        'capacity': 26667,
        'location': 'Middlesbrough, England',
        },

    {
        'name': 'Stade de Gerland',
        'address': '353, Avenue Jean-Jaurès, 69007',
        'location': 'Lyons, France',
        'opened': 1926,
        'capacity': 40500,
        
        },

    {
        'name': 'Stade de la Beaujoire', 
        'location': 'Nante, France',
        'address': 'Route de Saint Joseph 44300',
        'opened': datetime.datetime(1984, 5, 8),
        'capacity': 38285,
        },

    {
        'name': 'Parc des Princes',
        'location': 'Paris, France',
        'opened': datetime.datetime(1897, 7, 18),
        'capacity': 48712,

        },
    {
        'name': 'Ernst-Happel Stadion',
        'location': 'Vienna, Austria',
        },

    {
        'name': 'Stade Roi Baudouin',
        'location': 'Brussels, Belgium',
        },


    {
        'name': 'Stadio Cibali',
        'location': 'Catania, Italy',
        },
    {
        'name': 'Osteestadion',
        'location': 'Rostock, Germany',
        },

    {
        'name': 'Stade la Beaujoire',
        'location': 'Nantes, France',
        },

    {
        'name': 'Geoffrey Prichard Stadium',
        'location': 'St. Etienne, France',
        },

    {
        'name': 'Dinamo Stadium', 
        'location': 'Moscow, Russia',
        'opened': 1928,
        'closed': 2008,
        'capacity': 36540,
        },


    {
        'name': 'EasyCredit-Stadion', 
        'location': 'Nuremberg, Germany',
        },
    {
        'name': 'Fritz Walter Stadion', 
        'location': 'Kaiserslautern, Germany',
        },

    {
        'name': 'Veltins-Arena', 

        'location': 'Gelsenkirchen, Germany',
        'opened': 2001,
        'cost': 191000000,
        'denomination': 'Euro',
        'architect': 'Hentrich, Petschnigg, und Partner',
        'capacity': 61673,
        },

    {
        'name': 'Ullevaal Stadium', 
        'location': 'Oslo, Norway',
        },
    

    {
        'name': 'Laugardalsvollur', 
        'location': 'Reykjavik, Iceland',
        },
    {
        'name': 'Melavollur', 
        'location': 'Reykjavik, Iceland',
        },

    {
        'name': 'Inonu Stadium',
        'location': 'Istanbul, Turkey',
        'opened': datetime.datetime(1947, 5, 19),
        'architect': 'Paolo Vietti-Violi',
        'capacity': 32145,
        },

    {
        'name': 'Polish Army Stadium',
        'location': 'Warsaw, Poland',
        },
    {
        'name': 'Nepstadion',
        'location': 'Budapest, Hungary',
        'opened': 1953,
        'capacity': 39111,
        },

    {
        'name': 'LKS Stadium',
        'location': 'Lodz, Poland',
        },

    {
        'name': 'Stadio Comunale',
        'location': 'Florence, Italy',
        },

    {
        'name': 'Stadio San Nicola',
        'location': 'Bari, Italy',
        'opened': 1990,
        'capacity': 58270,
        
        },

    {
        'name': 'Stade Vélodrome',
        'location': 'Marseilles, France',
        'opened': 1937,
        'capacity': 42000,
        
        },
    {
        'name': 'Stadio Olimpico',
        'location': 'Rome, Italy',
        'opened': 1937,
        'capacity': 70634,
        },

    {
        'name': 'Stadio delle Alpi',
        'location': 'Turin, Italy',
        'opened': 1990,
        'closed': 2006,
        'capacity': 69000,
        },

    {
        'name': 'Stadio Olimpico di Torino',
        'location': 'Turin, Italy',
        'opened': datetime.datetime(1933, 5, 14),
        'capacity': 28140,
        },

    {
        'name': 'Stadio Giorgio Ascarelli',
        'location': 'Naples, Italy',
        'capacity': 40000,
        },


    {
        'name': 'Stadio Littorio',
        'location': 'Trieste, Italy',
        'opened': 1932,
        'closed': 1992,
        'capacity': 8000,
        },

    {
        'name': 'Stadio Renato Dall\'Ara',
        'location': 'Bologna, Italy',
        'opened': 1927,
        'capacity': 38279,
        },

    {
        'name': 'Rasunda Stadium',
        'location': 'Stockholm, Sweden',
        },
    {
        'name': 'Frogner Stadium',
        'location': 'Oslo, Norway',
        
        },

    {
        'name': 'Signal Iduna Park', 
        'location': 'Dortmund, Germany',
        },

    {
        'name': 'Fritz-Walter-Stadion', 
        'location': 'Kaiserslautern, Germany',
        },


    {
        'name': 'Landsdowne Road',
        'location': 'Dublin, Ireland',
        },


    {
        'name': 'Stadio Nazionale del PNF',
        'location': 'Rome, Italy',
        'opened': 1927,
        'closed': 1953,
        'capacity': 50000,
        },

    {
        'name': 'San Siro',
        'location': 'Milan, Italy',
        'opened': datetime.datetime(1926, 9, 19),
        'capacity': 80018,
        },

    {
        'name': 'Pershing Park',
        'location': 'Paris, France',
        },
    {
        'name': 'Agrykola Stadium',
        'location': 'Warsaw, Poland',
        },
    {
        'name': 'Warta Stadium',
        'location': 'Poznan, Poland',
        'opened': 1912,
        'capacity': 60000,
        
        },

    {
        'name': 'Griffin Park',
        'location': 'London, England',
        'opened': 1904,
        'capacity': 12763,
        },

    {
        'name': 'Hampden Park', 
        'location': 'Glasgow, Scotland',
        'opened': 1903,
        'capacity': 52063,
        },

    

    {
        'name': 'Stozice Stadium',
        'location': 'Ljubljana, Slovenia',
        },

    {
        'name': 'NRGi Park',
        'location': 'Aarhus, Denmark',
        'opened': datetime.datetime(1920, 6, 5),
        'capacity': 20032,
        },

    {
        'name': 'Tehelne Pole',
        'location': 'Bratislava, Slovakia',
        'opened': 1940,
        'closed': 2010,
        'capacity': 30085,
        },

    {
        'name': 'Amsterdam ArenA',
        'location': 'Amsterdam, Netherlands',
        'opened': datetime.datetime(1996, 8, 14),
        'cost': 140000000,
        'denomination': 'Euro',
        'capacity': 52342,
        },



    {
        'name': 'Estadio El Sardinero',
        'location': 'Santander, Spain',
        },

    {
        'name': 'Wembley Stadium',
        'location': 'London, England',
        'opened': 1923,
        'closed': 2000,
        'capacity': 82000,
        'cost': 750000,
        'denomination': 'British pounds',
        },


    {
        'name': 'Goodison Park',
        'location': 'Liverpool, England',
        'opened': datetime.datetime(1892, 8, 24),
        'capacity': 39571,
        'cost': 3000,
        'denomination': 'British pounds',
        },

    {
        'name': 'Hillsborough Stadium',
        'location': 'Sheffield, England',
        'opened': datetime.datetime(1899, 9, 2),
        'capacity': 39732
        },

    {
        'name': 'Roker Park',
        'location': 'Sunderland, England',
        'opened': 1897,
        'closed': 1998,
        'architect': 'Archibald Leitch',
        'capacity': 22500,
        },


    {
        'name': 'Villa Park',
        'location': 'Birmingham,England',
        'opened': 1897,
        'capacity': 42788,
        'cost': 16733,
        'denomination': 'British pounds',
        },



    {
        'name': 'Old Trafford',
        'location': 'Manchester,England',
        'opened': datetime.datetime(1910, 2, 19),
        'capacity': 75765,
        'cost': 90000,
        'denomination': 'British pounds',
        },

    {
        'name': 'White City Stadium',
        'location': 'London,England',
        'opened': 1908,
        'closed': 1984,
        'capacity': 93000,
        },

    {
        'name': 'Wisla Stadium',
        'location': 'Krakow, Poland',
        },

    {
        'name': 'Cornaredo Stadium',
        'location': 'Lugano, Switzerland',
        'opened': 1951,
        'capacity': 15900,
        },

    {
        'name': 'Wankdorf Stadium',
        'location': 'Bern, Switzerland',
        'opened': datetime.datetime(1925, 10, 18),
        'capacity': 64000,
        },


    {
        'name': 'Hardturm',
        'location': 'Zurich, Switzerland',
        'opened': 1929,
        'closed': datetime.datetime(2007, 9, 1),
        'capacity': 64000,
        },

    {
        'name': 'Stade Olympique de la Pontais',
        'location': 'Lausanne, Switzerland',
        'opened': 1904,
        'capacity': 15850,
        },

    {
        'name': 'Charmilles Stadium',
        'location': 'Geneve, Switzerland',
        'opened': 1930,
        'closed': 2002,
        'capacity': 9250,
        },

    {
        'name': 'St. Jakob-Park',
        'location': 'Basel, Switzerland',
        'opened': datetime.datetime(2001, 3, 15),
        'cost': 220000000,
        'denomination': 'Swiss franc',
        'architect': 'Herzog & de Meuron',
        },

    {
        'name': 'Ullevi Stadium',
        'location': 'Goteborg, Sweden',
        },



    {
        'name': 'Stade de France',
        'location': 'Paris, France',
        'opened': datetime.datetime(1998, 1, 28),
        'capacity': 81338,
        'cost': 290000000,
        'denomination': 'Euro',
        },

]
