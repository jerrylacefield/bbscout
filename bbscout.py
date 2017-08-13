import requests
from xml.etree import ElementTree as bbTree
import bblogin
import bbteaminfo as myteam

bbapiurl = 'http://bbapi.buzzerbeater.com/'
bbSession = requests.Session()

loginroot = bblogin.openBB(bbSession, bbapiurl)
loginSuccess = bblogin.isAuthorized(loginroot)

# Read teaminfo.aspx page
myTeam = {}
myTeamRoot = myteam.getTeamInfo(bbSession, bbapiurl)
myTeam = myteam.addTeamInfo(myTeamRoot, myTeam)
myteam.printTeamInfo(myTeam)
