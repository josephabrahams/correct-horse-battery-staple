#!/usr/bin/env python

import calendar
import datetime
import random
import re
import time

import xkcdpass.xkcd_password as xp


TIMECODE_INTERVAL = 30


def timecode(interval=TIMECODE_INTERVAL, for_time=datetime.datetime.now()):
    # Based on PyOTP: https://joseph.is/3L4GGwK
    if for_time.tzinfo:
        return int(calendar.timegm(for_time.utctimetuple()) / interval)
    else:
        return int(time.mktime(for_time.timetuple()) / interval)


def generate_wordlist(wordfile=None, min_length=5, max_length=9, valid_chars="."):
    if min_length > max_length:
        max_length = min_length

    words = list()

    regexp = re.compile("^{0}{{{1},{2}}}$".format(valid_chars, min_length, max_length))
    if wordfile is None:
        wordfile = "eff-long"

    for wf in wordfile.split(","):
        wf = xp.locate_wordfile(wf)
        with open(wf, encoding="utf-8") as wlf:
            for line in wlf:
                thisword = line.strip()
                if regexp.match(thisword) is not None:
                    words.append(thisword)
    if len(words):
        return words
    else:
        raise SystemExit(
            "Error: provided arguments result in zero-length wordlist, exiting."
        )


def choose_words(wordlist, numwords):
    seed = f"{xp.SEED}{timecode(interval=xp.TIMECODE_INTERVAL)}"
    rng = random.Random(seed)
    return [rng.choice(wordlist) for i in range(numwords)]


def generate_xkcd_totp(interval=None, numwords=4, seed=None):
    xp.SEED = seed
    xp.TIMECODE_INTERVAL = interval or TIMECODE_INTERVAL
    xp.generate_wordlist = generate_wordlist
    xp.choose_words = choose_words

    wordfile = xp.locate_wordfile()
    wordlist = xp.generate_wordlist(wordfile=wordfile)
    xkcd_totp = xp.generate_xkcdpassword(wordlist, numwords=numwords)

    return xkcd_totp


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Generate a XKCD-style time-based one-time password."
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=30,
        metavar="INTERVAL",
        help="Time in INTERVAL seconds that each passphrase lasts.",
    )
    parser.add_argument(
        "-n",
        "--numwords",
        type=int,
        default=4,
        metavar="NUM_WORDS",
        help="Generate passphrases containing exactly NUM_WORDS words.",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=str,
        default=None,
        metavar="SEED",
        help="String SEED used to make passphrases unique within a given time interval.",
    )

    args = parser.parse_args()

    try:
        print(
            generate_xkcd_totp(
                interval=args.interval, numwords=args.numwords, seed=args.seed
            )
        )
    except SystemExit as e:
        sys.exit(e.code)
