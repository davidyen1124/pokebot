#!/usr/bin/python

from helper.facebook_helper import FB
import configure
from helper.quit_group import SpamGroup


def main():
    fb = FB()
    fb.login(fb_email=configure.fb_email, fb_pass=configure.fb_password)
    spam_group = SpamGroup(fb.session, fb.my_id)
    spam_group.quitGroup(group_id='582797035086519')

if __name__ == '__main__':
    main()
