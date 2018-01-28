from boring_stuff import webScraping as web

#web.browse("http://www.google.com")
web.downloadPage(url='http://docs.python-requests.org/en/master/user/quickstart/#response-content', params={'a':'1', 'b':'2'}, output='test.txt')