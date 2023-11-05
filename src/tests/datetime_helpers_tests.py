from utils import datetime_helpers


def test_get_day():

    day = datetime_helpers.get_day()
    print(f'day :: {day[0]=}, month :: {day[1]=}')
    assert int(day[0]) <= 31 and int(day[1]) <= 12