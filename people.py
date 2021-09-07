from helpers import get_rand_year, get_rand_month

def make_person(name, favColor):
    return {
        'name': name,
        'favColor': favColor,
        'birth_year': get_rand_year(),
        'birth_month': get_rand_month()
    }