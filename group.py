#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys
import configure
from helper.facebook_helper import FB
from helper.group_helper import Group


def main():
    fb = FB()
    fb.login(fb_email=configure.fb_email, fb_pass=configure.fb_password)

    group = Group(fb.session, fb.my_id)

    # print all groups with name and id
    # group.printAllGroups()

    # post something in group
    group.updateStatus(group_id='165780593537834', text='生日快樂')

    sys.exit(0)

if __name__ == '__main__':
    main()
