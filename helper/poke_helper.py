import requests
import re
import utils
from datetime import datetime


class Poke:
    def __init__(self,session=None,my_id=None):
        self.session=session
        self.my_id=my_id

    def poke(self):
        request=self.session.get('https://www.facebook.com/pokes')
        (poke_list,dtsg)=self.__checkPokes(request.content)
        if not poke_list:
            pass
            #print 'Nobody poked you'
        else:
            for poke in poke_list:
                self.__pokeIt(dtsg,poke)

    def __pokeIt(self,dtsg,poke):
        print '[+] ({0})   Poke \"{1}\" like a boss!'.format(str(datetime.now()),poke['name'])

        data={}
        data['uid']=poke['uid']
        data['pokeback']='1'
        data['nctr[_mod]']='pagelet_pokes'
        data['__user']=self.my_id
        data['__a']='1'
        #data['__dyn']='7n8ahxoNpGr83ih0'
        data['__req']='8'
        data['fb_dtsg']=dtsg
        data['phstamp']=utils.getPhstamp(data,dtsg)

        request=self.session.post('https://www.facebook.com/ajax/pokes/poke_inline.php',data=data)

    def __checkPokes(self,content):
        poke_list=[]
        is_finished=False
        dtsg=''

        for line in content.split('\n'):

            # get dtsg parameter
            if 'head' in line and not dtsg:
               dtsg=utils.getDtsg(line)

            # get pokers' uid
            elif 'div class=\"uiHeader uiHeaderWithImage uiHeaderPage\"' in line:
                for poke in line.split('a href'):
                    if 'data-hovercard' in poke:
                        poke_match=re.search('user.php\?id=(\d+)\">(.*)</a>.*</div><div class=\"',poke)
                        if poke_match:
                            pokeman={'uid':poke_match.group(1),'name':poke_match.group(2)}
                            poke_list.append(pokeman)

        return (poke_list,dtsg)
