#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# World players of the year.
# This is merged with the FIFA Ballon D'Or.

fifa = {
    'competition': 'FIFA',
    
    'Puskas Award': [
        (2009, 'Cristiano Ronaldo', '?'),
        (2010, 'Hamit Altintop',  '?'),
        ],
}
         

world_player_of_the_year = [
    (1991, ('Lothar Matthäus', 'Jean-Pierre Papin', 'Gary Lineker')),
    (1992, ('Marco van Basten', 'Hristo Stoichkov', 'Thomas Häßler')),
    (1993, ('Roberto Baggio', 'Romário', 'Dennis Bergkamp')),
    (1994, ('Romário', 'Hristo Stoichkov', 'Roberto Baggio')),
    (1995, ('George Weah', 'Paolo Maldini', 'Jürgen Klinsmann')),
    (1996, ('Ronaldo', 'George Weah', 'Alan Shearer')),
    (1997, ('Ronaldo', 'Roberto Carlos', 'Dennis Bergkamp', 'Zinedine Zidane')),
    (1998, ('Zinedine Zidane', 'Ronaldo', 'Davor Šuker'),) ,
    (1999, ('Rivaldo', 'David Beckham', 'Gabriel Batistuta')),
    (2000, ('Zinedine Zidane', 'Luís Figo', 'Rivaldo')),
    (2001, ('Luís Figo', 'David Beckham', 'Raúl')),
    (2002, ('Ronaldo', 'Oliver Kahn', 'Zinedine Zidane')),
    (2003, ('Zinedine Zidane', 'Thierry Henry', 'Ronaldo')),
    (2004, ('Ronaldinho', 'Thierry Henry', 'Andriy Shevchenko')),
    (2005, ('Ronaldinho', 'Frank Lampard', 'Samuel Eto\'o')),
    (2006, ('Fabio Cannavaro', 'Zinedine Zidane', 'Ronaldinho')),
    (2007, ('Kaká', 'Lionel Messi', 'Cristiano Ronaldo')),
    (2008, ('Cristiano Ronaldo', 'Lionel Messi', 'Fernando Torres')),
    (2009, ('Lionel Messi', 'Cristiano Ronaldo', 'Xavi')),
    (2010, ('Lionel Messi', 'Andrés Iniesta', 'Xavi')),
]

# This is a list of the 125 greatest living players as chosen by
# Pele on FIFA's 100 year anniversary.
# cf. http://en.wikipedia.org/wiki/FIFA_100

fifa_100 = [
    'Gabriel Batistuta',
    'Hernán Crespo',
    'Alfredo di Stéfano',
    'Mario Kempes',
    'Diego Maradona',
    'Daniel Passarella',
    'Javier Saviola',
    'Omar Sivori',
    'Juan Sebastián Verón',
    'Javier Zanetti',
    ' Jan Ceulemans',
    'Jean-Marie Pfaff',
    'Franky Van der Elst',
    'Carlos Alberto',
    'Cafu',
    'Falcão',
    'Pelé',
    'Júnior',
    'Rivaldo',
    'Rivelino',
    'Roberto Carlos',
    'Romário',
    'Ronaldinho',
    'Ronaldo',
    'Djalma Santos',
    'Nílton Santos',
    'Sócrates',
    'Zico',
    'Hristo Stoichkov',
    'Roger Milla',
    'Elías Figueroa',
    'Iván Zamorano',
    'Carlos Valderrama',
    'Davor Šuker',
    'Josef Masopust',
    'Pavel Nedvěd',
    'Brian Laudrup',
    'Michael Laudrup',
    'Peter Schmeichel',
    'Gordon Banks',
    'David Beckham',
    'Bobby Charlton',
    'Kevin Keegan',
    'Gary Lineker',
    'Michael Owen',
    'Alan Shearer',
    'Éric Cantona',
    'Marcel Desailly',
    'Didier Deschamps',
    'Just Fontaine',
    'Thierry Henry',
    'Raymond Kopa',
    'Jean-Pierre Papin',
    'Robert Pirès',
    'Michel Platini',
    'Lilian Thuram',
    'Marius Trésor',
    'David Trezeguet',
    'Patrick Vieira',
    'Zinedine Zidane',
    'Michael Ballack',
    'Franz Beckenbauer',
    'Paul Breitner',
    'Oliver Kahn',
    'Jürgen Klinsmann',
    'Sepp Maier',
    'Lothar Matthäus',
    'Gerd Müller',
    'Karl-Heinz Rummenigge',
    'Uwe Seeler',
    'Abédi Pelé',
    'Ferenc Puskás',
    'Roy Keane',
    'Roberto Baggio',
    'Franco Baresi',
    'Giuseppe Bergomi',
    'Giampiero Boniperti',
    'Gianluigi Buffon',
    'Alessandro Del Piero',
    'Giacinto Facchetti',
    'Paolo Maldini',
    'Alessandro Nesta',
    'Gianni Rivera',
    'Paolo Rossi',
    'Francesco Totti',
    'Christian Vieri',
    'Dino Zoff',
    'Hidetoshi Nakata',
    'Hong Myung-Bo',
    'George Weah',
    'Hugo Sánchez',
    'Marco van Basten',
    'Dennis Bergkamp',
    'Johan Cruyff',
    'Edgar Davids',
    'Ruud Gullit',
    'René van de Kerkhof',
    'Willy van de Kerkhof',
    'Patrick Kluivert',
    'Johan Neeskens',
    'Ruud van Nistelrooy',
    'Rob Rensenbrink',
    'Frank Rijkaard',
    'Clarence Seedorf',
    'Jay-Jay Okocha',
    'George Best',
    'Romerito',
    'Teófilo Cubillas',
    'Zbigniew Boniek',
    'Eusébio',
    'Luís Figo',
    'Rui Costa',
    'Gheorghe Hagi',
    'Rinat Dasayev',
    'Kenny Dalglish',
    'El Hadji Diouf',
    'Emilio Butragueño',
    'Luis Enrique',
    'Raúl',
    'Rüştü Reçber',
    'Emre Belözoğlu',
    'Andriy Shevchenko',
    'Michelle Akers',
    'Mia Hamm',
    'Enzo Francescoli',
    ]

# This is a list of the 11 all-time best World Cup 
# players, chosen in 1994.

all_time_world_cup = [
    'Lev Yashin',
    'Djalma Santos',
    'Franz Beckenbauer',
    'Bobby Moore',
    'Paul Breitner',
    'Johan Cruyff',
    'Michel Platini',
    'Bobby Charlton',
    'Garrincha',
    'Ferenc Puskás',
    'Pelé'
    ]
