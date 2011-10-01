
#
# http://a-leaguearchive.tripod.com/2005/results05a.htm

# Looks like we're missing USL-1 from 2006-2009.


# Woo-hoo! This returns stats json!
url = 'http://www.uslsoccer.com/teams/33769235/934451-33769304-stat.js'


# USL-1 urls

# 2009
# http://www.uslsoccer.com/schedules/2009/13380593.html
# http://www.uslsoccer.com/schedules/2009/13380660.js?9228

# 2008
# http://www.uslsoccer.com/schedules/2008/8588667.20086.html

# 2007
# http://www.uslsoccer.com/schedules/2007/6187380.html

# 2006
# http://www.uslsoccer.com/schedules/2006/4068269.html

# 2005
# http://www.uslsoccer.com/schedules/2005/2465825.20058.html

# PDL urls
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




from soccerdata.utils import scrape_soup, get_contents


def scrape_game_page(url):
    soup = scrape_soup(url, encoding='iso_8859_1')
    div = soup.find("div", {"style": 'border: 1px solid #B0B0B0; background-color: #FFFFFF; padding: 8px;'})    

    text = get_contents(div)
    text = text.replace("&nbsp;", '')
    for e in "Weather", "Attendance", "Summary":
        text = text.replace(e, "")
    text = text.replace("Cautions", ":Cautions:")
    text = text.replace("Referees", ":Referees:")

    data = [e.strip() for e in text.split(":") if e.strip()]

    weather = data[0]
    attendance = data[1]

    goals = []
    for e in data[1:]:
        if e == 'Cautions':
            break
        goals.append(e)


    return {
        'weather': weather,
        'attendance': attendance,
        'goals': goals
        }
    


def scrape_bad(url):
    """
    """
    soup = scrape_soup(url)
    


    import pdb; pdb.set_trace()

    x = 5

if __name__ == "__main__":
    # bad choice
    #url = 'http://www.uslsoccer.com/stats/2011/2214249.html'
    #scrape_bad(url)

    print scrape_game_page('http://www.uslsoccer.com/stats/2005/32094.html')
