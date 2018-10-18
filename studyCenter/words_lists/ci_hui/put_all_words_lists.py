import requests


class PutAllWordsListsDone(object):
    def __init__(self, common, headers, accesstoken):
        self.headers = headers
        self.baseUrl = common.get('baseUrl')
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        self.accesstoken = accesstoken
        self.headers.update({"accesstoken": self.accesstoken})

    def put_all_words_lists_done(self, d):
        if d.get("currStatus") == 0:
            url = "{}/userVoc/{}/{}/vocStatus".format(self.baseUrl, d.get('taskID'), d.get('groupID'))
            response = requests.request("PUT", url, headers=self.headers)
            return response
        if d.get("currStatus") == 1:
            pass


if __name__ == '__main__':
    test = PutAllWordsListsDone()
    r = test.put_all_words_lists_done(34487, 2611)
    print(r)