#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime


d = {
    'competition': 'Liga MX',
    'champion': 'Champion',
    'team_data': ['Champion',],


    'Champion': [
        ('1943-1944', 'CF Asturias'),
        ('1944-1945', 'Real Club Espana'),
        ('1945-1946', 'Veracruz'),
        ('1946-1947', 'Atlante'),
        ('1947-1948', 'Leon'),
        ('1948-1949', 'Leon'),
        ('1949-1950', 'Veracruz'),
        ('1950-1951', 'Atlas'),
        ('1951-1952', 'Leon'),
        ('1952-1953', 'Tampico Madero'),
        ('1953-1954', 'Marte (Mexico)'),
        ('1954-1955', 'Zacatepec'),
        ('1955-1956', 'Leon'),
        ('1956-1957', 'Guadalajara'),
        ('1957-1958', 'Zacatepec'),
        ('1958-1959', 'Guadalajara'),
        ('1959-1960', 'Guadalajara'),
        ('1960-1961', 'Guadalajara'),
        ('1961-1962', 'Guadalajara'),
        ('1962-1963', 'Oro'),
        ('1963-1964', 'Guadalajara'),
        ('1964-1965', 'Guadalajara'),
        ('1965-1966', 'Club America'),
        ('1966-1967', 'Toluca'),
        ('1967-1968', 'Toluca'),
        ('1968-1969', 'Cruz Azul'),
        ('1969-1970', 'Guadalajara'),
        ('1970-1971', 'Club America'),
        ('1971-1972', 'Cruz Azul'),
        ('1972-1973', 'Cruz Azul'),
        ('1973-1974', 'Cruz Azul'),
        ('1974-1975', 'Toluca'),
        ('1975-1976', 'Club America'),
        ('1976-1977', 'UNAM'),
        ('1977-1978', 'UANL'),
        ('1978-1979', 'Cruz Azul'),
        ('1979-1980', 'Cruz Azul'),
        ('1980-1981', 'UNAM'),
        ('1981-1982', 'UANL'),
        ('1982-1983', 'Puebla'),
        ('1983-1984', 'Club America'),
        ('1984-1985', 'Club America'),
        ('1985 Prode', 'Club America'),
        ('1986-1987', 'Guadalajara'),
        ('1986 Mexico', 'Monterrey'),
        ('1987-1988', 'Club America'),
        ('1988-1989', 'Club America'),
        ('1989-1990', 'Puebla'),
        ('1990-1991', 'UNAM'),
        ('1991-1992', 'Leon'),
        ('1992-1993', 'Atlante'),
        ('1993-1994', 'Tecos'),
        ('1994-1995', 'Necaxa'),
        ('1995-1996', 'Necaxa'),
        ('1996 Apertura', 'Santos Laguna'),
        ('1997 Clausura', 'CD Guadalajara'),
        ('1997 Apertura', 'Cruz Azul'),
        ('1998 Clausura', 'Toluca'),
        ('1998 Apertura', 'Necaxa'),
        ('1999 Clausura', 'Toluca'),
        ('1999 Apertura', 'Pachuca'),
        ('2000 Clausura', 'Toluca'),
        ('2000 Apertura', 'Monarcas Morelia'),
        ('2001 Clausura', 'Santos Laguna'),
        ('2001 Apertura', 'Pachuca'),
        ('2002 Clausura', 'Club America'),
        ('2002 Apertura', 'Toluca'),
        ('2003 Clausura', 'CF Monterrey'),
        ('2003 Apertura', 'Pachuca'),
        ('2004 Clausura', 'UNAM'),
        ('2004 Apertura', 'UNAM'),
        ('2005 Clausura', 'Club America'),
        ('2005 Apertura', 'Toluca'),
        ('2006 Clausura', 'Pachuca'),
        ('2006 Apertura', 'CD Guadalajara'),
        ('2007 Clausura', 'Pachuca'),
        ('2007 Apertura', 'Guadalajara'),
        ('2008 Clausura', 'Pachuca'),
        ('2008 Apertura', 'Atlante'),
        ('2009 Clausura', 'Santos Laguna'),
        ('2009 Apertura', 'Toluca'),
        ('2010 Clausura', 'UNAM'),
        ('2010 Apertura', 'CF Monterrey'),
        ('2011 Clausura', 'UNAM'),
        ('2011 Apertura', 'UANL Tigres'),
        ('2012 Clausura', 'Santos Laguna'),
        ('2012 Apertura', 'Tijuana'),

        ],

    
    'Golden Boot': [
        ('1943-1944', 'Isidro Langara'),
        ('1944-1945', 'Roberto Aballay'),
        ('1945-1946', 'Isidro Langara'),
        ('1946-1947', 'Adalberto Lopez'),
        ('1947-1948', 'Adalberto Lopez'),
        ('1948-1949', 'Adalberto Lopez'),
        ('1949-1950', 'Julio Ayllon'),
        ('1950-1951', 'Horacio Casarin'),
        ('1951-1952', 'Adalberto Lopez'),
        ('1952-1953', 'Julio Quinones'),
        ('1953-1954', 'Juan Carlos Carrera'),
        ('1953-1954', 'Adalberto Lopez'),
        ('1953-1954', 'Julio M. Pallerio'),
        ('1954-1955', 'Julio M. Pallerio'),
        ('1955-1956', 'Hector Hernandez'),
        ('1956-1957', 'Crescencio Gutierrez'),
        ('1957-1958', 'Carlos Lara'),
        ('1958-1959', 'Eduardo Gonzalez Palmer'),
        ('1959-1960', 'Roberto Rolando'),
        ('1960-1961', 'Carlos Lara'),
        ('1961-1962', 'Salvador Reyes'),
        ('1961-1962', 'Carlos Lara'),
        ('1962-1963', 'Amaury Epaminondas'),
        ('1963-1964', 'Carlos Alberto Etcheverry'),
        ('1964-1965', 'Amaury Epaminondas'),
        ('1965-1966', 'Jose Alves'),
        ('1966-1967', 'Amaury Epaminondas'),
        ('1967-1968', 'Bernardo Hernandez'),
        ('1968-1969', 'Luis Estrada'),
        ('1969-1970', 'Vicente Pereda'),
        ('1970 Mexico', 'Sergio Anaya'),
        ('1970-1971', 'Enrique Borja'),
        ('1971-1972', 'Enrique Borja'),
        ('1972-1973', 'Enrique Borja'),
        ('1973-1974', 'Osvaldo Castro'),
        ('1974-1975', 'Horacio Lopez Salgado'),
        ('1975-1976', 'Evanivaldo Castro'),
        ('1976-1977', 'Evanivaldo Castro'),
        ('1977-1978', 'Evanivaldo Castro'),
        ('1978-1979', 'Evanivaldo Castro'),
        ('1978-1979', 'Evanivaldo Castro'),
        ('1978-1979', 'Hugo Sanchez'),
        ('1980-1981', 'Evanivaldo Castro'),
        ('1981-1982', 'Evanivaldo Castro'),
        ('1982-1983', 'Norberto Outes'),
        ('1983-1984', 'Norberto Outes'),
        ('1984-1985', 'Evanivaldo Castro'),
        ('1985 Prode', 'Sergio Lira'),
        ('1986-1987', 'Jose Luis Zalazar'),
        ('1986 Mexico', 'Sergio Lira'),
        ('1986 Mexico', 'Francisco Cruz'),
        ('1987-1988', 'Luis Flores'),
        ('1988-1989', 'Sergio Lira'),
        ('1989-1990', 'Jorge Comas'),
        ('1990-1991', 'Luis Garcia'),
        ('1991-1992', 'Luis Garcia'),
        ('1992-1993', 'Ivo Basay'),
        ('1993-1994', 'Carlos Hermosillo'),
        ('1994-1995', 'Carlos Hermosillo'),
        ('1995-1996', 'Carlos Hermosillo'),
        ('1996 Apertura', 'Carlos Munoz'),
        ('1997 Clausura', 'Lorenzo Saez'),
        ('1997 Apertura', 'Luis Garcia Postigo'),
        ('1998 Clausura', 'Jose Cardozo'),
        ('1998 Apertura', 'Cuauhtemoc Blanco'),
        ('1999 Clausura', 'Jose Cardozo'),
        ('1999 Apertura', 'Jesus Olalde'),
        ('2000 Clausura', 'Everaldo Begines'),
        ('2000 Clausura', 'Sebastian Abreu'),
        ('2000 Clausura', 'Agustin Delgado'),
        ('2000 Apertura', 'Jared Borgetti'),
        ('2001 Clausura', 'Jared Borgetti'),
        ('2001 Apertura', 'Martin Rodriguez'),
        ('2002 Clausura', 'Sebastian Abreu'),
        ('2002 Apertura', 'Jose Cardozo'),
        ('2003 Clausura', 'Jose Cardozo'),
        ('2003 Apertura', 'Luis Gabriel Rey'),
        ('2004 Clausura', 'Andres Silvera'),
        ('2004 Clausura', 'Bruno Marioni'),
        ('2004 Apertura', 'Guillermo Franco'),
        ('2005 Clausura', 'Matias Vuoso'),
        ('2005 Apertura', 'Matias Vuoso'),
        ('2005 Apertura', 'Walter Gaitan'),
        ('2005 Apertura', 'Kleber Boas'),
        ('2005 Apertura', 'Sebastian Abreu'),
        ('2006 Clausura', 'Sebastian Abreu'),
        ('2006 Clausura', 'Salvador Cabanas'),
        ('2006 Apertura', 'Bruno Marioni'),
        ('2007 Clausura', 'Omar Bravo'),
        ('2007 Apertura', 'Alfredo David Moreno'),
        ('2008 Clausura', 'Humberto Suazo'),
        ('2008 Apertura', 'Hector Mancilla'),
        ('2009 Clausura', 'Hector Mancilla'),
        ('2009 Apertura', 'Emanuel Villa'),
        ('2010 Clausura', 'Javier Hernandez'),
        ('2010 Clausura', 'Herculez Gomez'),
        ('2010 Clausura', 'Johan Fano'),
        ('2010 Apertura', 'Christian Benitez'),
        ('2011 Clausura', 'Angel Reyna'),
        ('2011 Apertura', 'Ivan Alonso'),
        ('2012 Clausura', 'Ivan Alonso'),
        ('2012 Clausura', 'Christian Benitez'),
        ('2012 Apertura', 'Christian Benitez'),
        ('2012 Apertura', 'Esteban Paredes'),
        ],
}


primera_fuerza = {
    'competition': 'Primera Fuerza',
    'champion': 'Champion',
    'team_data': ['Champion',],


    'Champion': [
        ('1902-1903', 'Orizaba AC'),
        ('1903-1904', 'Mexico Cricket'),
        ('1904-1905', 'Pachuca AC'),
        ('1905-1906', 'Reforma AC'),
        ('1906-1907', 'Reforma AC'),
        ('1907-1908', 'British Club Mexico'),
        ('1908-1909', 'Reforma AC'),
        ('1909-1910', 'Reforma AC'),
        ('1910-1911', 'Reforma AC'),
        ('1911-1912', 'Reforma AC'),
        ('1912-1913', 'Mexico FC'),
        ('1913-1914', 'Real Club Espana'),
        ('1914-1915', 'Real Club Espana'),
        ('1915-1916', 'Real Club Espana'),
        ('1916-1917', 'Real Club Espana'),
        ('1917-1918', 'Pachuca AC'),
        ('1918-1919', 'Real Club Espana'),
        ('1919-1920', 'Pachuca AC'),
        ('1920-1921', 'Germania FV'),
        ('1921-1922', 'Real Club Espana'),
        ('1922-1923', 'CF Asturias'),
        ('1923-1924', 'Real Club Espana'),
        ('1924-1925', 'Club America'),
        ('1925-1926', 'Club America'),
        ('1926-1927', 'Club America'),
        ('1927-1928', 'Club America'),
        ('1928-1929', 'Marte (Mexico)'),
        ('1929-1930', 'Real Club Espana'),
        ('1931-1932', 'Atlante'),
        ('1932-1933', 'Necaxa'),
        ('1933-1934', 'Real Club Espana'),
        ('1934-1935', 'Necaxa'),
        ('1935-1936', 'Real Club Espana'),
        ('1936-1937', 'Necaxa'),
        ('1937-1938', 'Necaxa'),
        ('1938-1939', 'CF Asturias'),
        ('1939-1940', 'Real Club Espana'),
        ('1940-1941', 'Atlante'),
        ('1941-1942', 'Real Club Espana'),
        ('1942-1943', 'Marte (Mexico)'),
        ],

    'Golden Boot': [
        ('1902-1903', 'John Hogg'),
        ('1903-1904', 'Julio Lacaud'),
        ('1904-1905', 'Percy Clifford'),
        ('1905-1906', 'Charles M. Butlin'),
        ('1906-1907', 'Percy Clifford'),
        ('1907-1908', 'John Hogg'),
        ('1908-1909', 'Jorge Parada'),
        ('1908-1909', 'William Bray'),
        ('1909-1910', 'Robert Blackmore'),
        ('1910-1911', 'Charles M. Butlin'),
        ('1910-1911', 'Alfred C. Crowle'),
        ('1911-1912', 'John Hogg'),
        ('1912-1913', 'Jorge Parada'),
        ('1913-1914', 'Bernardo Rodriguez'),
        ('1914-1915', 'Alfred C. Crowle'),
        ('1915-1916', 'Lazaro Ibarreche'),
        ('1916-1917', 'Lazaro Ibarreche'),
        ('1917-1918', 'Lazaro Ibarreche'),
        ('1917-1918', 'Frederick Williams'),
        ('1917-1918', 'Horatio Ortiz'),
        ('1918-1919', 'Lazaro Ibarreche'),
        ('1919-1920', 'Lazaro Ibarreche'),
        ('1924-1925', 'Ernesto Sota'),
        ('1925-1926', 'Kurt Friederich'),
        ('1926-1927', 'Pedro Arruza'),
        ('1926-1927', 'Miguel Ruiz'),
        ('1927-1928', 'Ernesto Sota'),
        ('1928-1929', 'Nicho Mejia'),
        ('1929-1930', 'Ernesto Sota'),
        ('1931-1932', 'Juan Carreno'),
        ('1931-1932', 'Julio Lores'),
        ('1932-1933', 'Julio Lores'),
        ('1933-1934', 'Jose Pacheco'),
        ('1934-1935', 'Hilario Lopez'),
        ('1935-1936', 'Hilario Lopez'),
        ('1936-1937', 'Hilario Lopez'),
        ('1937-1938', 'Efrain Ruiz'),
        ('1938-1939', 'Miguel Gual'),
        ('1939-1940', 'Alberto Mendoza'),
        ('1940-1941', 'Martin Ventolra'),
        ('1941-1942', 'Rafael Meza'),
        ('1942-1943', 'Manuel Alonso'),
        ],
}



campeon = {
    'competition': 'Campeón de Campeones',
    'champion': 'Champion',
    'team_data': ['Champion',],


    'Champion': [
        ('1942', 'Real Club Espana'),
        ('1943', 'Marte (Mexico)'),
        ('1944', 'Asturias'),
        ('1945', 'Real Club Espana'),
        ('1946', 'Veracruz'),
        ('1947', 'Atlante'),
        ('1948', 'Leon'),
        ('1949', 'Leon'),
        ('1950', 'Veracruz'),
        ('1951', 'Atlas'),
        ('1952', 'Leon'),
        ('1953', 'Tampico'),
        ('1954', 'Marte (Mexico)'),
        ('1955', 'Zacatepec'),
        ('1956', 'Leon'),
        ('1957', 'Guadalajara'),
        ('1958', 'Zacatepec'),
        ('1959', 'Guadalajara'),
        ('1960', 'Guadalajara'),
        ('1961', 'Guadalajara'),
        ('1962', 'Guadalajara'),
        ('1963', 'Oro'),
        ('1964', 'Guadalajara'),
        ('1965', 'Guadalajara'),
        ('1966', 'Club America'),
        ('1967', 'Toluca'),
        ('1968', 'Toluca'),
        ('1969', 'Cruz Azul'),
        ('1970', 'Guadalajara'),
        ('1971', 'Club America'),
        ('1972', 'Cruz Azul'),
        ('1974', 'Cruz Azul'),
        ('1975', 'Toluca'),
        ('1976', 'Club America'),
        ('1988', 'Club America'),
        ('1989', 'Club America'),
        ('1990', 'Puebla'),
        ('1991', 'UNAM'),
        ('1992', 'Leon'),
        ('1995', 'Necaxa'),
        ('1996', 'Necaxa'),
        ('1997', 'Santos Laguna'),
        ('1997', 'Guadalajara'),
        ('2003', 'Toluca'),
        ('2004', 'Pachuca'),
        ('2005', 'UNAM'),
        ('2006', 'Toluca'),
        ]
}
