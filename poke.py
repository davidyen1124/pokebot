#!/usr/bin/python

import time
import sys
import configure
from helper.facebook_helper import FB


def main():
    fb = FB()
    fb.login(fb_email=configure.fb_email, fb_pass=configure.fb_password)
    while True:
        try:
            fb.poke()
            time.sleep(configure.poke_interval)
        except KeyboardInterrupt:
            print '\n[!] Have a good POKE day!'
            sys.exit(0)

if __name__ == '__main__':
    main()
