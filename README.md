# correct horse battery staple

_Fun with XKCD-style passwords using [xkcdpass](https://github.com/redacted/XKCD-password-generator) and [PyOTP](https://github.com/pyauth/pyotp)._

## Install

```bash
$ pipenv install
```

## Usage

```
$ xkcd_pass.py [-h] [-d DELIM] [-n NUM_WORDS]

Generate a XKCD-style password.

optional arguments:
  -d DELIM      Separate words within a passphrase with DELIM.
  -n NUM_WORDS  Generate passphrases containing exactly NUM_WORDS words.
```

```
$ xkcd_totp.py [-h] [-i INTERVAL] [-n NUM_WORDS] [-s SEED]

Generate a XKCD-style time-based one-time password.

optional arguments:
  -i INTERVAL   Time in INTERVAL seconds that each passphrase lasts.
  -n NUM_WORDS  Generate passphrases containing exactly NUM_WORDS words.
  -s SEED       String SEED used to make passphrases unique within a given time interval.
```
