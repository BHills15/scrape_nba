import json
import urllib2

import helper

class SportVuData:
    def __init__(self):
        self.touches_team_url = "http://stats.nba.com/js/data/sportvu/2014/touchesTeamData.json"
        self.defense_team_url = "http://stats.nba.com/js/data/sportvu/2014/defenseTeamData.json"
        self.drives_team_url = "http://stats.nba.com/js/data/sportvu/2014/drivesTeamData.json"
        self.passing_team_url = "http://stats.nba.com/js/data/sportvu/2014/passingTeamData.json"
        self.pull_up_shoot_team_url = "http://stats.nba.com/js/data/sportvu/2014/pullUpShootTeamData.json"
        self.rebounding_team_url = "http://stats.nba.com/js/data/sportvu/2014/reboundingTeamData.json"
        self.shooting_team_url = "http://stats.nba.com/js/data/sportvu/2014/shootingTeamData.json"
        self.speed_team_url = "http://stats.nba.com/js/data/sportvu/2014/speedTeamData.json"
        self.catch_shoot_team_url = "http://stats.nba.com/js/data/sportvu/2014/catchShootTeamData.json"
        self.touches_url = "http://stats.nba.com/js/data/sportvu/2014/touchesData.json"
        self.defense_url = "http://stats.nba.com/js/data/sportvu/2014/defenseData.json"
        self.drives_url = "http://stats.nba.com/js/data/sportvu/2014/drivesData.json"
        self.passing_url = "http://stats.nba.com/js/data/sportvu/2014/passingData.json"
        self.pull_up_shoot_url = "http://stats.nba.com/js/data/sportvu/2014/pullUpShootData.json"
        self.rebounding_url = "http://stats.nba.com/js/data/sportvu/2014/reboundingData.json"
        self.shooting_url = "http://stats.nba.com/js/data/sportvu/2014/shootingData.json"
        self.speed_url = "http://stats.nba.com/js/data/sportvu/2014/speedData.json"
        self.catch_shoot_url = "http://stats.nba.com/js/data/sportvu/2014/catchShootData.json"

    def touches_team(self):
        return helper.get_data_from_url(self.touches_team_url, 0)

    def defense_team(self):
        return helper.get_data_from_url(self.defense_team_url, 0)

    def drives_team(self):
        return helper.get_data_from_url(self.drives_team_url, 0)

    def passing_team(self):
        return helper.get_data_from_url(self.passing_team_url, 0)

    def pull_up_shoot_team(self):
        return helper.get_data_from_url(self.pull_up_shoot_team_url, 0)

    def rebounding_team(self):
        return helper.get_data_from_url(self.rebounding_team_url, 0)

    def shooting_team(self):
        return helper.get_data_from_url(self.shooting_team_url, 0)

    def speed_team(self):
        return helper.get_data_from_url(self.speed_team_url, 0)

    def catch_shoot_team(self):
        return helper.get_data_from_url(self.catch_shoot_team_url, 0)

    def touches(self):
        return helper.get_data_from_url(self.touches_url, 0)

    def defense(self):
        return helper.get_data_from_url(self.defense_url, 0)

    def drives(self):
        return helper.get_data_from_url(self.drives_url, 0)

    def passing(self):
        return helper.get_data_from_url(self.passing_url, 0)

    def pull_up_shoot(self):
        return helper.get_data_from_url(self.pull_up_shoot_url, 0)

    def rebounding(self):
        return helper.get_data_from_url(self.rebounding_url, 0)

    def shooting(self):
        return helper.get_data_from_url(self.shooting_url, 0)

    def speed(self):
        return helper.get_data_from_url(self.speed_url, 0)

    def catch_shoot(self):
        return helper.get_data_from_url(self.catch_shoot_url, 0)
