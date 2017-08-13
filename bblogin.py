import requests
import getpass
from xml.etree import ElementTree as bbTree

class Account:
    def __init__(self, ln, ac):
        self.loginname = ln
        self.accesscode = ac

def openBB(bbSession, bbapiurl):
    # Get user login name and access code
    # clear-text format for access code
    ln = input('Enter Buzzerbeater Login Name: ')
    ac = getpass.getpass('Enter Buzzerbeater Access Code: ')

    # create user Account object
    user = Account(ln, ac)

    # Login to Buzzerbeater API
    r = bbSession.get(bbapiurl + 'login.aspx?login=' + user.loginname + '&code=' + user.accesscode)
    root = bbTree.fromstring(r.content)

    return root

def isAuthorized(root):
    for child in root.findall('loggedIn'):
        loggedin = child.find('1')

        if loggedin is None:
            return 1
        else:
            return 0
