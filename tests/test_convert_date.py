from utils import convert_date

def test_convert_date():
    dates = {
        "2020-08-05T14:35:00.000Z": "Wednesday August 5, 2020",
        "2020-08-16T14:35:00.000Z": "Sunday August 16, 2020",
        "2020-08-08T16:00:00.000Z": "Saturday August 8, 2020"
    }

    for key, val in dates.items():
        assert(convert_date(key) == val)