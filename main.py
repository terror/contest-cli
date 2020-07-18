import requests
import argparse
from datetime import datetime, date


def main():
    parser = argparse.ArgumentParser()

    # Add Args
    parser.add_argument('-s', '--site', help='Contest site')
    parser.add_argument('-l', '--list', action="store_true",
                        help='Contest site list')
    # Sites
    sites = {
        'leetcode': 'leet_code',
        'codeforcesgym': 'codeforces_gym',
        'codeforces': 'codeforces',
        'topcoder': 'top_coder',
        'atcoder': 'at_coder',
        'codechef': 'code_chef',
        'csacademy': 'cs_academy',
        'hackerrank': 'hacker_rank',
        'hackerearth': 'hacker_earth',
        'kickstart': 'kick_start',
    }
    # Parse Args
    args = parser.parse_args()
    if args.site:
        if args.site.lower() in sites:
            args.site = sites[args.site.lower()]
            url = 'https://kontests.net/api/v1/{}'.format(args.site)
        get_info(args.site, url)
    if args.list:
        get_sites()


def get_info(site, url):
    try:
        res, site = requests.get(url), ''.join(
            [i for i in site if i.isalpha()])
        count, i, length = 0, len(res.json())-1, int(get_length(res)*1.5)

        # Separators
        sep_hash, sep_dash, sep_title = "#"*length, "-"*length, "-"*(length//3)

        # Title
        print("{} {} {} ".format(sep_title, site.upper(), sep_title))

        for item in res.json():
            if count % 2 == 0:
                print(sep_hash)
            print("Contest name: ", item["name"])

            # Start & End info
            start_date = str(datetime.fromisoformat(item["start_time"][:-1]))
            end_date = str(datetime.fromisoformat(item["end_time"][:-1]))

            # Convert dates
            start_date_converted = convert_date(start_date[0:10])
            end_date_converted = convert_date(end_date[0:10])

            print("Register: ", item["url"])
            print("Start date: ", start_date_converted,
                  "Start time: ", start_date[11:19])
            print("End date: ", end_date_converted,
                  "End time: ", end_date[11:19])
            print("Duration: ", float(item["duration"])//3600, "Hours")
            if count == i and count % 2 != 0:
                print(sep_hash)
            if count % 2 == 0:
                print(sep_hash)

            count += 1
        print(sep_dash)
    except requests.exceptions.RequestException as e:
        raise System.Exit(e)


def get_sites():
    res = requests.get("https://kontests.net/api/v1/sites")
    print("Supported sites:")
    print("--------------------------")
    for item in res.json():
        print(item[0])
    print("---------------------------")


def get_length(items):
    mx = 0
    for i in items.json():
        for key, val in i.items():
            mx = max(len(str(val)), mx)
    return mx


def convert_date(date_to_convert):
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    year = int(date_to_convert[0:4])
    month = 0 + int(date_to_convert[6:7])
    day = 0 + int(date_to_convert[8:10])

    # temp fix
    while month < 1:
        month += 1

    converted_date = days[date(year, month, day).weekday(
    )] + " " + months[month-1] + " " + str(day) + ", " + str(year)
    return converted_date


if __name__ == '__main__':
    main()
