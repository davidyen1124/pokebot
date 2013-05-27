#!/usr/bin/python

import time
import sys
import configure
from helper.facebook_helper import FB
from helper.group_helper import Group


def main():
    fb=FB()
    fb.login(fb_email=configure.fb_email,fb_pass=configure.fb_password)

    group=Group(fb.session,fb.my_id)
    #group.getAllGroups()

    for i in range(1,5):
        group.updateStatus(group_id='242006459221814',text=u'Sparks Lab{0}'.format(i))

    sys.exit(0)

if __name__ == '__main__':
    main()
