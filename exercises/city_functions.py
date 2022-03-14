# 11-1 City, Country: write a function that accepts two parameters: a city name and a country nam;e.
# The function should return a single string of the form city, country such as santiago, Chile.
# Store the function in a module called city_functions.py.
# """A collection of functions fo working with cities."""

# def city_country(city, country):
# """Return a string like 'Santiago, Chile'."""
# return f"{city.title()}, {country.title()}"

# 11-2 population:
# modify your function, so it requires a third parameter, population. it should now return a single string of the
# form city, country- population xxx, such as santiago, chile - population 5000000. run test _cities.py again.
# make sure test_city_country() fail this time.
# modify the function so the population parameter is optional. run test _cities. py again, and make sure
# test_city_country passes again
# write a second test called test_city_country_population() that verfies you can call your function
# with values 'santiago, 'chile' and population=5000000'. run test_cities.py again, and make sure this new test passes.
"""A collection of functions fo working with cities."""


def city_country(city, country, population=()):
    """Return a string like 'Santiago, Chile - population 5000000'."""

    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f"-population {population}"
    return output_string


