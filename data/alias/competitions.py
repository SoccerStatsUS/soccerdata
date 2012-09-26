aliases = {}

full_alias = {
    'USISL Premier League': 'USL Premier Developmental League',
    'USISL Select League': 'USL First Division',
    'USISL Professional League': 'USL Second Division',
    'USL Pro': 'USL Second Division',
    'A-League': 'USL First Division',
    'United Soccer League': 'United Soccer League (1984-1985)',

    'Western Soccer Alliance': 'Western Soccer League',
    'Western Soccer Alliance Playoffs': 'Western Soccer League Playoffs',

    'American Indoor Soccer Association': 'National Professional Soccer League (indoor)',


    'USL Pro': 'USL Second Division',
    'International Friendly': 'Friendly International',

    'Recopa CONCACAF': 'CONCACAF Cup Winners Cup',
    'Southwest Indoor Soccer League': 'United States Interregional Soccer League (indoor)',
    'Southwest Independent Soccer League (indoor)': 'United States Interregional Soccer League (indoor)',
    'Southwest Independent Soccer League': 'United States Interregional Soccer League',
    'Premier Soccer Alliance': 'World Indoor Soccer League',
}

aliases.update(full_alias)

# Don't want to completely delete these.
partial_alias = {
    'Domestic Tour': 'Friendly',
    'International Tour': 'Friendly',

    'Bicentennial Cup': 'Friendly',
    'Carlsberg Cup': 'Friendly',
    'Carolina Challenge Cup': 'Friendly',
    'Dynamo Charities Cup': 'Friendly',
    'Europac International': 'Friendly',
    'Spring Cup Matches': 'Friendly',
    'Sunshine International': 'Friendly',
    'Toronto International': 'Friendly',
    'Tournament of Champions': 'Friendly',
    'Trans-Atlantic Challenge Cup': 'Friendly',

    'Amistad Cup': 'Friendly International',

    'International Cup': 'Friendly International',
    'Joe Robbie Cup': 'Friendly International',
    'Kirin Cup': 'Friendly International',
    'Los Angeles Soccer Tournament': 'Friendly',
    'Mexico City Tournament': 'Friendly International',
    'Miami Cup': 'Friendly International',
    'North American Nations Cup': 'Friendly International',
    'Presidents Cup': 'Friendly International',
    'Trinidad Tournament': 'Friendly International',
    }
aliases.update(partial_alias)


def get_competition(s):
    if s is None:
        return None
    
    s = s.strip()
    return aliases.get(s, s)
