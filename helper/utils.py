import urllib


def getPhstamp(data,dtsg):
    phstamp='1'

    string=urllib.urlencode(data)
    input_len=len(string)

    for char in dtsg:
        phstamp+=str(ord(char))

    phstamp='%s%d' % (phstamp,input_len)
    return phstamp
