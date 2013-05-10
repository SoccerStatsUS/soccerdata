#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [
    {
        'name': 'Manchester United',
        'founded': 1878,
        'city': 'Manchester, England',
        },


    {
        'name': 'Spartak Trnava',
        'founded': datetime.datetime(1923, 5, 30),
        'city': 'Trnava, Slovakia',
        },

    {
        'name': 'Austria Wien',
        'founded': datetime.datetime(1911, 3, 12),
        'city': 'Vienna, Austira',
        },


    {
        'name': 'Corinthian F.C.',
        'founded': 1882,
        'dissolved': 1939,
        'city': 'London, England',
        'next': 'Corinthian-Casuals F.C.',
        },
    {
        'name': 'Birmingham City F.C.',
        'founded': 1875,
        'city': 'Birmingham, England',
        },
    {
        'name': 'Eintracht Frankfurt',
        'founded': datetime.datetime(1899, 3, 8),
        'city': 'Frankfurt,Germany',
        },
    {
        'name': '1. FC Nuremberg',
        'founded': datetime.datetime(1900, 5, 4),
        'city': 'Nuremberg, Germany',
        },
    {
        'name': 'Itzehoer SV',
        'founded': datetime.datetime(1909, 10, 3),
        'city': 'Itzehoe, Germany',
        },
    {
        'name': 'Stuttgart Kickers',
        'founded': datetime.datetime(1899, 9, 21),
        'city': 'Stuttgart, Germany',
        },
    {
        'name': 'Sheffield United',
        'founded': datetime.datetime(1889, 3, 22),
        'city': 'Sheffield, England',
        },
    {
        'name': 'Newcastle United',
        'founded': datetime.datetime(1892, 12, 9),
        'city': 'Newcastle, England',
        },
    {
        'name': 'Fylkir',
        'founded': datetime.datetime(1967, 5, 28),
        'city': 'Reykjavik, Iceland',
        },
    {
        'name': 'Fulham F.C.',
        'founded': datetime.datetime(1879, 8, 16),
        'city': 'Fulham, England,'
        },
    {
        'name': 'GIF Sundsvall',
        'founded': datetime.datetime(1903, 8, 25),
        'city': 'Sundsvall, Sweden',
        },
    {
        'name': 'Viking FK',
        'founded': datetime.datetime(1899, 8, 10),
        'city': 'Stavanger, Norway',
        },
    {
        'name': 'Odd Grenland',
        'founded': datetime.datetime(1894, 3, 31),
        'city': 'Skien, Norway',
        },
    {
        'name': 'Stabæk Fotball',
        'founded': datetime.datetime(1912, 3, 16),
        'city': 'Baerum, Sweden',
        },
    {
        'name': 'FC Porto',
        'founded': datetime.datetime(1893, 9, 28),
        'city': 'Porto, Portugal',
        },

    {
        'name': 'FC Volendam',
        'founded': datetime.datetime(1977, 6, 1),
        'city': 'Volendam, Netherlands',
        },
    {
        'name': 'IFK Norrkoping',
        'founded': datetime.datetime(1897, 5, 29),
        'city': 'Norrkoping, Sweden',
        },

    # Same team?????
    {
        'name': 'Karlsruher SC',
        'founded': datetime.datetime(1894, 6, 6),
        'city': 'Karlsruhe, Germany',
        },
    {
        'name': 'Karlsruher FV',
        'founded': 1891,
        'city': 'Karlsruhe, Germany',
        },

    {
        'name': 'MTK Budapest',
        'founded': datetime.datetime(1888, 11, 16),
        'city': 'Budapest, Hungary',
        },
    {
        'name': 'Panathinaikos',
        'founded': datetime.datetime(1908, 2, 3),
        'city': 'Athens, Greece',
        },
    {
        'name': 'Polonia Bytom',
        'founded': datetime.datetime(1920, 1, 4),
        'city': 'Bytom, Poland',
        },
    {
        'name': 'SSV Reutlingen 05',
        'founded': datetime.datetime(1905, 5, 9),
        'city': 'Reutlingen, Germany',
        },
    {
        'name': 'Shamrock Rovers',
        'founded': 1901,
        'city': 'Dublin, Ireland',
        },
    {
        'name': 'Ipswich Town F.C.',
        'founded': 1878,
        'city': 'Ipswich, England',
        },

    {
        'name': 'Blackburn Rovers',
        'founded': 1875,
        'city': 'Blackburn, England',
        },

    {
        'name': 'Burnley FC',
        'founded': 1882,
        'city': 'Burnley, England',
        },


    {
        'name': 'Dinamo Zagreb',
        'founded': datetime.datetime(1945, 5, 9),
        'city': 'Zagreb, Croatia',
        },

    {
        'name': 'Dukla Prague',
        'founded': 1948,
        'dissolved': 1996,
        'city': 'Prague, Czech Republic',
        },

    {
        'name': 'Dynamo Bucharest',
        'founded': datetime.datetime(1948, 5, 14),
        'city': 'Bucharest, Romania',
        },

    {
        'name': 'FC Steaua București',
        'founded': datetime.datetime(1947, 6, 7),
        'city': 'Bucharest, Romania',
        },

    {
        'name': 'Everton',
        'founded': 1878,
        'city': 'Liverpool, England',
        },

    {
        'name': 'Fulham',
        'founded': datetime.datetime(1879, 8, 16),
        'city': 'London, England',
        },


    {
        'name': 'Preussen Munster',
        'founded': datetime.datetime(1906, 4, 30),
        'city': 'Munster, Germany',
        },

    {
        'name': 'Werder Bremen',
        'founded': datetime.datetime(1899, 2, 4),
        'city': 'Bremen, Germany',
        },


    {
        'name': 'VfL Wolfsburg',
        'founded': datetime.datetime(1945, 9, 12),
        'city': 'Wolfsburg, Germany',
        },


    {
        'name': 'Panionios',
        'founded': 1890,
        'city': 'Smyrna, Greece',
        },

    {
        'name': 'FC Locarno',
        'founded': 1906,
        'city': 'Locarno, Switzerland',
        },

    {
        'name': 'Norwich City F.C.',
        'founded': datetime.datetime(1902, 6, 17),
        'city': 'Norwich, England',
        },

    {
        'name': 'Walsall F.C.',
        'founded': 1888,
        'city': 'Walsall, England',
        },

    {
        'name': 'Maccabi Ironi Ashdod',
        'founded': 1961,
        'dissolved': 1999,
        'city': 'Ashdod, Israel',
        },

    {
        'name': 'Bayer Leverkusen',
        'founded': datetime.datetime(1904, 7, 1),
        'city': 'Leverkusen, Germany',
        },

    {
        'name': 'Bayern Munich',
        'founded': datetime.datetime(1900, 2, 27),
        'city': 'Munich, Germany',
        },


    {
        'name': 'Hajduk Split',
        'founded': datetime.datetime(1911, 2, 13),
        'city': 'Split, Croatia',
        },

    {
        'name': 'Glenavon FC',
        'founded': 1889,
        'city': 'Lurgan, Northern Ireland',
        },

    {
        'name': 'Helsingborgs IF',
        'founded': datetime.datetime(1907, 6, 4),
        'city': 'Helsingborg, Sweden',
        },

    {
        'name': 'Red Star Belgrade',
        'founded': datetime.datetime(1945, 3, 4),
        'city': 'Belgrade, Serbia',
        },



    {
        'name': 'Real Oviedo',
        'founded': datetime.datetime(1926, 3, 26),
        'city': 'Oviedo, Spain',
        },

    {
        'name': 'West Bromwich Albion',
        'founded': 1878,
        'city': 'West Bromwich, England',
        },


    {
        'name': 'West Ham United',
        'founded': 1895,
        'city': 'London, England',
        },


    {
        'name': '1. FC Saarbrucken',
        'founded': 1903,
        'city': 'Saarbrucken, Germany',
        },

    {
        'name': 'Eintracht Braunschweig',
        'founded': datetime.datetime(1895, 12, 15),
        'city': 'Braunschweig, Germany',
        },


    {
        'name': 'FC Avenir Beggen',
        'founded': datetime.datetime(1915, 7, 1),
        'city': 'Luxembourg City, Luxembourg',
        },


    {
        'name': '1860 Munich',
        'founded': datetime.datetime(1860, 5, 17),
        'city': 'Munich, Germany',
        },

    {
        'name': 'Macclesfield Town F.C.',
        'founded': 1874,
        'city': 'Macclesfield, England',
        },


    {
        'name': 'SG Egelsbach',
        'founded': datetime.datetime(1945, 11, 10),
        'city': 'Egelsbach, Germany',
        },

    {
        'name': 'FC St. Pauli',
        'founded': datetime.datetime(1910, 5, 15),
        'city': 'St.Pauli, Germany',
        },

    {
        'name': 'Hannover 96',
        'founded': datetime.datetime(1896, 4, 12),
        'city': 'Hannover, Germany',
        },

    {
        'name': 'Charleroi SC',
        'founded': 1904,
        'city': 'Charleroi, Belgium',
        },




    # Spain

    {
        'name': 'FC Barcelona',
        'founded': datetime.datetime(1899, 11, 29),
        'city': 'Barcelona, Spain',
        },

    {
        'name': 'RCD Espanyol',
        'founded': datetime.datetime(1900, 10, 28),
        'city': 'Barcelona, Spain',
        },

    {
        'name': 'CE Sabadell FC',
        'founded': 1903,
        'city': 'Sabadell, Spain',
        },

    {
        'name': 'Real Valladolid',
        'founded': 1928,
        'city': 'Valladolid, Spain',
        },

    # Belgium
    {
        'name': 'Royal Antwerp F.C.',
        'founded': 1880,
        'city': 'Antwerp, Belgium',
        },

    # Netherlands
    {
        'name': 'AFC Ajax',
        'founded': datetime.datetime(1900, 3, 18),
        'city': 'Amsterdam, Netherlands',
        },

    {
        'name': 'PSV Eindhoven',
        'founded': datetime.datetime(1913, 8, 31),
        'city': 'Eindhoven, Netherlands',
        },

    {
        'name': 'Feyenoord',
        'founded': datetime.datetime(1908, 7, 19),
        'city': 'Rotterdam, Netherlands',
        },

    # Greece
    {
        'name': 'Apollon Limassol',
        'founded': datetime.datetime(1954, 4, 14),
        'city': 'Limassol, Cyprus',
        },

    {
        'name': 'AEK Athens F.C.',
        'founded': 1924,
        'city': 'Athens, Greece',
        },

    # Austria
    {
        'name': 'Rapid Vienna',
        'founded': 1899,
        'city': 'Vienna, Austria',
        },

    {
        'name': 'FC Red Bull Salzburg',
        'founded': 1933,
        'city': 'Salzburg, Austria',
        },
    
    # Switzerland
    {
        'name': 'Grasshoppers',
        'founded': datetime.datetime(1886, 9, 1),
        'city': 'Zurich, Switzerland',
        },

    {
        'name': 'BSC Young Boys',
        'founded': datetime.datetime(1898, 3, 14),
        'city': 'Bern, Switzerland',
        },

    {
        'name': 'Ferencvaros',
        'founded': datetime.datetime(1899, 5, 3),
        'city': 'Budapest, Hungary',
        },

    {
        'name': 'Újpest FC',
        'founded': datetime.datetime(1885, 6, 16),
        'city': 'Budapest, Hungary',
        },

    {
        'name': 'Slavia Prague',
        'founded': datetime.datetime(1892, 11, 2),
        'city': 'Prague, Czech Republic',
        },

    {
        'name': 'Sparta Prague',
        'founded': datetime.datetime(1893, 11, 16),
        'city': 'Prague, Czech Republic',
        },

    {
        'name': 'SSK Vitkovice',
        'founded': 1919,
        'city': 'Vitkovice, Czech Republic',
        },

    {
        'name': 'Besiktas',
        'founded': datetime.datetime(1903, 3, 19),
        'city': 'Istanbul, Turkey',
        },


    {
        'name': 'Galatasaray',
        'founded': datetime.datetime(1905, 10, 1),
        'city': 'Istanbul, Turkey',
        },

    {
        'name': 'Fenerbahce',
        'founded': datetime.datetime(1907, 5, 3),
        'city': 'Istanbul, Turkey',
        },

    {
        'name': 'Dynamo Kiev',
        'founded': datetime.datetime(1927, 5, 13),
        'city': 'Kiev, Ukraine',
        },

    {
        'name': 'Rubin Kazan',
        'founded': datetime.datetime(1958, 4, 20),
        'city': 'Kazan, Russia',
        },

    {
        'name': 'Torpedo Moscow',
        'founded': 1930,
        'city': 'Moscow, Russia',
        },

    # Portugal
    {
        'name': 'Académica de Coimbra',
        'founded': 1876,
        'city': 'Coimbra, Portugal',
        },

    {
        'name': 'S.L. Benfica',
        'founded': datetime.datetime(1904, 2, 28),
        'city': 'Lisbon, Portugal',
        },

    {
        'name': 'A.C. Marinhense',
        'founded': 1923,
        'city': 'Marinha Grande, Portugal',
        },

    {
        'name': 'C.S. Maritimo',
        'founded': datetime.datetime(2010, 9, 20),
        'city': 'Funchal, Portugal',
        },

    {
        'name': 'C.D. Santa Clara',
        'founded': datetime.datetime(1927, 5, 12),
        'city': 'Ponta Delgada, Portugal',
        },

    {
        'name': 'Deportivo La Coruña',
        'founded': 1906,
        'city': 'A Coruña, Spain',
        },

    {
        'name': 'Sporting Lisbon',
        'founded': datetime.datetime(1906, 7, 1),
        'city': 'Lisbon, Portugal',
        },

    {
        'name': 'Varzim S.C.',
        'founded': datetime.datetime(1915, 12, 25),
        'city': 'Póvoa de Varzim, Portugal',
        },

    {
        'name': 'União de Santarém',
        'city': 'Santarém, Portugal',
        },

    {
        'name': 'FC Girondins de Bordeaux',
        'founded': 1881, 
        'city': 'Bordeaux, France',
        },

    {
        'name': 'FC Istres',
        'founded': 1920,
        'city': 'Fos-sur-Mer, France',
        },

    {
        'name': 'AS Monaco FC',
        'founded': datetime.datetime(1924, 8, 23),
        'city': 'Fontvielle, Monaco',
        },

    {
        'name': 'FC Nantes',
        'founded': 1943,
        'city': 'Nantes, France',
        },

    {
        'name': 'OGC Nice',
        'founded': 1904,
        'city': 'Nice, France',
        },

    {
        'name': 'Partizan Belgrade',
        'founded': datetime.datetime(1945, 10, 4),
        'city': 'Belgrade, Serbia',
        },

    {
        'name': 'Paris Saint-Germain F.C.',
        'founded': datetime.datetime(1970, 8, 12),
        'city': 'Paris, France',
        },

    {
        'name': 'Parma F.C.',
        'founded': datetime.datetime(1913, 12, 16),
        'city': 'Parma, Italy',
        },


    {
        'name': 'Arezzo',
        'founded': 1923, 
        'city': 'Arezzo, Italy',
        },

    {
        'name': 'A.S. Bari',
        'founded': 1908,
        'city': 'Bari, Italy',
        },

    {
        'name': 'Bologna F.C. 1909',
        'founded': 1909,
        'city': 'Bologna, Italy',
        },

    {
        'name': 'AFC Fiorentina',
        'founded': datetime.datetime(1926, 8, 26),
        'city': 'Florence, Italy',
        },

    {
        'name': 'Genoa CFC',
        'founded': datetime.datetime(1893, 9, 7),
        'city': 'Genoa, Italy',
        },

    {
        'name': 'Inter Milan',
        'founded': datetime.datetime(1908, 3, 9),
        'city': 'Milan, Italy',
        },

    {
        'name': 'Mantova F.C.',
        'founded': 1911, 
        'city': 'Mantua, Italy',
        },

    {
        'name': 'AC Milan',
        'founded': datetime.datetime(1899, 12, 16),
        'city': 'Milan, Italy',
        },

    {
        'name': 'Modena F.C.',
        'founded': 1912, 
        'city': 'Modena, Italy',
        },

    {
        'name': 'S.S.C. Napoli',
        'founded': 1926, 
        'city': 'Naples, Italy',
        },

    {
        'name': 'A.S. Roma',
        'founded': datetime.datetime(1927, 7, 22),
        'city': 'Rome, Italy',
        },

    {
        'name': 'U.C. Sampdoria',
        'founded': datetime.datetime(1946, 8, 1),
        'city': 'Genoa, Italy',
        },

    {
        'name': 'Venezia',
        'founded': 1907,
        'city': 'Venice, Italy',
        },

    {
        'name': 'Vicenza Calcio',
        'founded': datetime.datetime(1902, 3, 9),
        'city': 'Vicenza, Italy',
        },

    {
        'name': 'Videoton FC',
        'founded': 1941,
        'city': 'Székesfehérvár, Hungary',
        },

    {
        'name': 'Amica Wronki',
        'founded': 1992,
        'city': 'Warsaw, Poland',
        },

    {
        'name': 'Gornik Zabrze',
        'founded': 1948,
        'city': 'Zabrze, Poland',
        },

    {
        'name': 'KS Ruch',
        'founded': datetime.datetime(1920, 4, 20),
        'city': 'Chorzów, Poland',
        },

    {
        'name': 'Legia Warszawa',
        'founded': datetime.datetime(1916, 3, 5), 
        'city': 'Warsaw, Poland',
        },

    {
        'name': 'Wisla Krakow',
        'founded': 1906,
        'city': 'Kraków, Poland',
        },

    {
        'name': 'Aberdeen F.C.',
        'founded': 1903,
        'city': 'Aberdeen, Scotland',
        },


    {
        'name': 'Glasgow Celtic F.C.',
        'founded': 1888,
        'city': 'Glasgow, Scotland',
        },


    {
        'name': 'Glasgow Rangers',
        'founded': 1872,
        'city': 'Glasgow, Scotland',
        },


    {
        'name': 'Hearts of Midlothian F.C.',
        'founded': 1874,
        'city': 'Edinburgh, Scotland',
        },


    {
        'name': 'Kilmarnock F.C.',
        'founded': datetime.datetime(1869, 1, 5),
        'city': 'Kilmarnock, Scotland',
        },
    
    {
        'name': 'BK Häcken',
        'founded': datetime.datetime(194, 8, 2),
        'city': 'Gothenburg, Sweden',
        },
    
    {
        'name': 'Valencia CF',
        'founded': datetime.datetime(1919, 3, 18),
        'city': 'Valencia, Spain',
        },
    
    {
        'name': 'Olympique Lyonnais',
        'founded': 1899,
        'city': 'Lyon, France',
        },
    
    {
        'name': 'Montpellier Herault SC',
        'founded': 1974,
        'city': 'Montpellier, France',
        },
    
    {
        'name': 'Swansea City',
        'founded': 1912,
        'city': 'Swansea, England',
        },
    
    {
        'name': 'Næstved BK',
        'founded': 1939,
        'city': 'Naestved, Denmark',
        },
    
    {
        'name': 'SV Wageningen',
        'city': 'Wageningen,Netherlands',
        },
    
    {
        'name': 'FC Groningen',
        'founded': datetime.datetime(1971, 6, 16),
        'city': 'Groningen, Netherlands',
        },
    
    {
        'name': 'Hertha BSC',
        'founded': datetime.datetime(1892, 7, 25),
        'city': 'Berlin, Germany',
        },
    
    {
        'name': 'Fortuna Sittard',
        'founded': datetime.datetime(1968, 7, 1),
        'city': 'Sittard, Netherlands',
        },
    
    {
        'name': 'FC Dordrecht',
        'founded': datetime.datetime(1883, 8, 16),
        'city': 'Dordrecht, Netherlands',
        },
    
    {
        'name': 'Telstar',
        'founded': datetime.datetime(1963, 7, 17),
        'city': 'Velsen, Netherlands',
        },
    
    {
        'name': 'FC Utrecht',
        'founded': datetime.datetime(1970, 7, 1),
        'city': 'Utrecht, Netherlands',
        },

    {
        'name': 'FC Den Bosch',
        'founded': datetime.datetime(1965, 8, 18),
        'city': '\'s-Hertogenbosch, Netherlands',
        },

    {
        'name': 'ADO Den Haag',
        'founded': datetime.datetime(1905, 2, 1),
        'city': 'The Hague, Netherlands',
        },

    {
        'name': 'Bangor City F.C.',
        'founded': 1876,
        'city': 'Bangor, England',
        },

    {
        'name': 'MVV Maastricht',
        'founded': datetime.datetime(1902, 4, 2),
        'city': 'Maastricht, Netherlands',
        },

    {
        'name': 'Wigan Athletic F.C.',
        'founded': 1932,
        'city': 'Wigan, England',
        },

    {
        'name': 'Sunderland A.F.C.',
        'founded': 1879,
        'city': 'Sunderland, England',
        },

    {
        'name': 'La Louviere',
        'city': 'La Louviere, Belguim',
        },

    {
        'name': 'FC Birsfelden',
        'founded': datetime.datetime(1920, 7, 1),
        'city': 'Basel, Switzerland',
        },

    {
        'name': 'Wycombe Wanderers',
        'founded': 1887,
        'city': 'High Wycombe, England',
        },
    {
        'name': 'Sheffield Wednesday',
        'founded': 1867,
        'city': 'Sheffield, England',
        },
    {
        'name': 'VfL Bochum',
        'founded': 1848,
        'city': 'Bochum, England',
        },
    {
        'name': 'RSC Anderlecht',
        'founded': datetime.datetime(1908, 5, 27),
        'city': 'Anderlecht, Belgium',
        },
    {
        'name': 'Southampton F.C.',
        'founded': 1979,
        'city': 'Southampton, England',
        },
    {
        'name': 'Motherwell',
        'founded': datetime.datetime(1886, 5, 17),
        'city': 'Motherwell, Scotland',
        },
    {
        'name': 'Valur FC',
        'founded': datetime.datetime(1911, 5, 11),
        'city': 'Reykjavik, Iceland',
        },
    {
        'name': 'Lille OSC',
        'founded': datetime.datetime(1944, 9, 23),
        'city': 'Lille, France',
        },
    {
        'name': 'C.F. Os Belenenses',
        'founded': datetime.datetime(1919, 9, 23),
        'city': 'Lisbon, Portugal',
        },
    {
        'name': 'Viborg FF',
        'founded': 1896, 
        'city': 'Viborg, Denmark',
        },
    {
        'name': 'Reggina Calcio',
        'founded': 1914,
        'city': 'Reggio Calabria, Italy',
        },
    {
        'name': 'Clube Oriental de Lisboa',
        'founded': 1946,
        'city': 'Lisbon, Portugal',
        },
    {
        'name': 'FK Bodø/Glimt',
        'founded': datetime.datetime(1916, 9, 19),
        'city': 'Bodo, Norway',
        },
    {
        'name': 'Real Murcia',
        'founded': 1908,
        'city': 'Murcia, Spain',
        },
    {
        'name': 'Rabo de Peixe',
        'founded': 1985,
        'city': 'Rabo de Peixe, Spain',
        },
    {
        'name': 'Bolton Wanderers',
        'founded': 1874,
        'city': 'Horwich, England',
        },
    {
        'name': 'Almere City FC',
        'founded': datetime.datetime(2001, 9, 14),
        'city': 'Almere, Netherlands',
        },

    {
        'name': 'Arsenal',
        'founded': 1886,
        'city': 'London, England',
        },


    {
        'name': 'US Cantazaro 1929',
        'founded': 1929,
        'city': 'Catanzaro, Italy',
        },
    {
        'name': 'Finn Harps',
        'founded': 1954,
        'city': 'Ballybofey, Ireland',
        },
    {
        'name': 'Olympiakos',
        'founded': datetime.datetime(1925, 3, 10),
        'city': 'Piraeus, Greece',
        },

    {
        'name': 'Neuchâtel Xamax',
        'founded': 1970,
        'city': 'Neuchâtel, Switzerland',
        },
    {
        'name': 'FC Zurich',
        'founded': 1896,
        'city': 'Zurich, Switzerland',
        },
    {
        'name': 'Chelsea FC',
        'founded': datetime.datetime(1905, 3, 10),
        'city': 'London, England',
        },
    {
        'name': 'Hammarby IF',
        'founded': datetime.datetime(1897, 4, 10),
        'city': 'Johanneshov, Sweden',
        },
    {
        'name': 'Coventry City FC',
        'founded': datetime.datetime(1883, 8, 13),
        'city': 'Coventry, England',
        },
    {
        'name': 'Hertha Berlin',
        'founded': datetime.datetime(1892, 7, 25),
        'city': 'Berlin, Germany',
        },
    {
        'name': 'Tennis Borussia Berlin',
        'founded': datetime.datetime(1902, 4, 9),
        'city': 'Berlin, Germany',
        },
    {
        'name': 'Hapoel Petah Tikva F.C.',
        'founded': 1934,
        'city': 'Petah Tikva, Israel',
        },
    {
        'name': 'Lazio',
        'founded': datetime.datetime(1900, 1, 9),
        'city': 'Rome, Italy',
        },
    {
        'name': 'Stockport County F.C.',
        'founded': 1883,
        'city': 'Stockport, England',
        },
    {
        'name': 'Blackpool F.C.',
        'founded': datetime.datetime(1887, 7, 26),
        'city': 'Blackpool, England',
        },


    {
        'name': 'Workington A.F.C.',
        'founded': 1921,
        'city': 'Workington, England',
        },
    {
        'name': 'Portsmouth F.C.',
        'founded': 1898,
        'city': 'Portsmouth, England',
        },
    {
        'name': 'Port Vale F.C.',
        'founded': 1876,
        'city': 'Burslem, England',
        },
    {
        'name': 'Glentoran',
        'founded': 1882,
        'city': 'Belfast, Northern Ireland',
        },
    {
        'name': 'Coleraine F.C.',
        'founded': 1927,
        'city': 'Coleraine, Northern Ireland',
        },
    {
        'name': 'Ards F.C.',
        'founded': 1900,
        'city': 'Newtownards, Northern Ireland',
        },
    {
        'name': 'Brescia Calcio', 
        'founded': 1911,
        'city': 'Brescia, Italy',
        },

    {
        'name': 'Galway United FC',
        'founded': 1937,
        'city': 'Galway, Ireland',
        },
    {
        'name': 'Sligo Rovers',
        'founded': 1928,
        'city': 'Sligo, Ireland',
        },
    {
        'name': 'VfB Stuttgart',
        'founded': datetime.datetime(1912, 4, 1),
        'city': 'Stuttgart, Germany',
        },
    {
        'name': 'Dundalk F.C.',
        'founded': datetime.datetime(1903, 9, 1),
        'city': 'Dundalk, Ireland',
        },
    {
        'name': 'SC Freiburg',
        'founded': datetime.datetime(1904, 5, 30),
        'city': 'Freiburg im Breisgau, Germany',
        },
    {
        'name': 'Atlético Madrid',
        'founded': datetime.datetime(1903, 4, 26),
        'city': 'Madrid, Spain',
        },
    {
        'name': 'Helmond Sport',
        'founded': datetime.datetime(1967, 7, 27),
        'city': 'Helmond, Netherlands',
        },
    {
        'name': 'Middlesbrough F.C.',
        'founded': 1876,
        'city': 'Middlesbrough, England',
        },
    {
        'name': 'Leicester City',
        'founded': 1884,
        'city': 'Leicester, England',
        },
    {
        'name': 'Shrewsbury Town',
        'founded': 1886,
        'city': 'New Meadow, England',
        },
    {
        'name': 'Derby County',
        'founded': datetime.datetime(1884, 2, 5),
        'city': 'Derby, England',
        },
    {
        'name': 'Lincoln City',
        'founded': 1884,
        'city': 'Lincoln, England',
        },
    {
        'name': 'Leeds United',
        'founded': 1919,
        'city': 'Leeds, England',
        },
    {
        'name': 'Manchester City F.C.',
        'founded': 1880,
        'city': 'Manchester City, England',
        },
    {
        'name': 'Nottingham Forest F.C.',
        'founded': 1865,
        'city': 'West Bridgford, England',
        },
    {
        'name': 'Luton Town F.C.',
        'founded': datetime.datetime(1885, 4, 11),
        'city': 'Luton, England',
        },
    {
        'name': 'Linfield F.C.',
        'founded': 1886,
        'city': 'Belfast, Northern Ireland',
        },
    {
        'name': 'St. Mirren',
        'founded': 1877,
        'city': 'Paisley, Scotland',
        },
    {
        'name': 'Standard Liege',
        'founded': 1898,
        'city': 'Liege, Belgium',
        },
    {
        'name': 'Hereford United',
        'founded': 1924,
        'city': 'Hereford, England',
        },
    {
        'name': 'Real Betis',
        'founded': datetime.datetime(1907, 9, 12),
        'city': 'Seville, Spain',
        },
    {
        'name': 'Athlone Town',
        'founded': 1887,
        'city': 'Athlone, England',
        },
    {
        'name': 'VfB Oldenburg',
        'founded': 1897,
        'city': 'Oldenburg, Germany',
        },
    {
        'name': 'Malmo FF',
        'founded': 1910,
        'city': 'Malmo, Sweden',
        },
    {
        'name': 'Borussia Dortmund',
        'founded': datetime.datetime(1909, 12, 19),
        'city': 'Dortmund, Germany',
        },
    {
        'name': 'Borussia Mönchengladbach',
        'founded': datetime.datetime(1900, 8, 1),
        'city': 'Mönchengladbach, Germany',
        },

    {
        'name': 'Worcester City F.C.',
        'founded': 1902,
        'city': 'Worcester, England',
        },
    {
        'name': 'Bristol City',
        'founded': 1897,
        'city': 'Bristol, England',
        },
    {
        'name': 'Rot-Weiss Essen',
        'founded': datetime.datetime(1907, 2, 1),
        'city': 'Essen, Germany',
        },
    {
        'name': 'FC Dynamo Moscow',
        'founded': 1923,
        'city': 'Moscow, Russia',
        },

    {
        'name': 'Avellino',
        'founded': 1912,
        'city': 'Aveillino',
        },
    {
        'name': 'Aston Villa F.C.',
        'founded': 1874,
        'city': 'Birminghamn, England',
        },
    {
        'name': 'IFK Göteborg',
        'founded': datetime.datetime(1904, 10, 4),
        'city': 'Gothenburg, Sweden',
        },
    {
        'name': 'Ikast FS',
        'founded': 1935,
        'city': 'Ikast, Denmark',
        },
    {
        'name': 'Hamburger SV',
        'founded': datetime.datetime(1887, 9, 29),
        'city': 'Hamburg, Germany',
        },
    {
        'name': '1. FC Köln',
        'founded': datetime.datetime(1948, 2, 13),
        'city': 'Cologne, Germany',
        },
    {
        'name': 'Juventus',
        'founded': datetime.datetime(1897, 11, 1),
        'city': 'Turin, Italy',
        },
    {
        'name': 'Girona FC',
        'founded': 1930,
        'city': 'Girona, Spain',
        },
    {
        'name': 'Liverpool F.C.',
        'founded': datetime.datetime(1892, 3, 15),
        'city': 'Liverpool, England',
        },
    {
        'name': 'Real Madrid',
        'founded': datetime.datetime(1902, 3, 6),
        'city': 'Madrid, Spain',
        },
    {
        'name': 'Tottenham Hotspur',
        'founded': 1882,
        'city': 'London, England',
        },
    {
        'name': 'FC Schalke 04',
        'founded': datetime.datetime(1904, 5, 4),
        'city': 'Gelsenkirchen, Germany',
        },
    {
        'name': 'Zagłębie Lubin',
        'founded': datetime.datetime(1945, 9, 10),
        'city': 'Lubin, Poland',
        },

    {
        'name': 'Zagłębie Sosnowiec',
        'founded': 1906,
        'city': 'Sosnowiec, Poland',
        },
    {
        'name': 'Stoke City F.C.',
        'founded': 1863,
        'city': 'Stoke-on-Trent, England',
        },
    {
        'name': 'SV Munster',
        'founded': datetime.datetime(1946, 5, 5),
        'city': 'Munster, Germany',
        },
    {
        'name': 'VfR Heilbronn',
        'founded': 1896,
        'dissolved': 2003,
        'city': 'Heilbronn, Germany',
        },
    {
        'name': 'VfR Pforzheim',
        'founded': 1897,
        'dissolved': datetime.datetime(2010, 6, 30),
        'city': 'Pforzheim, Germany',
        },
    {
        'name': 'VfL Osnabrück',
        'founded': 1899,
        'city': 'Osnabruck, Germany',
        },
    {
        'name': 'SpVgg Plattling',
        'founded': 1919,
        'city': 'Plattling, Germany',
        },
    {
        'name': 'AGH Aarhus',
        'founded': 1880,
        'city': 'Aarhus, Denmark',
        },
    {
        'name': 'Wolverhampton Wanderers F.C.',
        'founded': 1877,
        'city': 'Wolverhampton, England',
        },

    {
        'name': 'ASV Bergedorf',
        'founded': datetime.datetime(1885, 3, 29),
        'city': 'Bergedorf, Germany',
        },
    {
        'name': 'VfL Marburg',
        'founded': datetime.datetime(1860, 7, 28),
        'city': 'Marburg, Germany',
        },

    {
        'name': 'Wisbech Town F.C.',
        'founded': 1920,
        'city': 'Wisbech, England',
        },

    {
        'name': 'King\'s Lynn F.C.',
        'founded': 1879,
        'dissolved': datetime.datetime(2009, 11, 25),
        'city': 'King\'s Lynn, England',
        },

    {
        'name': 'Ely City FC',
        'founded': 1885,
        'city': 'Ely, England',
        },

    {
        'name': 'Newmarket Town F.C.',
        'founded': datetime.datetime(1877, 11, 22),
        'city': 'Newmarket, England',
        },

    {
        'name': 'Peterborough United F.C.',
        'founded': 1934,
        'city': 'Peterborough, England',
        },

    {
        'name': 'Barking F.C.',
        'founded': 1880,
        'city': 'Barking, England',
        },

    {
        'name': 'Bromsgrove Rovers F.C.',
        'founded': 1885,
        'dissolved': 2010,
        'city': 'Bromsgrove, England',
        },
    {
        'name': 'Crystal Palace F.C.',
        'founded': datetime.datetime(1905, 9, 10),
        'city': 'South Norwood, England',
        },

    {
        'name': 'Pegasus A.F.C.',
        'founded': 1948,
        'city': 'Oxford, England',
        },

    {
        'name': 'Millwall F.C.',
        'founded': datetime.datetime(1885, 10, 3),
        'city': 'South Bermondsey, England',
        },

    {
        'name': 'Nørresundby Boldklub',
        'founded': datetime.datetime(1946, 6, 6),
        'city': 'Aalborg, Denmark',
        },

    {
        'name': 'FinnPa',
        'founded': 1965,
        'dissolved': 1998,
        'city': 'Helsinki, Finland',
        },

    {
        'name': 'AC Reggiana 1919',
        'founded': 1919,
        'city': 'Reggiana, Italy',
        },

    {
        'name': 'IBV',
        'founded': 1903,
        'city': 'Vestmannaeyjar, Iceland',
        },

    {
        'name': 'Lyngby BK',
        'founded': 1921,
        'city': 'Lyngby, Denmark',
        },

    {
        'name': 'Rosenborg BK',
        'founded': datetime.datetime(1917, 5, 19),
        'city': 'Trondheim, Norway',
        },

    {
        'name': 'Hibernian F.C.',
        'founded': 1875,
        'city': 'Leith, Scotland',
        },
    {
        'name': 'Torino FC',
        'founded': 1906,
        'city': 'Turin, Italy',
        },
    {
        'name': 'Vitória de Setúbal',
        'founded': datetime.datetime(1910, 11, 20),
        'city': 'Setubal, Portugal',
        },
    {
        'name': 'SpVgg Kaufbeuren',
        'founded': 1909,
        'city': 'Kaufbeuren, Germany',
        },
    {
        'name': 'VfL Oldesloe',
        'founded': 1862,
        'city': 'Bald Oldesloe, Germany',
        },
    {
        'name': 'Cordoba CF',
        'founded': 1954,
        'city': 'Cordoba, Spain',
        },
    {
        'name': 'RSD Alcalá',
        'founded': 1929,
        'city': 'Alcala de Henares',
        },
    {
        'name': 'Coria CF',
        'founded': 1923,
        'city': 'Coria del Rio, Spain',
        },
    {
        'name': 'AEL Limassol',
        'founded': datetime.datetime(1930, 10, 4),
        'city': 'Limassol, Greece',
        },
    {
        'name': 'Dunfermline',
        'founded': datetime.datetime(1885, 6, 1),
        'city': 'Dunfermline, Scotland',
        },
    {
        'name': 'Eintracht Braunschwieg',
        'founded': datetime.datetime(1895, 12, 15),
        'city': 'Braunschweig, Germany',
        },
    {
        'name': 'Dundee United',
        'founded': datetime.datetime(1909, 5, 24),
        'city': 'Dundee, Scotland',
        },
    {
        'name': 'FK Inter Bratislava',
        'founded': datetime.datetime(1940, 7, 1),
        'city': 'Bratislava, Slovakia',
        },
    {
        'name': 'FC Zenit Saint Petersburg',
        'founded': 1924,
        'city': 'Saint Petersburg, Russia',
        },

    {
        'name': 'Larne F.C.',
        'founded': 1889,
        'city': 'Larne, Northern Ireland',
        },
    {
        'name': 'SV Schwechat',
        'founded': 1903,
        'city': 'Schwechat, Austria',
        },
    {
        'name': 'Dundee FC',
        'founded': 1893,
        'city': 'Dundee, Scotland',
        },
    {
        'name': 'Vitória de Guimarães',
        'founded': 1922,
        'city': 'Guimaraes, Portugal',
        },
    {
        'name': 'IF Elfsborg',
        'founded': datetime.datetime(1904, 6, 26),
        'city': 'Elfsborg, Sweden',
        },

    {
        'name': 'Palermo',
        'founded': 1900,
        'city': 'Palermo, Italy',
        },
    {
        'name': 'Valenciennes FC',
        'founded': 1913,
        'city': 'Valenciennes, France',
        },

    ]
