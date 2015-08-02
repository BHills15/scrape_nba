import json
import urllib2

PBP_BASE_URL = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=<game_id>&RangeType=2&Season=2014-15&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"

def getGameData(game_id):
    url = PBP_BASE_URL.replace("<game_id>", game_id)
        
    response = urllib2.urlopen(url)
    data = json.loads(response.read())

    game_info = []
    plays = []
    for line in data['resultSets']:
        if 'name' in line.keys() and line['name'] == 'PlayByPlay':
            for event in line['rowSet']:
                row = dict(zip([header for header in line['headers']],event))
                plays.append(row)

    return plays