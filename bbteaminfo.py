from xml.etree import ElementTree as bbTree

class TeamInfo():
    teams = {}

def addTeamInfo(root, teams):
    teamID = ''
    for child in root.iter():
        if child.tag == 'team':
            teamID = child.attrib['id']
            teams[teamID] = {}
        else:
            if child.tag == 'teamName':
                teams[teamID]['longName'] = child.text
            elif child.tag == 'shortName':
                teams[teamID]['shortName'] = child.text
            elif child.tag == 'owner':
                teams[teamID]['Owner'] = child.text
            elif child.tag == 'league':
                teams[teamID]['league_id'] = child.attrib['id']
                teams[teamID]['league_level'] = child.attrib['level']
                teams[teamID]['league_name'] = child.text
            elif child.tag == 'country':
                teams[teamID]['country_id'] = child.attrib['id']
                teams[teamID]['country_name'] = child.text
            elif child.tag == 'rival':
                teams[teamID]['rival_id'] = child.attrib['id']
                teams[teamID]['rival_name'] = child.text

    return teams

def getTeamInfo(bbSession, bbapiurl):
    page = '/teaminfo.aspx'

    teaminfo = bbSession.get(bbapiurl + page)
    root = bbTree.fromstring(teaminfo.content)

    return root

def printTeamInfo(teams):
    for k,v in teams.items():
        print(k)
        for k,v in teams[k].items():
            print(k,v)

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
