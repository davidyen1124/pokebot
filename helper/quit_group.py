import utils

uri = 'https://www.facebook.com/ajax/groups/membership/leave.php?group_id={0}'


class SpamGroup:
    def __init__(self, session, my_id):
        self.session = session
        self.my_id = my_id

    def quitGroup(self, group_id=None):
        if not group_id:
            return
        request = self.session.get('https://www.facebook.com/bookmarks/groups')
        data = self.__getFormDatas(request.content)
        data['prevent_readd'] = 'on'
        data['confirmed'] = '1'
        data['__user'] = self.my_id
        data['__a'] = '1'
        data['__req'] = 'e'
        data['phstamp'] = utils.getPhstamp(data, data['fb_dtsg'])

        request = self.session.post(uri.format(group_id), data=data)

    def __getFormDatas(self, content):
        data = {}
        for line in content.split('\n'):
            if '<head>' in line:
                data['fb_dtsg'] = utils.getDtsg(line)
                break
        return data
