import requests
from xml.etree import ElementTree as bbTree

def openBB(bbSession):
    r = bbSession.get('http://bbapi.buzzerbeater.com/login.aspx?login=kaygdanimal&code=seminoles')
    root = bbTree.fromstring(r.content)

    return root

def isAuthorized(root):
    for child in root.findall('loggedIn'):
        loggedin = child.find('1')

        if loggedin is None:
            return 1
        else:
            return 0
