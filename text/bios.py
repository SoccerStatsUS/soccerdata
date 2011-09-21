import datetime

# Scrape bios compiled by me.

# Could probably improve this.
BIOS_PATH = "/home/chris/www/soccerdata/data/people/bios.chris.csv"


def load_bios():
    """
    Load my MLS bios data.
    """

    def process_line(line):

        # Remove trailing newline.
        if line.endswith("\n"):
            line = line[:-1]

        # Tab separated.
        items = line.split('\t')

        d = dict(zip(header, items))

        if d['year'] and d['month'] and d['day']:
            # Repair inconsistent year handling.
            if int(d['year']) < 100:
                d['year'] = int(d['year']) + 1900

            d['birthdate'] = datetime.datetime(int(d['year']), int(d['month']), int(d['day']))
        else:
            d['birthdate'] = None

        return d

    f = open(BIOS_PATH)
    header = ['name', '_', 'pos', 'feet', 'inches', 'weight', 'month', 'day', 'year', '_', 'college', 'birthplace']
    return [process_line(line) for line in f]
    



    

        
        
