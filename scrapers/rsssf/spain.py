from base import parse_season_page


def fetch_year(year):
    y = str(year)[-2:]
    url = "http://rsssf.com/tabless/span%s.html" % y
    return parse_season_page(url)
    


if __name__ == "__main__":
    parse_season_page(url)
