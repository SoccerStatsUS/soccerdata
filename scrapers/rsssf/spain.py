from base import parse_season_page


def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = "http://rsssf.com/tabless/span%s.html" % y
    return parse_season_page(url, year)


def process_years(years):
    for year in years:
        process_year(year)


if __name__ == "__main__":
    print "\n".join([str(e) for e in process_year(2011)])
