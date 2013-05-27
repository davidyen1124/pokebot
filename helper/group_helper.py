import requests
import re
import utils

class Group:
    def __init__(self,session,my_id):
        self.session=session
        self.groups=[]
        self.my_id=my_id
    
    def getAllGroups(self):
        self.groups=[]
        request=self.session.get('https://www.facebook.com/bookmarks/groups')
        self.groups=self.__checkGroups(request.content)
        if not self.groups:
            print 'No groups found'
            return

        for group in self.groups:
            print '{0}  {1}'.format(group['group_id'],group['name'])

    def __checkGroups(self,content):
        group_list=[]
        for line in content.split('\n'):
            if 'uiList fbBookmarksSeeAllList' in line:
                for group in line.split('itemLabel fcb'):

                    # get group name and id
                    match=re.search('\" id=\"\S+\">(.+)</span><span class=\"count.*data-hovercard=\".*group_(\d+)\" data-hovercard-instant',group)
                    if match:
                        group_item={'name':match.group(1),'group_id':match.group(2)}
                        group_list.append(group_item)
        return group_list

    def updateStatus(self,text=None,group_id=None):
        if not text or not group_id:
            print 'Nothing to update'
            return
        
        request=self.session.get('https://www.facebook.com/groups/{0}/'.format(group_id))
        data=self.__getUpdateStatusData(request.content)
        data['xhpc_context']='profile'
        data['xhpc_ismeta']='1'
        data['xhpc_timeline']=''
        data['xhpc_composerid']='u_jsonp_9_e'
        data['xhpc_targetid']=group_id
        data['xhpc_message_text']=text
        data['xhpc_message']=text
        #data['is_explicit_place']=''
        #data['composertags_place']=''
        #data['composertags_place_name']=''
        #data['composer_session_id']=''
        #data['composertags_city']=''
        data['disable_location_sharing']='false'
        #data['composer_predicted_city']=''
        data['nctr[_mod]']='pagelet_group_composer'
        data['__user']=self.my_id
        data['__a']='1'
        #data['__dyn']=''
        data['__req']='1t'
        data['phstamp']=utils.getPhstamp(data,data['fb_dtsg'])

        request=self.session.post('https://www.facebook.com/ajax/updatestatus.php',data=data)

        if request.status_code==200:
            print '[+] Post \"{0}\" successfully!'.format(text)
        
    def __getUpdateStatusData(self,content):
        dtsg=''
        data={}

        for line in content.split('\n'):
            if '<head>' in line and not dtsg:
                data['fb_dtsg']=utils.getDtsg(line)
                break
        return data
