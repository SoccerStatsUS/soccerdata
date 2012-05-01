
states = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'FL': 'Florida',
    'HI': 'Hawaii',
    'GA': 'Georgia',
    'IA': 'Iowa',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'ON': 'Ontario',
    'OR': 'Oregon',
    'OK': 'Oklahoma',
    'PA'; 'Pennsylvania',
    'QC': 'Quebec',
    'OH': 'Ohio',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tenneessee',
    'TX': 'Texas',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming',
    }



def get_location(s):
    if not s:
        return {}

    pieces = [e.strip() for e in s.split(",")]

    # Should only be of the forms Austin, TX, Austin, Texas, or Austin, Texas, United States
    if len(pieces) < 2 or len(pieces) > 3:
        import pdb; pdb.set_trace()
    elif len(pieces) == 2:
        city = pieces[0]

        if pieces[1] in STATES.keys():
            state = STATES[pieces[1]]
            country = 'United States'
        elif pieces[1] in STATES.values():
            state = pieces[1]
            country = 'United States'
        else:
            state = None
            country = pieces[1]

    elif len(pieces) == 3:
        city, state, country = pieces

    return {
        'city': city,
        'state': state,
        'country': country,
        }

    


