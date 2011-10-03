
SALARIES_PATH = "/home/chris/www/soccerdata/data/salaries.csv"

def load_salaries():
    """
    Load MLS salaries
    """

    def process_line(line):
        # Remove trailing newline.
        if line.endswith("\n"):
            line = line[:-1]

        year, team, last_name, first_name, _, base, extra = line.split('\t')
        name = "%s %s" % (first_name, last_name)

        return {
            'name': name,
            'year': year,
            'team': team,
            'base': base,
            'extra': extra,
            }

    f = open(SALARIES_PATH)
    return [process_line(line) for line in f]

