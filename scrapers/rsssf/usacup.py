from base import RSSSFParser

# Notes: 
# 2001 season is not any good.

class OpenCupParser(RSSSFParser):
    table_start = None
    table_end = None

    CUT_OFFS = [
        "Second Round", 
        "Third Round",
        "Quarterfinals",
        "Semifinals",
        'Final',
        ]

    SUB_LINES = {
        2009: {
            #'Second Round [Jun 16]': '[Jun 16]',
            #'Quarterfinals [Jul 7]': '[Jul 7]',
            #'Semifinals [Jul 21]': '[Jul 21]',
            'Final [Sep 2, RFK Stadium; Washington, DC]': '[Sep 2]'
            },

        2008: {
            'Final [Sep 3, RFK Stadium; Washington, DC]': '[Sep 3]',
            },

        2007: {
            'Final [Oct 3, Pizza Hut Park, Frisco; att: 10,618; ref: Alex Prus]': '[Oct 3]',
            },

        2006: {
            'Final [Sep 27, Toyota Park, Chicago]': '[Sep 27]',
            },

        2005: {
            'Final [Sep 28, Home Depot Center]': '[Sep 28]',
            },

        2004: {},
        2003: {
            'Final [Oct 16, at Giants Stadium; att: 5,183]': '[Oct 16]',
            },
        2002: {
            'Final [Oct 24, Columbus (Ohio) Crew Stadium]': '[Oct 24]',
            },




        }

def process_year(year):
    y = str(year)[-2:]
    url = 'http://rsssf.com/tablesu/usacup%s.html'% y
    print url
    return OpenCupParser().parse_page(url, year)



if __name__ == "__main__":
    print "\n".join([str(e) for e in process_year(2011)])
