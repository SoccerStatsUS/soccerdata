#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    {
        'name': 'FC Barcelona',
        'founded': datetime.date(1899, 11, 29),
        'city': 'Barcelona, Spain',
        },

    {
        'name': 'RCD Espanyol',
        'founded': datetime.date(1900, 10, 28),
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
        'founded': datetime.date(1900, 3, 18),
        'city': 'Amsterdam, Netherlands',
        },

    {
        'name': 'PSV Eindhoven',
        'founded': datetime.date(1913, 8, 31),
        'city': 'Eindhoven, Netherlands',
        },

    {
        'name': 'Feyenoord',
        'founded': datetime.date(1908, 7, 19),
        'city': 'Rotterdam, Netherlands',
        },

    # Greece
    {
        'name': 'Apollon Limassol',
        'founded': datetime.date(1954, 4, 14),
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
        'founded': datetime.date(1886, 9, 1),
        'city': 'Zurich, Switzerland',
        },

    {
        'name': 'BSC Young Boys',
        'founded': datetime.date(1898, 3, 14),
        'city': 'Bern, Switzerland',
        },

    {
        'name': 'Ferencvaros',
        'founded': datetime.date(1899, 5, 3),
        'city': 'Budapest, Hungary',
        },

    {
        'name': 'Ujpest',
        'founded': 1885,
        'city': 'Budapest, Hungary',
        },

    {
        'name': 'Slavia Prague',
        'founded': datetime.date(1892, 11, 2),
        'city': 'Prague, Czech Republic',
        },

    {
        'name': 'SSK Vitkovice',
        'founded': 1919,
        'city': 'Vitkovice, Czech Republic',
        },

    {
        'name': 'Besiktas',
        'founded': datetime.date(1903, 3, 19),
        'city': 'Istanbul, Turkey',
        },


    {
        'name': 'Galatasaray',
        'founded': datetime.date(1905, 10, 1),
        'city': 'Istanbul, Turkey',
        },

    {
        'name': 'Fenerbahce',
        'founded': datetime.date(1907, 5, 3)
        'city': 'Istanbul, Turkey',
        },

    {
        'name': 'Dynamo Kiev',
        'founded': datetime.date(1927, 5, 13),
        'city': 'Kiev, Ukraine',
        },

    {
        'name': 'Rubin Kazan',
        'founded': datetime.date(1958, 4, 20),
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
        'founded': datetime.date(1904, 2, 28),
        'city': 'Lisbon, Portugal',
        },

    {
        'name': 'A.C. Marinhense',
        'founded': 1923,
        'city': 'Marinha Grande, Portugal',
        },

    {
        'name': 'C.S. Maritimo',
        'founded': datetime.date(2010, 9, 20),
        'city': 'Funchal, Portugal',
        },

    {
        'name': 'C.D. Santa Clara',
        'founded': datetime.date(1927, 5, 12),
        'city': 'Ponta Delgada, Portugal',
        },

    {
        'name': 'Sporting Clube de Portugal',
        'founded': datetime.date(1906, 7, 1),
        'city': 'Lisbon, Portugal',
        },

    {
        'name': 'Varzim S.C.',
        'founded': datetime.date(1915, 12, 25),
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
        'founded': datetime.date(1924, 8, 23),
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
        'name': 'Paris Saint-Germain F.C.',
        'founded': datetime.date(1970, 8, 12),
        'city': 'Paris, France',
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
        'founded': datetime.date(1926, 8, 26),
        'city': 'Florence, Italy',
        },

    {
        'name': 'Genoa CFC',
        'founded': datetime.date(1893, 9, 7),
        'city': 'Genoa, Italy',
        },

    {
        'name': 'Inter Milan',
        'founded': datetime.date(1908, 3, 9),
        'city': 'Milan, Italy',
        },

    {
        'name': 'Mantova F.C.',
        'founded': 1911, 
        'city': 'Mantua, Italy',
        },

    {
        'name': 'AC Milan',
        'founded': datetime.date(1899, 12, 16),
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
        'founded': datetime.date(1927, 7, 22),
        'city': 'Rome, Italy',
        },

    {
        'name': 'U.C. Sampdoria',
        'founded': datetime.date(1946, 8, 1),
        'city': 'Genoa, Italy',
        },

    {
        'name': 'Venezia',
        'founded': 1907,
        'city': 'Venice, Italy',
        },

    {
        'name': 'Vicenza Calcio',
        'founded': datetime.date(1902, 3, 9),
        'city': 'Vicenza, Italy',
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
        'founded': datetime.date(1920, 4, 20),
        'city': 'Chorzów, Poland',
        },

    {
        'name': 'Legia Warszawa',
        'founded': datetime.date(1916, 3, 5), 
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
        'founded': datetime.date(1869, 1, 5),
        'city': 'Kilmarnock, Scotland',
        },
    
]
