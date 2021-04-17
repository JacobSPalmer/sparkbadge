import argparse
import sys
import tempfile
import webbrowser
import random

import sparkbadge
from sparkbadge import plot_normalizer

def main():
    parser = argparse.ArgumentParser(
        'sparkbadges',
        description='generate simplistic sparkline for github metrics'
    )

    parser.add_argument(
        '--data',
        nargs='+',
        type = float,
        help='the data, formatted as a list of intgers, to generate the sparkline'
    )
    parser.add_argument(
        '--browser',
        action='store_true',
        default=True,
        help='display generated badge within a browser window'
    )
    parser.add_argument(
        '--random',
        action='store_true',
        default=False,
        help='display a chart with randomized y values. If --random true, values inputted for --data will be ignored. Default range is 50 and n is 8'
    )
    parser.add_argument(
        '--random_size',
        default=None,
        type = int,
        help = 'set the number of values to be randomly generated if --random true is stated'
    )
    parser.add_argument(
        '--random_range',
        default=None,
        type = float,
        help = 'set the range of values to be randomly generated if -- random true is stated'
    )
    args = parser.parse_args()

    if args.random:
        r = random.randint(5, 100)
        n = random.randint(4, 15)
        if not(args.random_range is None):
            r = args.random_range
        if not(args.random_size is None):
            n = args.random_size
        s = random.sample(range(0, int(r)), int(n))
        badge = sparkbadge.badge(
            data = s
        )
    else:
        badge = sparkbadge.badge(
            data=args.data
        )





    if args.browser:
        _, badge_path = tempfile.mkstemp(suffix='.svg')
        with open(badge_path, 'w') as f:
            f.write(badge)

        webbrowser.open_new_tab('file://' + badge_path)
    else:
            print(badge, end='')

main()
