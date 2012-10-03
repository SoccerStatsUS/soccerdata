
SALARIES_PATH = "/home/chris/www/soccerdata/data/money/salaries/mls.csv"
MLS_2012_SALARIES_PATH = "/home/chris/www/soccerdata/data/money/salaries/2012"


def load_salaries():
    s1 = load_old_salaries()
    s2 = load_2012_salaries()
    l = s1 + s2

    return s1 + s2

def load_old_salaries():
    """
    Load MLS salaries
    """

    def process_line(line):
        # Remove trailing newline.
        if line.endswith("\n"):
            line = line[:-1]


        try:
            year, team, last_name, first_name, _, base, extra = line.split('\t')
        except:
            import pdb; pdb.set_trace()

        name = "%s %s" % (first_name.strip(), last_name.strip())

        if 'Twellman' in name:
            pass #import pdb; pdb.set_trace()

        return {
            'name': name,
            'year': year,
            'team': team,
            'base': base,
            'extra': extra,
            }

    f = open(SALARIES_PATH)
    return [process_line(line) for line in f]


def load_2012_salaries():
    """
    Load MLS salaries
    """

    def process_line(line):
        # Remove trailing newline.
        if line.endswith("\n"):
            line = line[:-1]

        team, n, base, extra = line.split(';')

        if ',' in n:
            last_name, first_name = [e.strip() for e in n.split(',')]
            name = "%s %s" % (first_name, last_name)
        else:
            print n
            name = n

        return {
            'year': '2012',

            'name': name,
            'team': team,
            'base': base,
            'extra': extra,
            }

    f = open(MLS_2012_SALARIES_PATH)
    return [process_line(line) for line in f]
