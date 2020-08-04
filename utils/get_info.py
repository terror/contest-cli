import requests
from datetime import datetime, date
from utils import get_max_length, convert_date

# Fetches and prints all useful contest information
def get_info(site, url):
    try:
        res, site = requests.get(url), ''.join(
            [i for i in site if i.isalpha()])
        count, i, length = 0, len(res.json())-1, int(get_max_length(res)*1.5)

        # Separators
        sep_hash, sep_dash, sep_title = "#"*length, "-"*length, "-"*(length//3)

        # Title
        print("{} {} {} ".format(sep_title, site.upper(), sep_title))

        for item in res.json():
            print("{}\n".format(sep_hash) if count % 2 == 0 else "", end="")
            print("Contest name: ", item["name"])

            # Start & End info
            start_date = str(datetime.fromisoformat(item["start_time"][:-1]))
            end_date = str(datetime.fromisoformat(item["end_time"][:-1]))

            # Convert dates
            start_date_converted = convert_date(start_date[0:10])
            end_date_converted = convert_date(end_date[0:10])

            # Print main information
            print("Register: ", item["url"])
            print("Start date: ", start_date_converted,
                  "Start time: ", start_date[11:19])
            print("End date: ", end_date_converted,
                  "End time: ", end_date[11:19])
            print("Duration: ", round(
                float(item["duration"])/3600, 1), "Hours")

            # Print Separators
            print("{}\n".format(sep_hash) if count == i and count % 2 != 0 else "", end="")
            print("{}\n".format(sep_hash) if count % 2 == 0 else "", end="")
            count += 1

        print(sep_dash)
    except requests.exceptions.RequestException as e:
        raise System.Exit(e)