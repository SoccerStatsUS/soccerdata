import os

p = '/home/chris/www/soccerdata/data/sources'




def load():

    def process_line(line):
        if not line.strip():
            return {}


        fields = line.split(';')
        fields = [e.strip() for e in fields]
        if len(fields) == 2:
            name, author = fields
            url = ''
        else:
            try:
                name, author, url = fields
            except:
                import pdb; pdb.set_trace()

        return {
                'name': name,
                'author': author,
                'base_url': url,
                }

    l = []

    for line in open(p):
        l.append(process_line(line))

    return [e for e in l if e]

