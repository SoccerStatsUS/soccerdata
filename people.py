from collections import defaultdict

from mongo import soccer_db


class PersonNamer(object):
    """
    Get the canonical name of a person.
    Currently retrieving based on stats model.
    Not sure what the best way to do this is.
    """
    def __init__(self):
        self.mapping = self.get_mapping()


    def get_mapping(self):
        d = defaultdict(list)
        for e in soccer_db.stats.find():
            # Could do a lot of other tuples.
            t = (e['team'], e['season'])
            d[t].append(e['name'])

        return d

    def get_player_name(self, partial, team, season):
        names = self.mapping[(team, season)]
        for name in names:
            if partial in name:
                return partial

        # Handle J. Rooney et al.
        for name in names:
            first, last = partial.split(' ', 1)
            first = first.replace('.', '')
            if last in name and name.startswith(first):
                return name

        print "Can't find for %s" % partial
        

            

