import json
import urllib2

class SportVuData:
    def __init__(self):
        self.touches_team_url = "http://stats.nba.com/js/data/sportvu/2014/touchesTeamData.json"
        self.touches_team_response = urllib2.urlopen(self.touches_team_url)
        self.touches_team_data = json.loads(self.touches_team_response.read())

        self.defense_team_url = "http://stats.nba.com/js/data/sportvu/2014/defenseTeamData.json"
        self.defense_team_response = urllib2.urlopen(self.defense_team_url)
        self.defense_team_data = json.loads(self.defense_team_response.read())

        self.drives_team_url = "http://stats.nba.com/js/data/sportvu/2014/drivesTeamData.json"
        self.drives_team_response = urllib2.urlopen(self.drives_team_url)
        self.drives_team_data = json.loads(self.drives_team_response.read())

        self.passing_team_url = "http://stats.nba.com/js/data/sportvu/2014/passingTeamData.json"
        self.passing_team_response = urllib2.urlopen(self.passing_team_url)
        self.passing_team_data = json.loads(self.passing_team_response.read())

        self.pull_up_shoot_team_url = "http://stats.nba.com/js/data/sportvu/2014/pullUpShootTeamData.json"
        self.pull_up_shoot_team_response = urllib2.urlopen(self.pull_up_shoot_team_url)
        self.pull_up_shoot_team_data = json.loads(self.pull_up_shoot_team_response.read())

        self.rebounding_team_url = "http://stats.nba.com/js/data/sportvu/2014/reboundingTeamData.json"
        self.rebounding_team_response = urllib2.urlopen(self.rebounding_team_url)
        self.rebounding_team_data = json.loads(self.rebounding_team_response.read())

        self.shooting_team_url = "http://stats.nba.com/js/data/sportvu/2014/shootingTeamData.json"
        self.shooting_team_response = urllib2.urlopen(self.shooting_team_url)
        self.shooting_team_data = json.loads(self.shooting_team_response.read())

        self.speed_team_url = "http://stats.nba.com/js/data/sportvu/2014/speedTeamData.json"
        self.speed_team_response = urllib2.urlopen(self.speed_team_url)
        self.speed_team_data = json.loads(self.speed_team_response.read())

        self.catch_shoot_team_url = "http://stats.nba.com/js/data/sportvu/2014/catchShootTeamData.json"
        self.catch_shoot_team_response = urllib2.urlopen(self.catch_shoot_team_url)
        self.catch_shoot_team_data = json.loads(self.catch_shoot_team_response.read())

        self.touches_url = "http://stats.nba.com/js/data/sportvu/2014/touchesData.json"
        self.touches_response = urllib2.urlopen(self.touches_url)
        self.touches_data = json.loads(self.touches_response.read())

        self.defense_url = "http://stats.nba.com/js/data/sportvu/2014/defenseData.json"
        self.defense_response = urllib2.urlopen(self.defense_url)
        self.defense_data = json.loads(self.defense_response.read())

        self.drives_url = "http://stats.nba.com/js/data/sportvu/2014/drivesData.json"
        self.drives_response = urllib2.urlopen(self.drives_url)
        self.drives_data = json.loads(self.drives_response.read())

        self.passing_url = "http://stats.nba.com/js/data/sportvu/2014/passingData.json"
        self.passing_response = urllib2.urlopen(self.passing_url)
        self.passing_data = json.loads(self.passing_response.read())

        self.pull_up_shoot_url = "http://stats.nba.com/js/data/sportvu/2014/pullUpShootData.json"
        self.pull_up_shoot_response = urllib2.urlopen(self.pull_up_shoot_url)
        self.pull_up_shoot_data = json.loads(self.pull_up_shoot_response.read())

        self.rebounding_url = "http://stats.nba.com/js/data/sportvu/2014/reboundingData.json"
        self.rebounding_response = urllib2.urlopen(self.rebounding_url)
        self.rebounding_data = json.loads(self.rebounding_response.read())

        self.shooting_url = "http://stats.nba.com/js/data/sportvu/2014/shootingData.json"
        self.shooting_response = urllib2.urlopen(self.shooting_url)
        self.shooting_data = json.loads(self.shooting_response.read())

        self.speed_url = "http://stats.nba.com/js/data/sportvu/2014/speedData.json"
        self.speed_response = urllib2.urlopen(self.speed_url)
        self.speed_data = json.loads(self.speed_response.read())

        self.catch_shoot_url = "http://stats.nba.com/js/data/sportvu/2014/catchShootData.json"
        self.catch_shoot_response = urllib2.urlopen(self.catch_shoot_url)
        self.catch_shoot_data = json.loads(self.catch_shoot_response.read())


    def touches_team(self):
        headers = self.touches_team_data['resultSets'][0]['headers']
        rows = self.touches_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def defense_team(self):
        headers = self.defense_team_data['resultSets'][0]['headers']
        rows = self.defense_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def drives_team(self):
        headers = self.drives_team_data['resultSets'][0]['headers']
        rows = self.drives_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def passing_team(self):
        headers = self.passing_team_data['resultSets'][0]['headers']
        rows = self.passing_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pull_up_shoot_team(self):
        headers = self.pull_up_shoot_team_data['resultSets'][0]['headers']
        rows = self.pull_up_shoot_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def rebounding_team(self):
        headers = self.rebounding_team_data['resultSets'][0]['headers']
        rows = self.rebounding_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def shooting_team(self):
        headers = self.shooting_team_data['resultSets'][0]['headers']
        rows = self.shooting_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def speed_team(self):
        headers = self.speed_team_data['resultSets'][0]['headers']
        rows = self.speed_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def catch_shoot_team(self):
        headers = self.catch_shoot_team_data['resultSets'][0]['headers']
        rows = self.catch_shoot_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def touches(self):
        headers = self.touches_data['resultSets'][0]['headers']
        rows = self.touches_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def defense(self):
        headers = self.defense_data['resultSets'][0]['headers']
        rows = self.defense_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def drives(self):
        headers = self.drives_data['resultSets'][0]['headers']
        rows = self.drives_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def passing(self):
        headers = self.passing_data['resultSets'][0]['headers']
        rows = self.passing_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pull_up_shoot(self):
        headers = self.pull_up_shoot_data['resultSets'][0]['headers']
        rows = self.pull_up_shoot_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def rebounding(self):
        headers = self.rebounding_data['resultSets'][0]['headers']
        rows = self.rebounding_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def shooting(self):
        headers = self.shooting_data['resultSets'][0]['headers']
        rows = self.shooting_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def speed(self):
        headers = self.speed_data['resultSets'][0]['headers']
        rows = self.speed_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def catch_shoot(self):
        headers = self.catch_shoot_data['resultSets'][0]['headers']
        rows = self.catch_shoot_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]
