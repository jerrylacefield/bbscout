from xml.etree import ElementTree as bbTree

def getTeamInfo(bbSession, bbapiurl):
    page = '/teaminfo.aspx'

    teaminfo = bbSession.get(bbapiurl + page)
    root = bbTree.fromstring(teaminfo.content)

    return root

def writeTeamInfo(myTeamRoot, myTeam):
    for child in myTeamRoot.iter():
        if (child.tag == 'team'):
            myTeam['id'] = child.attrib['id']
        elif (child.tag == 'teamName'):
            myTeam['teamLong'] = child.text
        elif (child.tag == 'shortName'):
            myTeam['shortName'] = child.text
        elif (child.tag == 'owner'):
            myTeam['Owner'] = child.text
        elif (child.tag == 'league'):
            myTeam['league_id'] = child.attrib['id']
            myTeam['league_level'] = child.attrib['level']
            myTeam['league_name'] = child.text
        elif (child.tag == 'country'):
            myTeam['country_id'] = child.attrib['id']
            myTeam['country_Name'] = child.text
        elif (child.tag == 'rival'):
            myTeam['rival_id'] = child.attrib['id']
            myTeam['rival_Name'] = child.text

    return myTeam
