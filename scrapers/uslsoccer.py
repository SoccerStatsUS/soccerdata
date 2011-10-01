



# Woo-hoo! This returns stats json!
url = 'http://www.uslsoccer.com/teams/33769235/934451-33769304-stat.js'


# All results json:
# 2011
# http://pdl.uslsoccer.com/schedules/2011/33769304.js?2630
# 2010
# http://pdl.uslsoccer.com/schedules/2010/20202833.js?2814
# 2009
# http://www.uslsoccer.com/schedules/2009/13381307.js?0387

# 2008
# http://pdl.uslsoccer.com/scripts/runisa.dll?M2.131326:gp:2049575503.7311:72014+Elements/Display+E+46241++8630281++04/2008+8630213


# Game url:
#http://pdl.uslsoccer.com/stats/2011/2214590.html




from soccerdata.utils import scrape_soup


def scrape_bad(url):
    """
    """
    soup = scrape_soup(url)
    

    import pdb; pdb.set_trace()

    x = 5

if __name__ == "__main__":
    # bad choice
    url = 'http://www.uslsoccer.com/stats/2011/2214249.html'

    scrape_bad(url)
