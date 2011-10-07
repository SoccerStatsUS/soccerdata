import datetime

transactions = [

    ('Bruce Arena', 'DC United', (1996, 1, 1), (1998, 10, 28)),
    ('Thomas Rongen', 'DC United', (1998, 12, 3), None),
    ('Ray Hudson', 'DC United', (2002, 1, 8), None),
    ('Peter Nowak', 'DC United', (2004, 1, 9), (2006, 12, 20)),
    ('Tom Soehn', 'DC United', (2006, 12, 22), None),
    ('Curt Onalfo', 'DC United', (2009, 12, 28), (2010, 8, 4)),
    ('Ben Olsen', 'DC United', (2010, 8, 4), None),

    ('Frank Stapleton', 'New England Revolution', (1996, 1, 1), (1996, 10, 4)),
    ('Thomas Rongen', 'New England Revolution', None, (1998, 8, 24)),
    ('Walter Zenga', 'New England Revolution', (1998, 10, 29), (1999, 9, 30)), # This seems wrong.
    ('Steve Nicol', 'New England Revolution', (1999, 9, 30), None),
    ('Frank Clavijo, ', 'New England Revolution', (1999, 11, 29), (2002, 5, 22)),
    ('Steve Nicol', 'New England Revolution', (2002, 5, 22), None),

    ('Eddie Firmani', 'New York Red Bulls', (1996, 1, 3), (1996, 5, 24)),
    ('Carlos Quieroz', 'New York Red Bulls', (1996, 5, 30), None),
    ('Carlos Albert Parreira', 'New York Red Bulls', (1996, 12, 30), (1997, 12, 11)),
    ('Alfonso Mondelo', 'New York Red Bulls', (1998, 1, 14), (1998, 9, 21)),
    ('Bora Milutinovic', 'New York Red Bulls', (1998, 9, 21), None),
    ('Octaivio Zambrano', 'New York Red Bulls', (1999, 11, 30), None),
    ('Bob Bradley', 'New York Red Bulls', (2002, 10, 21), (2005, 10, 4)), #approximately
    ('Mo Johnston', 'New York Red Bulls', (2005, 10, 4), (2006, 6, 27)),
    ('Richie Williams', 'New York Red Bulls', (2006, 6, 27), None),
    ('Bruce Arena', 'New York Red Bulls', (2006, 8, 11), (2007, 11, 5)), 
    ('Juan Carlos Osorio', 'New York Red Bulls', (2007, 12, 19), (2009, 8, 21)),
    ('Richie Williams', 'New York Red Bulls',(2009, 8, 21), None),
    ('Hans Backe', 'New York Red Bulls', (2010, 1, 7), None),

    ('Ron Newman', 'Sporting Kansas City', (1996, 1, 1), (1999, 4, 14)),
    ('Ken Fogarty', 'Sporting Kansas City', (1999, 4, 15), None),
    ('Bob Gansler', 'Sporting Kansas City', (1999, 4, 28), (2006, 7, 19)),
    ('Brian Bliss', 'Sporting Kansas City', (2006, 7, 19), None),
    ('Curt Onalfo', 'Sporting Kansas City', (2006, 11, 27), (2009, 8, 3)),
    ('Peter Vermes', 'Sporting Kansas City', (2009, 8, 4), None),

    ('Bob Houghton', 'Colorado Rapids', (1996, 1, 1), (1996, 9, 11)),
    ('Roy Wegerle', 'Colorado Rapids', (1996, 9, 12), None),
    ('Glenn Myernick', 'Colorado Rapids', (1996, 11, 19), None),
    ('Tim Hankinson', 'Colorado Rapids', (2000, 12, 21), None),
    ('Fernando Clavijo', 'Colorado Rapids', (2004, 12, 22), (2008, 8, 20)),
    ('Gary Smith', 'Colorado Rapids', None, None),

    ('Dave Dir', 'FC Dallas', (1996, 1, 1), (2000, 10, 20)),
    ('Mike Jeffries', 'FC Dallas', (2001, 1, 23), (2003, 9, 15)),
    ('Colin Clarke', 'FC Dallas', None, (2006, 11, 7)),
    ('Steve Morrow', 'FC Dallas', None, (2008, 5, 20)),
    ('Schellas Hyndman', 'FC Dallas', (2008, 6, 16), None),

    ('Timo Liekoski', 'Columbus Crew', (1995, 12, 5), (1996, 8, 3)),
    ('Tom Fitzgerald', 'Columbus Crew', None, (2001, 5, 18)),
    ('Greg Andrulis', 'Columbus Crew', None, (2005, 7, 12)),
    ('Robert Warzycha', 'Columbus Crew', (2005, 7, 12), None),
    ('Sigi Schmid', 'Columbus Crew', (2010, 10, 20), None),
    ('Robert Warzycha', 'Columbus Crew', (2008, 12, 22), None),

    ('Lothar Osiander', 'Los Angeles Galaxy', (1996, 1, 1), (1997, 6, 10)),
    ('Octavio Zambrano', 'Los Angeles Galaxy', (1997, 6, 10), None),
    ('Sigi Schmid', 'Los Angeles Galaxy', (1999, 4, 23), (2004, 8, 17)),
    ('Steve Sampson', 'Los Angeles Galaxy', (2004, 8, 18), (2006, 6, 6)),
    ('Frank Yallop', 'Los Angeles Galaxy', (2004, 8, 17), None),
    ('Ruud Gullit', 'Los Angeles Galaxy', (2007, 11, 8), (2008, 8, 11)),
    ('Cobi Jones', 'Los Angeles Galaxy', (2008, 8, 11), None),
    ('Bruce Arena', 'Los Angeles Galaxy', (2008, 8, 18), None),

    ('Laurie Calloway', 'San Jose Earthquakes', (1995, 12, 7), (1997, 6, 25)),
    ('Brian Quinn', 'San Jose Earthquakes', (1997, 6, 26), (1999, 9, 16)),
    ('Jorge Espinoza', 'San Jose Earthquakes', None, None),
    ('Lothar Osiander', 'San Jose Earthquakes', (1999, 9, 16), None),
    ('Frank Yallop', 'San Jose Earthquakes', (2001, 2, 2), (2003, 12, 26)),
    ('Dominic Kinnear', 'San Jose Earthquakes', (2004, 1, 8), (2005, 12, 15)), # Earthquakes stop existing
    ('Frank Yallop', 'San Jose Earthquakes', (2007, 11, 4), None),

    ('Thomas Rongen', 'Tampa Bay Mutiny', (1996, 1, 1), None),
    ('John Kowalski', 'Tampa Bay Mutiny', (1996, 11, 16), (1998, 6, 8)),
    ('Tim Hankinson', 'Tampa Bay Mutiny', (1998, 6, 8), (2000, 12, 18)),
    ('Alfonso Mondelo', 'Tampa Bay Mutiny', None, (2001, 7, 6)),
    ('Perry Van der Beck', 'Tampa Bay Mutiny', (2001, 7, 6), (2002, 1, 1)),

    ('Bob Bradley', 'Chicago Fire', (1998, 1, 1), None), 
    ('Dave Sarachan', 'Chicago Fire', (2002, 11, 6), (2007, 6, 20)), 
    ('Juan Carlos Osorio', 'Chicago Fire', (2007, 7, 5), (2007, 12, 10)),
    ('Denis Hamlett', 'Chicago Fire', (2008, 1, 11), (2009, 11, 24)), 
    ('Carlos de los Cobos', 'Chicago Fire', (2010, 1, 11), (2011, 5, 30)),
    ('Frank Klopas', 'Chicago Fire', (2011, 5, 30), None),

    ('Carlos Cordoba', 'Miami Fusion', (1998, 1, 1), None),
    ('Ivo Wortmann', 'Miami Fusion', (1998, 7, 26), None),
    ('Ray Hudson', 'Miami Fusion', (2000, 5, 9), (2002, 1, 1)),

    ('Thomas Rongen', 'Chivas USA', (2005, 1, 1), (2005, 5, 30)),
    ('Javier Ledesma', 'Chivas USA', (2005, 5, 30), None),
    ('Hans Westerhof', 'Chivas USA', (2005, 6, 3), None),
    ('Bob Bradley', 'Chivas USA', (2005, 11, 21), (2006, 11, 9)),
    ('Preki', 'Chivas USA', (2007, 1, 17), (2009, 11, 12)),
    ('Martin Vasquez', 'Chivas USA', (2009, 12, 2), (2010, 10, 27)),
    ('Robin Fraser', 'Chivas USA', (2011, 1, 4), None),

    ('John Ellinger', 'Real Salt Lake', (2005, 1, 1), (2007, 5, 3)), # estimate
    ('Jason Kreis', 'Real Salt Lake', (2007, 5, 3), None),

    ('Dominic Kinnear', 'Houston Dynamo', (2005, 12, 15), None),

    ('Mo Johnston', 'Toronto FC', (2006, 8, 22), (2008, 2, 1)),
    ('John Carver', 'Toronto FC', (2008, 2, 1), (2009, 4, 25)),
    ('Chris Cummins', 'Toronto FC', (2009, 4, 29), (2009, 10, 27)),
    ('Preki', 'Toronto FC', (2010, 1, 7), (2010, 9, 14)),
    ('Nick Dasovic', 'Toronto FC', (2010, 9, 14), None),
    ('Aron Winter', 'Toronto FC', (2011, 1, 6), None),

    ('Sigi Schmid', 'Seattle Sounders', (2008, 12, 17), None),

    ('Peter Nowak', 'Philadelphia Union', (2009, 5, 29), None),

    ('John Spencer', 'Portland Timbers', (2010, 8, 10), None),

    ('Teitur Thordarson', 'Vancouver Whitecaps', (2007, 12, 11), (2011, 5, 30)),
    ('Tom Soehn', 'Vancouver Whitecaps', (2011, 5, 30), None),

    ('Jesse Marsch', 'Montreal Impact', (2011, 8, 10), None),
]
