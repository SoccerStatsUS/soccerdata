#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

#The Golden Ball award is presented to the best player at each 
# FIFA World Cup finals, with a shortlist drawn up by the 
# FIFA technical committee and the winner voted for by representatives of the media. 
# Those who finish as runners-up in the vote receive the Silver Ball and 
# Bronze Ball awards as the second and third most outstanding players in the tournament respectively.

golden_ball = [
    (1930, 'José Nasazzi', 'Guillermo Stábile', 'José Leandro Andrade'),
    (1934, 'Giuseppe Meazza', 'Matthias Sindelar', 'Oldřich Nejedlý'),
    (1938, 'Leônidas', 'Silvio Piola', 'György Sárosi'),
    (1950, 'Zizinho', 'Juan Schiaffino', 'Ademir'),
    (1954, 'Ferenc Puskás', 'Sándor Kocsis', 'Fritz Walter'),
    (1958, 'Didi', 'Pelé', 'Just Fontaine'),
    (1962, 'Garrincha', 'Josef Masopust' 'Leonel Sánchez'),
    (1966, 'Bobby Charlton', 'Bobby Moore', 'Eusébio'),
    (1970, 'Pelé', 'Gérson', 'Gerd Muller'), 
    (1974, 'Johan Cruijff', 'Franz Beckenbauer', 'Kazimierz Deyna'),
    (1978, 'Mario Kempes', 'Paolo Rossi', 'Dirceu'),
    (1982, 'Paolo Rossi', 'Falcão', 'Karl-Heinz Rummenigge'),
    (1986, 'Diego Maradona', 'Harald Schumacher', 'Preben Elkjær'),
    (1990, 'Salvatore Schillaci', 'Lothar Matthäus', 'Diego Maradona'),
    (1994, 'Romário', 'Roberto Baggio', 'Hristo Stoichkov'), 
    (1998, 'Ronaldo', 'Davor Šuker', 'Lilian Thuram'),
    (2002, 'Oliver Kahn', 'Ronaldo', 'Hong Myung-Bo'),
    (2006, 'Zinedine Zidane', 'Fabio Cannavaro', 'Andrea Pirlo'),
    (2010, 'Diego Forlán', 'Wesley Sneijder', 'David Villa'),
    ]

young_player = [
    (1958, 'Pelé'),
    (1962, 'Albert'),
    (1966, 'Franz Beckenbauer'),
    (1970, 'Teofilo Cubillas'),
    (1974, 'Władysław Żmuda'),
    (1978, 'Antonio Cabrini'),
    (1982, 'Manuel Amoros'),
    (1986, 'Enzo Scifo'),
    (1990, 'Robert Prosinečki'),
    (1994, 'Marc Overmars'),
    (1998, 'Michael Owen'),
    (2002, 'Landon Donovan'),
    (2006, 'Lukas Podolski'),
    (2010, 'Thomas Müller'),
    ]


all_star_team = {
    1930: [
        'Enrique Ballesteros',
        'José Nasazzi',
        'Milutin Ivković',
        'Luis Monti',
        'Álvaro Gestido',
        'José Andrade',
        'Pedro Cea',
        'Héctor Castro',
        'Héctor Scarone',
        'Guillermo Stábile',
        'Bert Patenaude',
        ],
    1934: [
        'Ricardo Zamora',
        'Jacinto Quincoces',
        'Eraldo Monzeglio',
        'Luis Monti',
        'Attilio Ferraris',
        'Leonardo Cilaurren',
        'Giuseppe Meazza',
        'Raimundo Orsi',
        'Enrique Guaita',
        'Matthias Sindelar',
        'Oldřich Nejedlý',
        ],
    1938: [
        'František Plánička',
        'Pietro Rava',
        'Alfredo Foni',
        'Domingos da Guia',
        'Michele Andreolo',
        'Ugo Locatelli',
        'Silvio Piola',
        'Gino Colaussi',
        'György Sárosi',
        'Gyula Zsengellér',
        'Leônidas',
        ],
    1950: [
        'Roque Máspoli',
        'Erik Nilsson',
        'José Parra',
        'Schubert Gambetta',
        'Obdulio Varela',
        'Bauer',
        'Alcides Ghiggia',
        'Jair',
        'Zizinho',
        'Ademir',
        'Juan Alberto Schiaffino',
        ],
    1954: [
        'Gyula Grosics',
        'Ernst Ocwirk',
        'Djalma Santos',
        'José Santamaría',
        'Fritz Walter',
        'József Bozsik',
        'Nándor Hidegkuti',
        'Zoltan Czibor',
        'Helmut Rahn',
        'Ferenc Puskás',
        'Sándor Kocsis',
        ],
    1958: [
        'Harry Gregg',
        'Djalma Santos',
        'Bellini',
        'Nílton Santos',
        'Danny Blanchflower',
        'Didi',
        'Gunnar Gren',
        'Raymond Kopa',
        'Pelé',
        'Garrincha',
        'Just Fontaine',
        ],
    1962: [
        'Viliam Schrojf',
        'Djalma Santos',
        'Cesare Maldini',
        'Valeriy Voronin',
        'Karl-Heinz Schnellinger',
        'Zagallo',
        'Zito',
        'Josef Masopust',
        'Vavá',
        'Garrincha',
        'Leonel Sánchez',
        ],
    1966: [
        'Gordon Banks',
        'George Cohen',
        'Bobby Moore',
        'Vicente',
        'Silvio Marzolini',
        'Franz Beckenbauer',
        'Mário Coluna',
        'Bobby Charlton',
        'Florian Albert',
        'Uwe Seeler',
        'Eusébio',
        ],
    1970: [
        'Ladislao Mazurkiewicz',
        'Carlos Alberto',
        'Piazza',
        'Franz Beckenbauer',
        'Giacinto Facchetti',
        'Gérson',
        'Teofilo Cubillas',
        'Bobby Charlton',
        'Pelé',
        'Gerd Müller',
        'Jairzinho',
        ],
    1974: [
        'Jan Tomaszewski',
        'Berti Vogts',
        'Wim Suurbier',
        'Franz Beckenbauer',
        'Marinho Chagas',
        'Ruud Krol',
        'Wolfgang Overath',
        'Kazimierz Deyna',
        'Johan Neeskens',
        'Rob Rensenbrink',
        'Johan Cruyff',
        'Grzegorz Lato',
        ],
    1978: [
        'Ubaldo Fillol',
        'Berti Vogts',
        'Ruud Krol',
        'Daniel Passarella',
        'Alberto Tarantini',
        'Dirceu',
        'Teófilo Cubillas',
        'Rob Rensenbrink',
        'Roberto Bettega',
        'Paolo Rossi',
        'Mario Kempes',
        ],
    1982: [
        'Dino Zoff',
        'Luizinho',
        'Júnior',
        'Claudio Gentile',
        'Fulvio Collovati',
        'Zbigniew Boniek',
        'Falcão',
        'Michel Platini',
        'Zico',
        'Sócrates',
        'Paolo Rossi',
        'Karl-Heinz Rummenigge',
        ],
    1986: [
        'Harald Schumacher',
        'Josimar',
        'Manuel Amoros',
        'Maxime Bossis',
        'Jan Ceulemans',
        'Felix Magath',
        'Michel Platini',
        'Diego Maradona',
        'Preben Elkjær Larsen',
        'Emilio Butragueño',
        'Gary Lineker',
        ],
    1990: [
        'Sergio Goycochea',
        'Andreas Brehme',
        'Paolo Maldini',
        'Franco Baresi',
        'Diego Maradona',
        'Lothar Matthäus',
        'Roberto Donadoni',
        'Paul Gascoigne',
        'Salvatore Schillaci',
        'Roger Milla',
        'Jürgen Klinsmann',
        'Claudio Caniggia',
        ],
    1994: [
        'Michel Preud\'homme',
        'Jorginho',
        'Márcio Santos',
        'Paolo Maldini',
        'Dunga',
        'Krasimir Balakov',
        'Gheorghe Hagi',
        'Tomas Brolin',
        'Romário',
        'Hristo Stoichkov',
        'Roberto Baggio',
        ],
    1998: [
        'Fabien Barthez',
        'José Luis Chilavert',
        'Roberto Carlos',
        'Marcel Desailly',
        'Lilian Thuram',
        'Frank de Boer',
        'Carlos Gamarra',
        'Dunga',
        'Rivaldo',
        'Michael Laudrup',
        'Zinedine Zidane',
        'Edgar Davids',
        'Ronaldo',
        'Davor Šuker',
        'Brian Laudrup',
        'Dennis Bergkamp',
        ],
    2002: [
        'Oliver Kahn',
        'Rüştü Reçber',
        'Roberto Carlos',
        'Sol Campbell',
        'Fernando Hierro',
        'Hong Myung-Bo',
        'Alpay Özalan',
        'Rivaldo',
        'Ronaldinho',
        'Michael Ballack',
        'Claudio Reyna',
        'Yoo Sang-Chul',
        'Ronaldo',
        'Miroslav Klose',
        'El Hadji Diouf',
        'Hasan Şaş',
        ],
    2006: [
        'Gianluigi Buffon',
        'Jens Lehmann',
        'Ricardo',
        'Roberto Ayala',
        'John Terry',
        'Lilian Thuram',
        'Philipp Lahm',
        'Fabio Cannavaro',
        'Gianluca Zambrotta',
        'Ricardo Carvalho',
        'Zé Roberto',
        'Patrick Vieira',
        'Zinedine Zidane',
        'Michael Ballack',
        'Andrea Pirlo',
        'Gennaro Gattuso',
        'Luís Figo',
        'Maniche',
        'Hernán Crespo',
        'Thierry Henry',
        'Miroslav Klose',
        'Luca Toni',
        'Francesco Totti',
        ],
    2010: [
        'Iker Casillas',
        'Philipp Lahm',
        'Sergio Ramos',
        'Carles Puyol',
        'Maicon',
        'Andrés Iniesta',
        'Bastian Schweinsteiger',
        'Wesley Sneijder',
        'Xavi',
        'David Villa',
        'Diego Forlán',
        ]
    }
