from soccer.drafts.models import Draft, Pick
from soccer.players.models import Person
from soccer.teams.models import Team

from soccer.utils.players import scrape_person


def remove_pairs(text, start, end):
    """
    Removes pairs like (hello) or [whatever]
    """
    s = ""
    include = True
    for char in text:
        if char == start:
            include = False

        if include:
            s += char
        
        if char == end:
            include = True

    return s



def process_draft(draft, text)
    
    # Clean up some extraneous info..
    text = text.replace("*", "")
    text = remove_pairs(text, "(", ")")
    text = remove_pairs(text, "[", "]")
    lines = [e for e in text.split("\n") if e]

    def process_line(line):
        number, name, team = itesm.split('\t')
        return {
            'number': int(number),
            'name': name.strip(),
            'team': team.strip(),
            }

    return [process_line(line) for line in lines]
        
