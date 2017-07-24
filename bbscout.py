import requests
from xml.etree import ElementTree as bbTree
import bblogin

bbSession = requests.Session()
root = bblogin.openBB(bbSession)
loginSuccess = bblogin.isAuthorized(root)
print(loginSuccess)
