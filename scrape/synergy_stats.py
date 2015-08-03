import json
import urllib2

class SynergyData:
    def __init__(self):
        self.transition_team_url = "http://stats.nba.com/js/data/playtype/team_Transition.js"
        self.transition_team_response = urllib2.urlopen(self.transition_team_url)
        self.transition_team_data = json.loads(self.transition_team_response.read())

        self.transition_url = "http://stats.nba.com/js/data/playtype/player_Transition.js"
        self.transition_response = urllib2.urlopen(self.transition_url)
        self.transition_data = json.loads(self.transition_response.read())

        self.isolation_team_url = "http://stats.nba.com/js/data/playtype/team_Isolation.js"
        self.isolation_team_response = urllib2.urlopen(self.isolation_team_url)
        self.isolation_team_data = json.loads(self.isolation_team_response.read())

        self.isolation_url = "http://stats.nba.com/js/data/playtype/player_Isolation.js"
        self.isolation_response = urllib2.urlopen(self.isolation_url)
        self.isolation_data = json.loads(self.isolation_response.read())

        self.pr_ball_handler_team_url = "http://stats.nba.com/js/data/playtype/team_PRBallHandler.js"
        self.pr_ball_handler_team_response = urllib2.urlopen(self.pr_ball_handler_team_url)
        self.pr_ball_handler_team_data = json.loads(self.pr_ball_handler_team_response.read())

        self.pr_ball_handler_url = "http://stats.nba.com/js/data/playtype/player_PRBallHandler.js"
        self.pr_ball_handler_response = urllib2.urlopen(self.pr_ball_handler_url)
        self.pr_ball_handler_data = json.loads(self.pr_ball_handler_response.read())

        self.pr_roll_man_team_url = "http://stats.nba.com/js/data/playtype/team_PRRollMan.js"
        self.pr_roll_man_team_response = urllib2.urlopen(self.pr_roll_man_team_url)
        self.pr_roll_man_team_data = json.loads(self.pr_roll_man_team_response.read())

        self.pr_roll_man_url = "http://stats.nba.com/js/data/playtype/player_PRRollMan.js"
        self.pr_roll_man_response = urllib2.urlopen(self.pr_roll_man_url)
        self.pr_roll_man_data = json.loads(self.pr_roll_man_response.read())

        self.post_up_team_url = "http://stats.nba.com/js/data/playtype/team_Postup.js"
        self.post_up_team_response = urllib2.urlopen(self.post_up_team_url)
        self.post_up_team_data = json.loads(self.post_up_team_response.read())

        self.post_up_url = "http://stats.nba.com/js/data/playtype/player_Postup.js"
        self.post_up_response = urllib2.urlopen(self.post_up_url)
        self.post_up_data = json.loads(self.post_up_response.read())

        self.spot_up_team_url = "http://stats.nba.com/js/data/playtype/team_Spotup.js"
        self.spot_up_team_response = urllib2.urlopen(self.spot_up_team_url)
        self.spot_up_team_data = json.loads(self.spot_up_team_response.read())

        self.spot_up_url = "http://stats.nba.com/js/data/playtype/player_Spotup.js"
        self.spot_up_response = urllib2.urlopen(self.spot_up_url)
        self.spot_up_data = json.loads(self.spot_up_response.read())

        self.handoff_team_url = "http://stats.nba.com/js/data/playtype/team_Handoff.js"
        self.handoff_team_response = urllib2.urlopen(self.handoff_team_url)
        self.handoff_team_data = json.loads(self.handoff_team_response.read())

        self.handoff_url = "http://stats.nba.com/js/data/playtype/player_Handoff.js"
        self.handoff_response = urllib2.urlopen(self.handoff_url)
        self.handoff_data = json.loads(self.handoff_response.read())

        self.cut_team_url = "http://stats.nba.com/js/data/playtype/team_Cut.js"
        self.cut_team_response = urllib2.urlopen(self.cut_team_url)
        self.cut_team_data = json.loads(self.cut_team_response.read())

        self.cut_url = "http://stats.nba.com/js/data/playtype/player_Cut.js"
        self.cut_response = urllib2.urlopen(self.cut_url)
        self.cut_data = json.loads(self.cut_response.read())

        self.off_screen_team_url = "http://stats.nba.com/js/data/playtype/team_OffScreen.js"
        self.off_screen_team_response = urllib2.urlopen(self.off_screen_team_url)
        self.off_screen_team_data = json.loads(self.off_screen_team_response.read())

        self.off_screen_url = "http://stats.nba.com/js/data/playtype/player_OffScreen.js"
        self.off_screen_response = urllib2.urlopen(self.off_screen_url)
        self.off_screen_data = json.loads(self.off_screen_response.read())

        self.put_back_team_url = "http://stats.nba.com/js/data/playtype/team_OffRebound.js"
        self.put_back_team_response = urllib2.urlopen(self.put_back_team_url)
        self.put_back_team_data = json.loads(self.put_back_team_response.read())

        self.put_back_url = "http://stats.nba.com/js/data/playtype/player_OffRebound.js"
        self.put_back_response = urllib2.urlopen(self.put_back_url)
        self.put_back_data = json.loads(self.put_back_response.read())

        self.misc_team_url = "http://stats.nba.com/js/data/playtype/team_Misc.js"
        self.misc_team_response = urllib2.urlopen(self.misc_team_url)
        self.misc_team_data = json.loads(self.misc_team_response.read())

        self.misc_url = "http://stats.nba.com/js/data/playtype/player_Misc.js"
        self.misc_response = urllib2.urlopen(self.misc_url)
        self.misc_data = json.loads(self.misc_response.read())

    def transition_team_offense(self):
        headers = self.transition_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.transition_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def transition_team_defense(self):
        headers = self.transition_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.transition_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def transition_offense(self):
        headers = self.transition_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.transition_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def isolation_team_offense(self):
        headers = self.isolation_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.isolation_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def isolation_team_defense(self):
        headers = self.isolation_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.isolation_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def isolation_offense(self):
        headers = self.isolation_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.isolation_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def isolation_defense(self):
        headers = self.isolation_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.isolation_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_ball_handler_team_offense(self):
        headers = self.pr_ball_handler_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_ball_handler_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_ball_handler_team_defense(self):
        headers = self.pr_ball_handler_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_ball_handler_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_ball_handler_offense(self):
        headers = self.pr_ball_handler_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_ball_handler_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_ball_handler_defense(self):
        headers = self.pr_ball_handler_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_ball_handler_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_roll_man_team_offense(self):
        headers = self.pr_roll_man_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_roll_man_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_roll_man_team_defense(self):
        headers = self.pr_roll_man_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_roll_man_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_roll_man_offense(self):
        headers = self.pr_roll_man_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_roll_man_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def pr_roll_man_defense(self):
        headers = self.pr_roll_man_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.pr_roll_man_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def post_up_team_offense(self):
        headers = self.post_up_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.post_up_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def post_up_team_defense(self):
        headers = self.post_up_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.post_up_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def post_up_offense(self):
        headers = self.post_up_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.post_up_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def post_up_defense(self):
        headers = self.post_up_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.post_up_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def spot_up_team_offense(self):
        headers = self.spot_up_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.spot_up_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def spot_up_team_defense(self):
        headers = self.spot_up_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.spot_up_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def spot_up_offense(self):
        headers = self.spot_up_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.spot_up_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def spot_up_defense(self):
        headers = self.spot_up_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.spot_up_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def handoff_team_offense(self):
        headers = self.handoff_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.handoff_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def handoff_team_defense(self):
        headers = self.handoff_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.handoff_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def handoff_offense(self):
        headers = self.handoff_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.handoff_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def handoff_defense(self):
        headers = self.handoff_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.handoff_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def cut_team_offense(self):
        headers = self.cut_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.cut_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def cut_team_defense(self):
        headers = self.cut_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.cut_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def cut_offense(self):
        headers = self.cut_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.cut_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def off_screen_team_offense(self):
        headers = self.off_screen_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.off_screen_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def off_screen_team_defense(self):
        headers = self.off_screen_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.off_screen_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def off_screen_offense(self):
        headers = self.off_screen_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.off_screen_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def off_screen_defense(self):
        headers = self.off_screen_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.off_screen_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def put_back_team_offense(self):
        headers = self.put_back_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.put_back_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def put_back_team_defense(self):
        headers = self.put_back_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.put_back_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def put_back_offense(self):
        headers = self.put_back_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.put_back_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def misc_team_offense(self):
        headers = self.misc_team_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.misc_team_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def misc_team_defense(self):
        headers = self.misc_team_data['resultSets'][1]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.misc_team_data['resultSets'][1]['rowSet']
        return [dict(zip(headers, row)) for row in rows]

    def misc_offense(self):
        headers = self.misc_data['resultSets'][0]['headers']
        headers = ["FG_m" if x=="FGm" else x for x in headers]
        headers = ["FG_mG" if x=="FGmG" else x for x in headers]
        rows = self.misc_data['resultSets'][0]['rowSet']
        return [dict(zip(headers, row)) for row in rows]
