#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime


d = {
    'competition': 'Major League Soccer',
    'team_data': ['Supporters\' Shield',],
    'champion': 'Supporters\' Shield',


    'Supporters\' Shield': [
        (1996, 'Tampa Bay Mutiny'),
        (1997, 'D.C. United'),
        (1998, 'Los Angeles Galaxy'),
        (1999, 'D.C. United'),
        (2000, 'Kansas City Wizards'),
        (2001, 'Miami Fusion'),
        (2002, 'Los Angeles Galaxy'),
        (2003, 'Chicago Fire'),
        (2004, 'Columbus Crew'),
        (2005, 'San Jose Earthquakes'),
        (2006, 'D.C. United'),
        (2007, 'D.C. United'),
        (2008, 'Columbus Crew'),
        (2009, 'Columbus Crew'),
        (2010, 'Los Angeles Galaxy'),
        (2011, 'Los Angeles Galaxy'),
        ],


    'MVP': [
        (2010, 'David Ferreira'),
        (2009, 'Landon Donovan'),
        (2008, 'Guillermo Barros Schelotto'),
        (2007, 'Luciano Emilio'),
        (2006, 'Christian Gómez'),
        (2005, 'Taylor Twellman'),
        (2004, 'Amado Guevara'),
        (2003, 'Preki'),
        (2002, 'Carlos Ruíz'),
        (2001, 'Alex Pineda Chacón'),
        (2000, 'Tony Meola'),
        (1999, 'Jason Kreis'),
        (1998, 'Marco Etcheverry'),
        (1997, 'Preki'),
        (1996, 'Carlos Valderrama'),
        ],
    
    'Coach of the Year': [
        (1996, 'Thomas Rongen'),
        (1997, 'Bruce Arena'),
        (1998, 'Bob Bradley'),
        (1999, 'Sigi Schmid'),
        (2000, 'Bob Gansler'),
        (2001, 'Frank Yallop'),
        (2002, 'Steve Nicol'),
        (2003, 'Dave Sarachan'),
        (2004, 'Greg Andrulis'),
        (2005, 'Dominic Kinnear'),
        (2006, 'Bob Bradley'),
        (2007, 'Preki'),
        (2008, 'Sigi Schmid'),
        (2009, 'Bruce Arena'),
        (2010, 'Schellas Hyndman'),
        ],

    'Defender of the Year': [
        (1996, 'John Doyle'),
        (1997, 'Eddie Pope'),
        (1998, 'Lubos Kubik'),
        (1999, 'Robin Fraser'),
        (2000, 'Peter Vermes'),
        (2001, 'Jeff Agoos'),
        (2002, 'Carlos Bocanegra'),
        (2003, 'Carlos Bocanegra'),
        (2004, 'Robin Fraser'),
        (2005, 'Jimmy Conrad'),
        (2006, 'Bobby Boswell'),
        (2007, 'Michael Parkhurst'),
        (2008, 'Chad Marshall'),
        (2009, 'Chad Marshall'),
        (2010, 'Jámison Olave'),
        (2011, 'Omar Gonzalez'),
        ],

    'Rookie of the Year': [
        (1996, 'Steve Ralston'),
        (1997, 'Mike Duhaney'),
        (1998, 'Ben Olsen'),
        (1999, 'Jay Heaps'),
        (2000, 'Carlos Bocanegra'),
        (2001, 'Rodrigo Faria'),
        (2002, 'Kyle Martino'),
        (2003, 'Damani Ralph'),
        (2004, 'Clint Dempsey'),
        (2005, 'Michael Parkhurst'),
        (2006, 'Jonathan Bornstein'),
        (2007, 'Maurice Edu'),
        (2008, 'Sean Franklin'),
        (2009, 'Omar Gonzalez'),
        (2010, 'Andy Najar'),
        (2011, 'C.J. Sapong'),
        ],

    'Newcomer of the Year': [
        (2007, 'Luciano Emilio'),
        (2008, 'Darren Huckerby'),
        (2009, 'Fredy Montero'),
        (2010, 'Álvaro Saborío'),
        ],

    'Comeback Player of the Year': [
        (2000, 'Tony Meola'),
        (2001, 'Troy Dayak'),
        (2002, 'Chris Klein'),
        (2003, 'Chris Armas'),
        (2004, 'Brian Ching'),
        (2005, 'Chris Klein'),
        (2006, 'Richard Mulrooney'),
        (2007, 'Eddie Johnson'),
        (2008, 'Kenny Cooper'),
        (2009, 'Zach Thornton'),
        (2010, 'Bobby Convey'),
        ],

    'Fair Play Award': [
        (1997, 'Mark Chung'),
        (1998, 'Thomas Dooley'),
        (1999, 'Steve Ralston'),
        (2000, 'Steve Ralston'),
        (2001, 'Alex Pineda Chacon'),
        (2002, 'Mark Chung'),
        (2003, 'Brian McBride'),
        (2004, 'Eddie Pope'),
        (2005, 'Ronald Cerritos'),
        (2006, 'Chris Klein'),
        (2007, 'Michael Parkhurst'),
        (2008, 'Michael Parkhurst'),
        (2009, 'Steve Ralston'),
        (2010, 'Sebastien Le Toux'),
        (2011, 'Sebastien Le Toux'),
        ],

    'Humanitarian of the Year': [
        (1999, 'Eddie Pope'),
        (2000, 'Abdul Thompson Conteh'),
        (2001, 'Tim Howard'),
        (2002, 'Steve Jolley'),
        (2003, 'Ben Olsen'),
        (2004, 'Chris Henderson'),
        (2005, 'Brian Kamler'),
        (2006, 'Michael Parkhurst'),
        (2007, 'Diego Gutierrez'),
        (2008, 'Michael Parkhurst'),
        (2009, 'Jimmy Conrad'),
        (2009, 'Logan Pause'),
        (2010, 'Michael Lahoud'),
        ],



    'Best XI': [

        (1996, [
                'Mark Dodd',
                'Leonel Alvarez',
                'John Doyle',
                'Robin Fraser',
                'Mauricio Cienfuegos',
                'Roberto Donadoni',
                'Marco Etcheverry',
                'Preki',
                'Carlos Valderrama',
                'Eduardo Hurtado',
                'Roy Lassiter',
                ]),

        (1997, [
                'Brad Friedel',
                'Jeff Agoos',
                'Thomas Dooley',
                'Richard Gough',
                'Eddie Pope',
                'Mark Chung',
                'Marco Etcheverry',
                'Preki',
                'Carlos Valderrama', 
                'Ronald Cerritos',
                'Jaime Moreno',
                ]),

        (1998, [
                'Zach Thornton', 
                'Thomas Dooley',
                'Robin Fraser', 
                'Lubos Kubik',
                'Eddie Pope',
                'Chris Armas',
                'Mauricio Cienfuegos',
                'Marco Etcheverry',
                'Peter Nowak',
                'Stern John',
                'Cobi Jones',
                ]),

        (1999, [
                'Kevin Hartman',
                'Jeff Agoos',
                'Robin Fraser',
                'Lubos Kubik', 
                'Chris Armas',
                'Mauricio Cienfuegos',
                'Marco Etcheverry',
                'Eddie Lewis',
                'Steve Ralston',
                'Jaime Moreno',
                'Jason Kreis',
                ]),

        (2000, [
                'Tony Meola',
                'Robin Fraser',
                'Greg Vanney',
                'Peter Vermes',
                'Chris Armas',
                'Peter Nowak',
                'Steve Ralston',
                'Hristo Stoichkov',
                'Carlos Valderrama',
                'Mamadou Diallo', 
                'Clint Mathis',
                ]),

        (2001, [
                'Tim Howard',  
                'Jeff Agoos', 
                'Carlos Llamosa', 
                'Pablo Mastroeni', 
                'Greg Vanney', 
                'Chris Armas', 
                'Peter Nowak', 
                'Preki', 
                'Alex Pineda Chacon', 
                'Diego Serna', 
                'John Spencer', 
                ]),

        (2002, [
                'Tim Howard', 
                'Wade Barrett', 
                'Carlos Bocanegra', 
                'Alexi Lalas', 
                'Mark Chung', 
                'Ronnie Ekelund', 
                'Óscar Pareja', 
                'Steve Ralston',  
                'Jeff Cunningham', 
                'Carlos Ruiz', 
                'Taylor Twellman', 
                ]),

        (2003, [
                'Pat Onstad',  
                'Carlos Bocanegra', 
                'Ryan Nelsen', 
                'Eddie Pope',  
                'Chris Armas', 
                'DaMarcus Beasley', 
                'Mark Chung', 
                'Landon Donovan', 
                'Preki',  
                'John Spencer', 
                'Ante Razov', 
                ]),

        (2004, [
                'Joe Cannon',  
                'Jimmy Conrad', 
                'Robin Fraser', 
                'Ryan Nelsen', 
                'Eddie Pope',  
                'Eddie Gaven', 
                'Amado Guevara', 
                'Ronnie O\'Brien', 
                'Kerry Zavagnin', 
                'Brian Ching', 
                'Jaime Moreno', 
                ]),

        (2005,[
                'Pat Onstad',
                'Chris Albright',
                'Danny Califf',
                'Jimmy Conrad',  
                'Clint Dempsey', 
                'Dwayne De Rosario', 
                'Christian Gomez', 
                'Shalrie Joseph', 
                'Ronnie O\'Brien',  
                'Jaime Moreno', 
                'Taylor Twellman', 
                ]),

        (2006, [ 
                'Troy Perkins',  
                'Bobby Boswell', 
                'Jose Burciaga Jr.', 
                'Jimmy Conrad',  
                'Ricardo Clark', 
                'Clint Dempsey', 
                'Dwayne De Rosario', 
                'Christian Gomez', 
                'Justin Mapp',
                'Jeff Cunningham', 
                'Jaime Moreno', 
                ]),

        (2007, [
                'Brad Guzan', 
                'Jonathan Bornstein', 
                'Michael Parkhurst', 
                'Eddie Robinson',  
                'Guillermo Barros Schelotto', 
                'Dwayne De Rosario', 
                'Christian Gomez', 
                'Shalrie Joseph', 
                'Ben Olsen', 
                'Juan Pablo Angel', 
                'Luciano Emilio', 
                ]),

        (2008, [ 
                'Jon Busch',  
                'Jimmy Conrad', 
                'Bakary Soumare', 
                'Chad Marshall', 
                'Guillermo Barros Schelotto', 
                'Sacha Kljestan', 
                'Robbie Rogers', 
                'Shalrie Joseph', 
                'Cuauhtémoc Blanco',  
                'Landon Donovan', 
                'Kenny Cooper', 
                ]),

        (2009, [
                'Zach Thornton',  
                'Geoff Cameron', 
                'Wilman Conde', 
                'Chad Marshall',  
                'Shalrie Joseph', 
                'Landon Donovan', 
                'Stuart Holden', 
                'Freddie Ljungberg', 
                'Dwayne DeRosario',  
                'Conor Casey', 
                'Jeff Cunningham', 
                ]),

        (2010, [
                'Donovan Ricketts',  
                'Nat Borchers', 
                'Omar Gonzalez', 
                'Jámison Olave',  
                'Javier Morales', 
                'Sébastien Le Toux',
                'Landon Donovan', 
                'Dwayne De Rosario', 
                'David Ferreira',  
                'Edson Buddle', 
                'Chris Wondolowski', 
                ]),

        (2011, [
                'Kasey Keller',
                'Todd Dunivant',
                'Omar Gonzalez',
                'Jamison Olave',
                'David Beckham',
                'Brad Davis',
                'Dwayne De Rosario',
                'Landon Donovan',
                'Brek Shea',
                'Thierry Henry',
                'Chris Wondolowski',
                ]),
        ]
}

{
    'Goal of the Year': [
        (1996, 'Eric Wynalda', (4, 6, 1996)),
        (1997, 'Marco Etcheverry', (8, 27, 1997)),
        (1998, 'Brian McBride', (7, 9, 1998)),
        (1999, 'Marco Etcheverry', (5, 22, 1999)),
        (2000, 'Marcelo Balboa', (4, 22, 2000)),
        (2001, 'Clint Mathis', (4, 28, 2001), 'http://www.youtube.com/watch?v=lVsqiV2uKd0'),
        (2002, 'Carlos Ruiz', (6, 27, 2002)),
        (2003, 'Damani Ralph', (8, 13, 2002)),
        (2004, 'Dwayne De Rosario', (8, 2, 2004), 'http://www.youtube.com/watch?v=ZI0f6angcM0'),
        (2005, 'Dwayne De Rosario', (10, 15, 2005), 'http://www.youtube.com/watch?v=ML7Kh_Na3Tg'),
        (2006, 'Brian Ching', (9, 30, 2006), 'http://www.youtube.com/watch?v=JNZ75mGmiPY'),
        (2007, 'Cuauhtemoc Blanco', (8, 18, 2007), 'http://www.youtube.com/watch?v=NcfBSZbX22E'),
        (2008, 'Will Johnson', (10, 18, 2008), 'http://youtu.be/FxMWsEQprWI?t=28s'),
        (2009, 'Landon Donovan', (8, 8, 2009), 'http://www.youtube.com/watch?v=qnuPei0xyNs'),
        (2010, 'Marco Pappa', (4, 10, 2010), 'http://youtu.be/Ym_ZWti0bBo?t=2m36s'),
        ],
}

d2 = {
    'competition': 'MLS Cup Playoffs',
    'team_data': ['MLS Cup',],
    'champion': 'MLS Cup',


    'MLS Cup': [
        (1996, 'D.C. United'),
        (1997, 'D.C. United'),
        (1998, 'Chicago Fire'),
        (1999, 'D.C. United'),
        (2000, 'Kansas City Wizards'),
        (2001, 'San Jose Earthquakes'),
        (2002, 'Los Angeles Galaxy'),
        (2003, 'San Jose Earthquakes'),
        (2004, 'D.C. United'),
        (2005, 'Los Angeles Galaxy'),
        (2006, 'Houston Dynamo'),
        (2007, 'Houston Dynamo'),
        (2008, 'Columbus Crew'),
        (2009, 'Real Salt Lake'),
        (2010, 'Colorado Rapids'),
        ],

}
