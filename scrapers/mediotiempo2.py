

from soccerdata.utils import scrape_soup, get_contents, pounds_to_kg, inches_to_cm
from soccerdata.cache import data_cache, set_cache




def scrape_schedule(url_data):
    url = 'http://msn.mediotiempo.com/ajax/ajax_jornadas.php'
    soup = scrape_soup(url, encoding='iso_8859_1', url_data=url_data)

    import pdb; pdb.set_trace()
    x = 5




if __name__ == "__main__":
    print scrape_schedule({
            'id_torneo': 136,
            'jornada': 'final',
            'id_liga': 1,
            })
