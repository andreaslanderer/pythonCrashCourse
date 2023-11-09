from cities import city_country


def test_city_country():
    result = city_country("Buenos Aires", "Argentina")
    assert result == "Buenos Aires, Argentina"


def test_title_case():
    result = city_country("berlin", "gERMANY")
    assert result == "Berlin, Germany"
