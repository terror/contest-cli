import requests
import argparse
from datetime import datetime


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
            args.site = sites[args.site]
        get_info(args.site)
    if args.list:
        get_sites()


def get_info(site):
    res, site = requests.get('https://kontests.net/api/v1/{}'.format(site)
                             ), ''.join([i for i in site if i.isalpha()])
    count, i, length = 0, len(res.json())-1, int(get_length(res)*1.5)

    # Separators
    sep_hash, sep_dash, sep_title = "#"*length, "-"*length, "-"*(length//3)

    # Title
    print("{} {} {} ".format(sep_title, site.upper(), sep_title))

    for item in res.json():
        if count % 2 == 0:
            print(sep_hash)
        print("Contest name: ", item["name"])

        # Start / End
        start_date = item["start_time"][0:10]
        start_time = item["start_time"][12:16]
        end_date = item["end_time"][0:10]
        end_time = item["end_time"][12:16]

        print("Register: ", item["url"])
        print("Start date: ", start_date, "Start time: ", start_time)
        print("End date: ", end_date, "End time: ", end_time)
        print("Duration: ", float(item["duration"])//3600, "Hours")
        if count == i and count % 2 != 0:
            print(sep_hash)
        if count % 2 == 0:
            print(sep_hash)

        count += 1
    print(sep_dash)


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
            mx = max(len(val), mx)
    return mx


if __name__ == '__main__':
    main()
