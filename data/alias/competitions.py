competitions = {
    'USISL Premier League': 'USL Premier Developmental League',
    'USISL Select League': 'USL First Division',
    'USISL Professional League': 'USL Second Division',
    'USL Pro': 'USL Second Division',
    'A-League': 'USL First Division',
    'United Soccer League': 'United Soccer League (1984-1985)',

    'Western Soccer Alliance': 'Western Soccer League',
    'Western Soccer Alliance Playoffs': 'Western Soccer League Playoffs',


    'USL Pro': 'USL Second Division',
    'Domestic Tour': 'Friendly',
    'International Tour': 'Friendly',
}



def get_competition(s):
    if s is None:
        return None
    
    s = s.strip()
    return competitions.get(s, s)
