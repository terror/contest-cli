import argparse
from utils import get_max_length, convert_date, get_sites, get_info

def main():
    parser = argparse.ArgumentParser()

    # Add Args
    parser.add_argument('-s', '--site', help='Contest site')
    parser.add_argument('-l', '--list', action="store_true",
                        help='Contest site list')

    # All Supported Sites
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

if __name__ == '__main__':
    main()
