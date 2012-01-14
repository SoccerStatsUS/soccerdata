#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# A second text processor for numerista's usa data.

import datetime
import os
import re

from soccerdata.alias import get_team, get_name
from soccerdata.cache import data_cache



PATH = '/home/chris/www/soccerdata/data/lineups/usapb.txt'


competition_map = {
    'fr': 'International Friendly',
    'wcq': 'World Cup Qualifier',
    'wcf': 'World Cup',
    'gc': 'Gold Cup',
    'ca': 'Copa America',
    'cc': 'Confederations Cup',
    }

name_map = {
    'T.Howard': 'Tim Howard',
    'S.Cherundolo': 'Steve Cherundolo',
    'C.Goodson': 'Clarence Goodson',
    'C.Bocanegra': 'Carlos Bocanegra',
    'T.Chandler': 'Timothy Chandler',
    'D.Williams': 'Danny Williams',
    'K.Beckerman': 'Kyle Beckerman',
    'J.Jones': 'Jermaine Jones',
    'M.Bradley': 'Michael Bradley',
    'R.Rogers': 'Robbie Rogers',
    'F.Johnson': 'Fabian Johnson',
    'B.Shea': 'Brek Shea',
    'C.Dempsey': 'Clint Dempsey',
    'E.Buddle': 'Edson Buddle',
    'M.Edu': 'Maurice Edu',
    'J.Altidore': 'Jozy Altidore',
    'N.Rimando': 'Nick Rimando',
    'S.Johnson': 'Sean Johnson',
    'S.Franklin': 'Sean Franklin',
    'T.Ream': 'Tim Ream',
    'O.Gonzalez': 'Omar Gonzalez',
    'M.Wynne': 'Marvell Wynne',
    'Z.Loyd': 'Zach Loyd',
    'A.Wallace': 'Anthony Wallace',
    'J.Larentowicz': 'Jeff Larentowicz',
    'D.McCarty': 'Dax McCarty',
    'A.Bedoya': 'Alejandro Bedoya',
    'E.Alexander': 'Eric Alexander',
    'M.Diskerud': 'Mikkel Diskerud',
    'J.Agudelo': 'Juan Agudelo',
    'C.Wondolowski': 'Chris Wondolowski',
    'T.Bunbury': 'Teal Bunbury',
    'T.Perkins': 'Troy Perkins',
    'J.Conrad': 'Jimmy Conrad',
    'C.Marshall': 'Chad Marshall',
    'H.Pearce': 'Heath Pearce',
    'J.Bornstein': 'Jonathan Bornstein',
    'S.Kljestan': 'Sacha Kljestan',
    'B.Feilhaber': 'Benny Feilhaber',
    'D.McCarty': 'Dax McCarty',
    'K.Beckerman': 'Kyle Beckerman',
    'Conor.Casey': 'Conor Casey',
    'R.Rogers': 'Robbie Rogers',
    'B.Davis': 'Brad Davis',
    'J.Cunningham': 'Jeff Cunningham',
    'R.Findley': 'Robbie Findley',
    'J.Walker': 'Jonny Walker',
    'C.Albright': 'Chris Albright',
    'F.Hejduk': 'Frankie Hejduk',
    'E.Pope': 'Eddie Pope',
    'N.Garcia': 'Nick Garcia',
    'B.Convey': 'Bobby Convey',
    'S.Ralston': 'Steve Ralston',
    'C.Klein': 'Chris Klein',
    'R.Mulrooney': 'Richard Mulrooney',
    'K.Zavagnin': 'Kerry Zavagnin',
    'C.Armas': 'Chris Armas',
    'J.Wolyniec': 'John Wolyniec',
    'D.Beasley': 'DaMarcus Beasley',
    'A.Razov': 'Ante Razov',
    'J.Wolff': 'Josh Wolff',
    'L.Donovan': 'Landon Donovan',
    'B.Friedel': 'Brad Friedel',
    'G.Berhalter': 'Gregg Berhalter',
    'T.Sanneh': 'Tony Sanneh',
    'P.Mastroeni': 'Pablo Mastroeni',
    'E.Stewart': 'Earnie Stewart',
    'E.Lewis': 'Eddie Lewis',
    'C.Reyna': 'Claudio Reyna',
    'C.Jones': 'Cobi Jones',
    'J.O\'Brien': 'John O\'Brien',
    'B.McBride': 'Brian McBride',
    'C.Mathis': 'Clint Mathis',
    'J.Agoos': 'Jeff Agoos',
    'C.Llamosa': 'Carlos Llamosa',
    'G.Vanney': 'Greg Vanney',
    'JM.Moore': 'Joe Max Moore',
    'C.Armas': 'Chris Armas',
    'R.Williams': 'Richie Williams',
    'J.Kirovski': 'Jovan Kirovski',
    'P.Radosavljevic': 'Preki',
    'T.Meola': 'Tony Meola',
    'R.Fraser': 'Robin Fraser',
    'CJ.Brown': 'C.J. Brown',
    'R.Lassiter': 'Roy Lassiter',
    'J.Douglas': 'Jimmy Douglas',
    'A.Wood': 'Alexander Wood',
    'G.Moorhouse': 'George Moorhouse',
    'J.Gallagher': 'James Gallagher',
    'R.Tracey': 'Raphael Tracy',
    'J.Brown': 'James Brown',
    'B.Gonsalves': 'Billy Gonsalves',
    'T.Florie': 'Tom Florie',
    'B.Patenaude': 'Bert Patenaude',
    'A.Auld': 'Andy Auld',
    'B.McGhee': 'Bart McGhee',
'F.Borghi': 'Frank Borghi',
'H.Keough': 'Harry Keough',
 'J.Maca': 'Joe Maca',
'E.McIlvenny': 'Ed McIlvenny',
'C.Colombo': 'Charlie Colombo',
'W.Bahr': 'Walter Bahr',
'F.Wallace': 'Frank Wallace',
'G.Pariani': 'Gino Pariani',
'J.Gaetjens': 'Joe Gaetjens',
'J.Souza': 'John Souza',
'E.Souza': 'Ed Souza',

'A.Mausser': 'Arnie Mausser',
'B.Rudroff': 'Bruce Rudroff',
'T.McAlister': 'Jim McAlister',
'G.Myernick': 'Glenn Myernick',
'G.Makowski': 'Greg Makowski',
'R.Davis': 'Ricky Davis',
'M.Liveric': 'Mark Liveric',
'G.Nanchoff': 'George Nanchoff',
'T.Keough': 'Ty Keough',
'A.DiBernardo': 'Angelo DiBernardo',
'G.Etherington': 'Gary Etherington',
'D.Wit': 'Dennis Wit',
'L.Hulcer': 'Larry Hulcer',
'C.Fowles': 'Colin Fowles',
'B.Bandov': 'Boris Bandov',

'W.DuBose': 'Winston DuBose',
'Tim.Twellman': 'Tim Twellman',
'D.Spalding': 'Dick Spalding',
'T.Crudo': 'Tony Crudo',
'T.O\'Hara': 'Tom O\'Hara',
'J.Lignos': 'John Lignos',
'R.Cantillo': 'Ringo Cantillo',
'C.Fajkus': 'Charlie Fajkus',
'H.Borja': 'Chico Borja',
'J.Veee': 'Juli Veee',
'N.Pesa': 'Njego Pesa',
'S.Moyers': 'Steve Moyers',

'D.Vanole': 'David Vanole',
'P.Krumpe': 'Paul Krumpe',
'P.Caligiuri': 'Paul Caligiuri',
'J.Banks': 'Jimmy Banks',
'M.Windischmann': 'Mike Windischmann',
'S.Sengelmann': 'Steve Sengelmann',
'J.Stollmeyer': 'John Stollmeyer',
'E.Eichmann': 'Eric Eichmann',
'E.Biefeld': 'Eric Biefeld',
'T.Kain': 'Tom Kain',
'B.Goulet': 'Brent Goulet',
'S.Gjonbalaj': 'Sadri Gjonbalaj',
'T.Silvas': 'Tom Silvas',

'S.Fuchs': 'Steve Fuchs',
'B.James': 'Bernie James',
'N.Megson': 'Neil Megson',
'A.Velazco': 'Arturo Velazco',
'M.Balboa': 'Marcelo Balboa',
'J.Doyle': 'John Doyle',
'K.Grimes': 'Kevin Grimes',
'B.Murray': 'Bruce Murray',
'C.Sullivan': 'Chris Sullivan',
'M.Fox': 'Mike Fox',
'J.Gabarra': 'Jim Gabarra',
'G.Pastor': 'George Pastor',
'J.Kirk': 'Joey Kirk',

'M.Dodd': 'Mark Dodd',
'J.Kirk': 'Joey Kirk',
'D.Cogsville': 'Donald Cogsville',
'G.Pastor': 'George Pastor',

'I.Feuer': 'Ian Feuer',
'J.Michallik': 'Janusz Michallik',
'B.Savage': 'Bruce Savage',
'B.Quinn': 'Brian Quinn',
'J.Acosta': 'Jorge Acosta',
'J.DeBrito': 'John DeBrito',
'M.Sorber': 'Mike Sorber',
'D.Kinnear': 'Dominic Kinnear',
'H.Perez': 'Hugo Perez',
'Z.Ibsen': 'Zak Ibsen',

'M.Burns': 'Mike Burns',
'G.Villa': 'Greg Villa',
'A.Auld': 'Andy Auld',
'H.Gomez': 'Herculez Gomez',
'N.Clarke': 'Neil Clarke',
'G.Thompson': 'Gregg Thompson',

    'B.Looby': 'Bill Looby',
    'B.McLaughlin': 'Benny McLaughlin',
    'J.Ferguson': 'Jock Ferguson',
    'D.Ficken': 'Dieter Ficken',
    'D.Regis': 'David Regis',
    'J.Ladouceur': 'Jacques LaDouceur',
    'A.Cziotka': 'Andy Cziotka',
    'R.Wild': 'Richard Wild',
    'A.Lalas': 'Alexi Lalas',
    'G.Geimer': 'Gene Geimer',
    'T.Ferrans': 'Thomson Ferrans',
    'H.Koffler': 'Helmut Kofler',
    'O.Onyewu': 'Oguchi Onyewu',
    'S.Holden': 'Stuart Holden',
    'HJA.Smith': 'Harry Smith',
    'R.Wegerle': 'Roy Wegerle',
    'E.Georges': 'Emmanuel Georges',
    'M.Flater': 'Mike Flater',
    'A.Zerhusen': 'Al Zerhusen',
    'B.Bliss': 'Brian Bliss',
    'J.Sommer': 'Juergen Sommer',
    'D.Brown': 'Davey Brown',
    'P.Vermes': 'Peter Vermes',
    'B.Ching': 'Brian Ching',
    'T.Dayak': 'Troy Dayak',
    'J.Kreis': 'Jason Kreis',
    'D.Moor': 'Drew Moor',
    'M.Lapper': 'Mike Lapper',
    'D.Califf': 'Danny Califf',
    'D.Szetela': 'Danny Szetela',
    'Z.Thornton': 'Zach Thornton',
    'T.Dooley': 'Thomas Dooley',
    'M.Kmosko': 'Matt Kmosko',
    'S.Trittschuh': 'Steve Trittschuh',
    'T.Ramos': 'Tab Ramos',
    'D.Brose': 'Dario Brose',
    'D.Calichman': 'Dan Calichman',
    'B.Guzan': 'Brad Guzan',
    'B.Gansler': 'Bob Gansler',
    'F.Klopas': 'Frank Klopas',
    'R.Clark': 'Ricardo Clark',
    'S.Quaranta': 'Santino Quaranta',
    'K.Hartman': 'Kevin Hartman',
    'B.Olsen': 'Ben Olsen',
    'C.Fry': 'Chance Fry',
    'M.Chung': 'Mark Chung',
    'F.Clavijo': 'Fernando Clavijo',
    'B.Maisonneuve': 'Brian Maisonneuve',
    'F.Adu': 'Freddy Adu',
    'B.Carroll': 'Brian Carroll',
    'D.Gutierrez': 'Diego Gutierrez',
    'N.Borchers': 'Nat Borchers',
    'J.Harkes': 'John Harkes',
    'Tay.Twellman': 'Taylor Twellman',
    'C.Gibbs': 'Corey Gibbs',
    'E.Johnson': 'Edward Johnson',
    'K.Keller': 'Kasey Keller',
    'D.Wagner': 'David Wagner',
    'M.Mason': 'Michael Mason',
    'M.Santel': 'Mark Santel',
    'M.Vasquez': 'Martin Vasquez',
    'F.Ryan': 'Francis Ryan',
    'A.Maca': 'Alain Maca',
    'R.Roberts': 'Richard Roberts',
    'S.Pecher': 'Steve Pecher',
    'A.Roboostoff': 'Archie Roboostoff',
    'A.Wolanow': 'Abbie Wolanow',
    'B.Barto': 'Barry Barto',
    'M.Martin': 'Manuel Martin',
    'F.Cameron': 'Fred Cameron',
    'G.Rensing': 'Gary Rensing',
    'J.Travis': 'John Travis',
    'P.VanderBeck': 'Perry Van der Beck',
    'M.Hahnemann': 'Marcus Hahnemann',
    'E.Hart': 'Edward Hart',
    'E.Kapp': 'Erhardt Kapp',
    'D.Armstrong': 'Desmond Armstrong',
    'W.McLean': 'Willie McLean',
    'D.Brcic': 'David Brcic',
    'A.Mihailovich': 'Ane Mihailovich',
    'T.Murray': 'Thomas Murray',
    'J.Currie': 'John Currie',
    'R.Ryerson': 'Rob Ryerson',
    'C.Horvath': 'Charles Horvath',
    'R.Getzinger': 'Rudy Getzinger',
    'C.Rafael': 'Charlie Raphael',
    'J.Askew': 'Sonny Askew',
    'T.Swords': 'Thomas Swords',
    'G.Grabowski': 'Gene Grabowski',
    'J.DeMerit': 'Jay DeMerit',
    'W.Roth': 'Werner Roth',
    'A.Straden': 'Andy Straden',
    'L.Lozzano': 'Lawrence Lozzano',
    'M.Lagos': 'Manny Lagos',
    'A.Ely': 'Alex Ely',
    'B.Rigby': 'Bob Rigby',
    'J.Harbor': 'Jean Harbor',
    'C.Kooiman': 'Cle Kooiman',
    'B.Smith': 'Bobby Smith',
    'J.Benitez': 'Jorge Benitez',
    'M.Winter': 'Mike Winter',
    'J.Heaps': 'Jay Heaps',
    'B.Demling': 'Buzz Demling',
    'J.Torres': 'José Francisco Torres',
    'R.Decker': 'Rolf Decker',
    'C.Moore': 'Cecil Moore',
    'M.Goldie': 'Malcolm Goldie',
    'T.McFarlane': 'Tommy McFarlane',
    'E.Murphy': 'Ed Murphy',
    'N.Krat': 'Nick Krat',
    'W.Barrett': 'Wade Barrett',
    'J.Servin': 'Julio Servin',
    'H.Liotart': 'Hank Liotart',
    'R.Kotschau': 'Ritchie Kotschau',
    'D.Armstrong': 'Desmond Armstrong',
    'J.O\'Connell': 'John O\'Connell',
    'J.RegoCosta': 'Joseph Rego-Costa',
    'I.Mitic': 'Ilija Mitic',
    'S.Victorine': 'Sasha Victorine',
    'R.Corrales': 'Ramiro Corrales',
    'W.Herd': 'Willie Herd',
    'G.Baker': 'Gerry Baker',
    'L.Martin': 'Lucas Martin',
    'T.Donlic': 'Tony Donlic',
    'S.Cronin': 'Sam Cronin',
    'R.Mendoza': 'Ruben Mendoza',
    'F.Pereira': 'Fred Pereira',
    'A.Rudd': 'Arthur Rudd',
    'H.Cooper': 'Harry Cooper',
    'Z.Stritzl': 'Siegfried Stritzl',
    'M.Renshaw': 'Mike Renshaw',
    'B.Deszofi': 'Bill Deszofi',
    'T.Ianni': 'Tayt Ianni',
    'W.Mata': 'Werner Mata',
    'Jo.Moore': 'Johnny Moore',
    'R.Gormley': 'Bob Gormley',
    'L.Monsen': 'Lloyd Monsen',
    'R.Hamilton': 'Raymond Hamilton',
    'I.Davis': 'Irving Davis',
    'T.Martin': 'Tim Martin',
    'D.D\'Errico': 'Dave D\'Errico',
    'H.Rick': 'Horst Rick',
    'J.Kelly': 'James Kelly',
    'J.Krische': 'Joseph Krische',
    'J.Best': 'John Best',
    'M.Joseph': 'Miles Joseph',
    'S.Djordjevic': 'Barney Djordjevic',
    'A.Bachmeier': 'Adolph Bachmeier',
    'W.Sheppell': 'Bill Sheppell',
    'L.Hausemann': 'Larry Hausmann',
    'W.Chyzowych': 'Walter Chyzowych',
    'N.Covone': 'Neil Covone',
    'H.Noga': 'Henry Noga',
    'J.Hooker': 'Jeff Hooker',
    'A.Marina': 'Alfonso Marina',
    'S.Pittman': 'Steve Pittman',
    'J.Murphy': 'James Murphy',
    'E.Valentine': 'Ed Valentine',
    'J.Duback': 'Jeff Duback',
    'J.Kerr': 'John Kerr',
    'J.Diffley': 'John Diffley',
    'J.Deal': 'John Deal',
    'A.Cooper': 'Albert Cooper',
    'J.Benedek': 'Jim Benedek',
    'A.Trost': 'Al Trost',
    'J.Fink': 'Joey Fink',
    'H.Farrell': 'Harry Farrell',
    'W.Eppy': 'Bill Eppy',
    'D.Vaninger': 'Denny Vaninger',
    'A.Rymarczuk': 'Andy Rymarczuk',
    'A.Martinich': 'Art Martinich',
    'T.Bellinger': 'Tony Bellinger',
    'R.Milne': 'Ray Milne',
    'A.Coker': 'Ade Coker',
    'A.Bachmeier': 'Adolph Bachmeier',
    'M.Collins': 'Michael Collins',
    'E.Gaven': 'Eddie Gaven',
    'W.Roy': 'Willy Roy',
    'C.Kreiger': 'Cornell Krieger',
    'C.Rolfe': 'Chris Rolfe',
    'K.Martino': 'Kyle Martino',
    'W.Lehman': 'William Lehmann',
    'F.Moniz': 'Frank Moniz',
    'H.Margenson': 'Henry Margenson',
    'C.Gentile': 'Carl Gentile',
    'A.Rodriguez': 'Angel Rodrigues',
    'J.Robertson': 'James Robertson',
    'J.Siega': 'Jorge Siega',
    'JP.Traina': 'John Peter Traina',
    'E.Hawkins': 'Eddie Hawkins',
    'M.Seissler': 'Manfred Seissler',
    'P.McBride': 'Pat McBride',
    'C.Deering': 'Chad Deering',
    'O.Banach': 'Orest Banach',
    'T.Resznecki': 'Tibor Resznecki',
    'M.Orozco': 'Michael Orozco',
    'A.Stark': 'Archie Stark',
    'E.Robinson': 'Eddie Robinson',
    'J.McGuire': 'Johnny McGuire',
    'E.Petramale': 'Eugene Petramale',
    'J.Spector': 'Jonathan Spector',
    'M.McKeon': 'Matt McKeon',
    'B.Kehoe': 'Bob Kehoe',
    'K.Rote': 'Kyle Rote Jr.',
    'W.Findlay': 'William Findlay',
    'D.Droege': 'Don Droege',
    'C.Henderson': 'Chris Henderson',
    'D.Counce': 'Dan Counce',
    'F.Kovacs': 'Fred Kovacs',
    'S.Sharp': 'Steve Sharp',
    'K.Crow': 'Kevin Crow',
    'J.Thorrington': 'John Thorrington',
    'T.Hantak': 'Ted Hantak',
    'A.Donelli': 'Aldo Donelli',
    'K.Finn': 'Kenny Finn',
    'E.Cook': 'Elwood Cook',
    'O.Banach': 'Orest Banach',
    'W.Romanowicz': 'Walter Romanowicz',
    'H.Meyerdierks': 'Henry Meyerdierks',
    'E.Wynalda': 'Eric Wynalda',
    'L.Pause': 'Logan Pause',
    'P.Noonan': 'Pat Noonan',
    'A.Parkinson': 'Andrew Parkinson',
    'D.McMillan': 'Doug McMillan',
    'W.Shmotolocha': 'Walt Schmotolocha',
    'E.Kelly': 'Ed Kelly',
    'D.Canter': 'Dan Canter',
    'I.Borodiak': 'Ivan Borodiak',
    'D.Arnaud': 'Davy Arnaud',
    'T.Stark': 'Tommy Stark',
    'R.Volz': 'Ray Voltz',
    'P.Garcia': 'Poli Garcia',
    'C.Smith': 'Clarence Smith',
    'K.Cooper': 'Kenny Cooper',
    'M.Reis': 'Matt Reis',
    'B.Mullan': 'Brian Mullan',
    'K.Snow': 'Ken Snow',
    'D.Washington': 'Dante Washington',
    'M.Slivinski': 'Mike Slivinski',
    'T.Eck': 'Ted Eck',
    'M.Petke': 'Mike Petke',
    'F.Grgurev': 'Fred Grgurev',
    'M.Parkhurst': 'Michael Parkhurst',
    'W.Bertani': 'Bill Bertani',
    'R.Suarez': 'Ryan Suarez',
    'D.Farquhar': 'Doug Farquhar',
    'L.Nanchoff': 'Louis Nanchoff',
    'E.Lichaj': 'Eric Lichaj',
    'L.Yacopec': 'Lou Yakopec',
    'A.Wolanin': 'Adam Wolanin',
    'Brad.Evans': 'Brad Evans',
    'C.Davies': 'Charlie Davies',

}


location_map = {
    'Berlin, E.Germany': 'Berlin, East Germany',
    'Bloemfontein, SouthAfrica': 'Bloemfontein, South Africa',
    'CapeTown, SouthAfrica': 'Cape Town, South Africa',
    'CommerceCity, CO': 'Commerce City, CO',
    'E.Hartford, CT': 'East Hartford, CT',
    'E.Rutherford, NJ': 'East Rutherford, NJ',
    'EastHartford, CT': 'East Hartford, CT',
    'Foxboro, MA': 'Foxborough, MA',
    'Ft.Lauderdale, FL': 'Fort Lauderdale, FL',
    'Ft.Worth, TX': 'Fort Worth, TX',
    'Johannesburg, SouthAfrica': 'Johannesburg, South Africa',
    'KansasCity, KS': 'Kansas City, KS',
    'LosAngeles, CA': 'Los Angeles, CA',
    'MexicoCity, Mexico': 'Mexico City, Mexico',
    'MiamiGardens, FL': 'Miami Gardens, FL',
    'Phlladelphia, PA': 'Philadelphia, PA',
    'PortauPrince, Haiti': 'Port au Prince, Haiti',
    'Pretoria, SouthAfrica': 'Pretoria, South Africa',
    'RiodeJaneiro, Brazil': 'Rio de Janeiro, Brazil',
    'Roodeport, SouthAfrica': 'Roodeport, South Africa',
    'Rustenberg, SouthAfrica': 'Rustenburg, South Africa',
    'Rustenburg, SouthAfrica': 'Rustenburg, South Africa',
    'San Jose, CR': 'San Jose, Costa Rica',
    'SanDiego, CA': 'San Diego, CA',
    'SanFrancisco, CA': 'San Francisco, CA',
    'SanJose, CA': 'San Jose, CA',
    'SanJose, Costa Rica': 'San Jose, Costa Rica',
    'St Etienne, France': 'Saint-Étienne, France',
    'St.Gallen, Switzerland': 'St. Gallen, Switzerland',
    'St.George, Grenada': 'St. George, Grenada',
    'St.John\'s, Canada': 'St. John\'s, Canada',
    'St.Louis, MO': 'St. Louis, MO',
    'Washington, D.C': 'Washington, D.C.',
    'Washington, DC': 'Washington, D.C.',
}
    

class TextProcessor(object):
    
    def __init__(self):
        self.year = None
        self.date = None
        self.competition = None
        
        self.games = []
        self.goals = []
        self.lineups = []


    def process_row(self, row):
        commas = row.count(',')
        
        if commas == 0:
            if not row.strip():
                return
            else:
                try:
                    self.year = int(row)
                except:
                    import pdb; pdb.set_trace()


        elif commas == 2:
            fields = [e.strip() for e in row.split('  ')] # 2 spaces
            fields = [e for e in fields if e] # Remove empty fields.

            try:
                assert len(fields) == 5
            except:
                print row
                return

            monthday, opponent, location, result, competition = fields

            # Set the date correctly.
            ds = "%s %s" % (monthday, self.year)
            d = datetime.datetime.strptime(ds, "%b %d %Y")
            self.date = d
            
            wl, score = result.split(",")

            # Fixme. This is just to ignore 3-2(og) style scores.
            if "(" in score:
                score = score.split("(")[0]
            us_score, opponent_score = [int(e) for e in score.split('-')]

            # Map the competition abbreviation
            self.competition = competition_map[competition]

            city, other = location.split(",") # other can be a country or a state.
            ls = "%s, %s" % (city, other)
            l = location_map.get(ls, ls)

            # Match states like TX or CA. Anything else is (hopefully) in another country.
            # Haven't verified.
            if len(other) == 2 and other.upper() == other: 
                home_team = 'United States'
                home_score = us_score
                away_team = opponent
                away_score = opponent_score
            else:
                away_team = 'United States'
                away_score = us_score
                home_team = opponent
                home_score = opponent_score
                            
            self.games.append({
                    'home_team': home_team,
                    'away_team': away_team,
                    'home_score': home_score,
                    'away_score': away_score,
                    'location': l,
                    'date': self.date,
                    'competition': self.competition,
                    'season': self.date.year,
                    })

        else:
            if commas > 10: print row
            # Process lineup

            player_strings = row.split(',')
            
            # Need to do a lot more processing for this.
            for ps in player_strings:
                if '(' not in ps:
                    starter, subs = ps, []
                else:
                    starter, subs = ps.split('(')
                    subs = subs.replace(')', '').split(';')

                if len(subs) == 0:
                    self.process_single_player(starter, 0, 90)
                elif len(subs) == 1:
                    self.process_single_player(starter, 0, '?')
                    self.process_single_player(subs[0], '?', 90)
                elif len(subs) == 2:
                    self.process_single_player(starter, 0, '?')
                    self.process_single_player(subs[0], '?', '?')
                    self.process_single_player(subs[1], '?', 90)
                else:
                    raise


    def process_single_player(self, item, on, off):
        if '-' in item:
            name, goals = [e.strip() for e in item.split('-')]
            goals = int(goals)
        else:
            name, goals = item.strip(), 0

        for goal in range(goals):
            self.goals.append({
                    'goal': name_map.get(name, name),
                    'minute': None,
                    'date': self.date,
                    'team': 'United States',
                    'season': self.date.year,
                    'competition': self.competition,
                    'assists': [],
                    })

        
        self.lineups.append({
                'name': name_map.get(name, name),
                'on': on,
                'off': off,
                'team': 'United States',
                'date': self.date,
                'season': self.date.year,
                'competition': self.competition,
                })


def process_usa():
    f = open(PATH)
    tp = TextProcessor()
    for line in f:
        tp.process_row(line)
    return tp

def process_usa_games():
    return process_usa().games

def process_usa_goals():
    return process_usa().goals

def process_usa_lineups():
    return process_usa().lineups    
            
            


if __name__ == "__main__":
    print process_usa_lineups()
            
