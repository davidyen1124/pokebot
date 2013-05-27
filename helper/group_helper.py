import requests
import re

class Group:
    def __init__(self,session):
        self.session=session
    
    def getAllGroups(self):
        request=self.session.get('https://www.facebook.com/bookmarks/groups')
        self.__checkGroups(request.content)

    def __checkGroups(self,content):
        pass
        
