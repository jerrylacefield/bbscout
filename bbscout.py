import requests
from xml.etree import ElementTree as bbTree
import bblogin
import bbteaminfo as myteam

# bbapi session defined
bbapiurl = 'http://bbapi.buzzerbeater.com/'
bbSession = requests.Session()

# bbapi login
user = bblogin.makeAccount()
loginroot = bblogin.openBB(bbSession, bbapiurl, user)
loginSuccess = bblogin.isLoggedIn(loginroot)
print(user)
if loginSuccess:
    print('Welcome,',bblogin.getMyLoginName(user))

# Read teaminfo.aspx page
myTeam = {}
myTeamRoot = myteam.getTeamInfo(bbSession, bbapiurl)
myTeam = myteam.addTeamInfo(myTeamRoot, myTeam)
myteam.printTeamInfo(myTeam)

# bbapi logout
logoutroot = bblogin.closeBB(bbSession, bbapiurl)
loginSuccess = bblogin.isLoggedOut(logoutroot)
