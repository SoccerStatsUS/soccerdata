competitions = {
    'USISL Premier League': 'USL Premier Developmental League',
    'USISL Select League': 'USL First Division',
    'USISL Professional League': 'USL Second Division',
    'USL Pro': 'USL Second Division',
    'A-League': 'USL First Division',
    'Western Soccer Alliance': 'Western Soccer League',
    'USL Pro': 'USL Second Division',
}



def get_competition(s):
    s = s.strip()
    return competitions.get(s, s)
