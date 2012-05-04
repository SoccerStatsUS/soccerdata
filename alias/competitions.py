competitions = {
    'USISL Premier League': 'USL Premier Developmental League',
    'USISL Select League': 'USL First Division',
    'USISL Professional League': 'USL Second Division',
    'USL Pro': 'USL Second Division',
    'A-League': 'USL First Division',
    'Western Soccer Alliance': 'Western Soccer League',
    'USL Pro': 'USL Second Division',
    'Domestic Tour': 'Friendly',
    'International Tour': 'Friendly',
}



def get_competition(s):
    if s is None:
        return None
    
    s = s.strip()
    return competitions.get(s, s)
