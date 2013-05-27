import requests
import re
import configure
from helper.poke_helper import Poke

class FB:
    def __init__(self):
        self.session=requests.Session()
        self.session.headers.update({'User-Agent':configure.user_agent})
        self.my_id=-1

    def login(self,fb_email=None,fb_pass=None):
        print '[+] Loging in...'

        if not fb_email or not fb_pass:
            print '[!] No email or password given'
            return

        request=self.session.get('http://facebook.com/')
        data=self.__getLoginForms(request.content)

        if data:
            data['fields']['email']=fb_email
            data['fields']['pass']=fb_pass

            request=self.session.post(data['action'],data=data['fields'])
            self.my_id=self.__findMyId(request.content)

            print '[+] Welcome {0}\n'.format(self.my_id)
        else:
            print '[!] Login error'
        
    def __getLoginForms(self,content):
        forms={}
        form_content=''

        # Get the content of 'login_form' form only
        for line in content.split('\n'):
            if 'login_form' in line:
                form_match=re.search(r'<form id=\"login_form\".+</form></div>',line)
                if form_match:
                    form_content=form_match.group(0)
                    break

        if not form_content:
            return forms

        # Find action url
        action_match=re.search(r'action=\"(\S+)\"',form_content)
        if action_match:
            forms['action']=action_match.group(1)

        # Find the fields
        fields={}
        field_match=re.findall(r'name=\"(\S+)\" (value=\"(\S*)\")*',form_content)
        if field_match:
            for field in field_match:
                fields[field[0]]=field[2]
        forms['fields']=fields

        return forms

    def __findMyId(self,content):
        my_id=-1
        for line in content.split('\n'):
            if '<head>' in line:
                id_match=re.search('\"user\":\"(\d+)\"',line)
                if id_match:
                    my_id=id_match.group(1)
                break
        return my_id

    def poke(self):
        poke=Poke(session=self.session,my_id=self.my_id)
        poke.poke()
