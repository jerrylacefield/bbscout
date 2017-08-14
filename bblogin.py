import requests
import getpass
import bblogin_credentials as mylogin
import bblogin_errors as loginError
from xml.etree import ElementTree as bbTree

# calls BB logout.aspx, returns root
def closeBB(bbSession, bbapiurl):
    r = bbSession.get(bbapiurl + 'logout.aspx')
    root = bbTree.fromstring(r.content)

    return root

# open a Buzzerbeater Session, saves cookie, returns XML root
def openBB(bbSession, bbapiurl, user):
    # loggedIn = False
    failedAttempts = 0
    while True and failedAttempts < 5:
        try:
            ln = input('Enter Buzzerbeater Login Name: ')
            ac = getpass.getpass('Enter Buzzerbeater Access Code: ')

            user.setLoginName(ln)  # store login name to user account object

            r = bbSession.get(bbapiurl + 'login.aspx?login=' + user.loginname + '&code=' + ac)
            root = bbTree.fromstring(r.content)

            ac = '' # overwrite login access code

            if isLoggedIn(root):
                loggedIn = True
                break
            else:
                failedAttempts += 1
                if failedAttempts < 3:
                    raise loginError.InvalidLogin
                else:
                    raise loginError.TooManyBadAttempts

        except loginError.InvalidLogin:
            print('Invalid Login Name / Access Code combination')
            print('Try Again ...')
            continue
        except loginError.TooManyBadAttempts:
            print("Too many failed attempts ... exiting BB Scout")
            break

    return root

# test if login procedure called correctly, returns boolean
def isLoggedIn(root):
    loggedIn = False
    for child in root.findall('loggedIn'):
        if child.tag == 'loggedIn':
            loggedIn = True
            break

    return loggedIn

# test if logout procedure called correctly, returns boolean
def isLoggedOut(root):
    loggedOut = False
    for child in root.findall('loggedOut'):
        if child.tag == 'loggedOut':
            loggedOut = True
            break

    return loggedOut

# retrieves the login name from the user account object
def getMyLoginName(user):
    myName = user.getLoginName()

    return myName

# function to make the account object, returns object
def makeAccount():
    ln = ''
    user = mylogin.Account(ln)

    return user
