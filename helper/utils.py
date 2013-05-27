import urllib
import re


def getPhstamp(data,dtsg):
    phstamp='1'

    string=urllib.urlencode(data)
    input_len=len(string)

    for char in dtsg:
        phstamp+=str(ord(char))

    phstamp='%s%d' % (phstamp,input_len)
    return phstamp

def getDtsg(head_content):
    dtsg=''

    dtsg_match=re.search('\"fb_dtsg\":\"(\S+)\",\"ajaxpipe_token\"',head_content)
    if dtsg_match:
        dtsg=dtsg_match.group(1)
    return dtsg

