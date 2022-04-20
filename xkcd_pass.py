#!/usr/bin/env python

import xkcdpass.xkcd_password as xp


def generate_xkcd_pass(delimiter=" ", numwords=4):
    wordfile = xp.locate_wordfile()
    wordlist = xp.generate_wordlist(wordfile=wordfile)
    xkcd_totp = xp.generate_xkcdpassword(
        wordlist, delimiter=delimiter, numwords=numwords
    )

    return xkcd_totp


if __name__ == "__main__":
    import argparse
    import sys


    parser = argparse.ArgumentParser(description="Generate a XKCD-style password.")
    parser.add_argument(
        "-d",
        "--delimiter",
        default=" ",
        metavar="DELIM",
        help="Separate words within a passphrase with DELIM.",
    )
    parser.add_argument(
        "-n",
        "--numwords",
        type=int,
        default=4,
        metavar="NUM_WORDS",
        help="Generate passphrases containing exactly NUM_WORDS words.",
    )

    args = parser.parse_args()

    try:
        print(generate_xkcd_pass(delimiter=args.delimiter, numwords=args.numwords))
    except SystemExit as e:
        sys.exit(e.code)
