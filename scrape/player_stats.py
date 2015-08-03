import json
import urllib2

class PlayerData:
    def __init__(self, player_id):
        self.player_id = player_id

        self.shot_logs_url = "http://stats.nba.com/stats/playerdashptshotlog?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID="+player_id+"&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="
        self.shot_logs_response = urllib2.urlopen(self.shot_logs_url)
        self.shot_logs_data = json.loads(self.shot_logs_response.read())

        self.rebound_logs_url = "http://stats.nba.com/stats/playerdashptreboundlogs?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID="+player_id+"&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="
        self.rebound_logs_response = urllib2.urlopen(self.rebound_logs_url)
        self.rebound_logs_data = json.loads(self.rebound_logs_response.read())

        self.passes_url = "http://stats.nba.com/stats/playerdashptpass?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=0&PlayerID="+player_id+"&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision="
        self.passes_response = urllib2.urlopen(self.passes_url)
        self.passes_data = json.loads(self.passes_response.read())

    def shot_logs(self):
        headers = self.shot_logs_data['resultSets'][0]['headers']
        headers = ["PLAYER_ID"] + headers
        rows = self.shot_logs_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, [self.player_id] + row)) for row in rows]

    def rebound_logs(self):
        headers = self.rebound_logs_data['resultSets'][0]['headers']
        headers = ["PLAYER_ID"] + headers
        rows = self.rebound_logs_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, [self.player_id] + row)) for row in rows]

    def passes_made(self):
        headers = self.passes_data['resultSets'][0]['headers']
        rows = self.passes_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def passes_received(self):
        headers = self.passes_data['resultSets'][1]['headers']
        rows = self.passes_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]
