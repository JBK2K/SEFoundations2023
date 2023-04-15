from app.dynlottonr.models import Lottoresults, Main, Super


def test_lottoresults_renders_results(client):
    # Page loads and renders cookies

    new_entry = Lottoresults(day='Highday', mainnr_id=1, supernr_id=1), Main(
        nr1=1, nr2=2, nr3=3, nr4=4, nr5=5), Super(nr1=1, nr2=2)
    new_entry.save()

    response = client.get('/eurojackpot')
    assert b'Highday' in response.data
