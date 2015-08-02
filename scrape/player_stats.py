import json
import urllib2

class PlayerData:
    def __init__(self, player_id):
        self.player_id = player_id

        self._shot_logs_url = base_url = "http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID="+player_id+"&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="
        self._shot_logs_response = urllib2.urlopen(self._shot_logs_url)
        self._shot_logs_data = json.loads(self._shot_logs_response.read())

    def shot_logs(self):
        # won't have player id
        _headers = self._pbp_data['resultSets'][0]['headers']
        _rows = self._pbp_data['resultSets'][0]['rowSet']
        return [dict(zip(_headers, row)) for row in _rows]
