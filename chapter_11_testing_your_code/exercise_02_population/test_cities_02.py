from cities_02 import city_country


def test_city_country():
    result = city_country("Paris", "France")
    assert result == "Paris, France"


def test_city_country_population():
    result = city_country("Zurich", "Switzerland", 400_000)
    assert result == "Zurich, Switzerland - population 400000"
