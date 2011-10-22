
from soccerdata.utils import scrape_soup

url = 'http://nasljerseys.com/Players/Players_Roster.htm'



def scrape_player_urls():
    soup = scrape_soup(url)
    table = soup.find("table", "MsoTableGrid")

    urls = []
    for e in table.findAll('a'):
        try:
            urls.append(e['href'])
        except KeyError:
            print e

    return urls

    import pdb; pdb.set_trace()
    x = 5


if __name__ == "__main__":
    print scrape_player_urls()
