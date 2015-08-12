import MySQLdb
import time

class Storage:
    def __init__(self, host, user, pw, db):
        self._host=host
        self._user=user
        self._pw=pw
        self._db=db
        self.conn = MySQLdb.connect(host, user, pw, db)

    def insert(self, data, table_name):
        for line in data:
            headers = [key for key,val in sorted(line.items())]
            quoted_values = ['"%s"' % (val) for key,val in sorted(line.items())]
            duplicate_key_clauses = ['`%s`="%s"' % (key,val) for key,val in sorted(line.items())]
            for i in range(len(headers)):
                headers[i] = "`" + headers[i] + "`"
            self.query("""
                INSERT INTO %s
                (%s)
                VALUES (%s)
                ON DUPLICATE KEY UPDATE
                %s
            """ % (table_name, ','.join(headers), ','.join(quoted_values),','.join(duplicate_key_clauses)))

    def insert_with_date(self, data, table_name):
        for line in data:
            line['DATE'] = time.strftime("%Y-%m-%d")
            headers = [key for key,val in sorted(line.items())]
            quoted_values = ['"%s"' % (val) for key,val in sorted(line.items())]
            duplicate_key_clauses = ['`%s`="%s"' % (key,val) for key,val in sorted(line.items())]
            for i in range(len(headers)):
                headers[i] = "`" + headers[i] + "`"
            self.query("""
                INSERT INTO %s
                (%s)
                VALUES (%s)
                ON DUPLICATE KEY UPDATE
                %s
            """ % (table_name, ','.join(headers), ','.join(quoted_values),','.join(duplicate_key_clauses)))

    def close(self):
        return self.conn.close()

    def query(self, sql):
        curs = self.curs()
        curs.execute(sql)

        return curs.fetchall()

    def curs(self):
        return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

class Db:
    def __init__(self, host, user, pw, db):
        self._host=host
        self._user=user
        self._pw=pw
        self._db=db

    def create_db(self):
        conn = MySQLdb.connect(host=self._host, user=self._user, passwd=self._pw)
        cursor = conn.cursor()
        query = 'CREATE DATABASE IF NOT EXISTS ' + self._db
        cursor.execute(query)
        conn.close()

    def create_tables(self):
        conn = MySQLdb.connect(host=self._host, user=self._user, passwd=self._pw, db=self._db)
        cursor = conn.cursor()
        pbp_query = 'CREATE TABLE IF NOT EXISTS pbp\
        (\
        GAME_ID VARCHAR(255),\
        EVENTNUM INT,\
        EVENTMSGTYPE INT,\
        EVENTMSGACTIONTYPE INT,\
        PERIOD INT,\
        WCTIMESTRING VARCHAR(255),\
        PCTIMESTRING VARCHAR(255),\
        HOMEDESCRIPTION VARCHAR(255),\
        NEUTRALDESCRIPTION VARCHAR(255),\
        VISITORDESCRIPTION VARCHAR(255),\
        SCORE VARCHAR(255),\
        SCOREMARGIN VARCHAR(255),\
        PERSON1TYPE VARCHAR(255),\
        PLAYER1_ID INT,\
        PLAYER1_NAME VARCHAR(255),\
        PLAYER1_TEAM_ID VARCHAR(255),\
        PLAYER1_TEAM_CITY VARCHAR(255),\
        PLAYER1_TEAM_NICKNAME VARCHAR(255),\
        PLAYER1_TEAM_ABBREVIATION VARCHAR(255),\
        PERSON2TYPE VARCHAR(255),\
        PLAYER2_ID INT,\
        PLAYER2_NAME VARCHAR(255),\
        PLAYER2_TEAM_ID VARCHAR(255),\
        PLAYER2_TEAM_CITY VARCHAR(255),\
        PLAYER2_TEAM_NICKNAME VARCHAR(255),\
        PLAYER2_TEAM_ABBREVIATION VARCHAR(255),\
        PERSON3TYPE VARCHAR(255),\
        PLAYER3_ID INT,\
        PLAYER3_NAME VARCHAR(255),\
        PLAYER3_TEAM_ID VARCHAR(255),\
        PLAYER3_TEAM_CITY VARCHAR(255),\
        PLAYER3_TEAM_NICKNAME VARCHAR(255),\
        PLAYER3_TEAM_ABBREVIATION VARCHAR(255),\
        HOME_PLAYER1 VARCHAR(255),\
        HOME_PLAYER2 VARCHAR(255),\
        HOME_PLAYER3 VARCHAR(255),\
        HOME_PLAYER4 VARCHAR(255),\
        HOME_PLAYER5 VARCHAR(255),\
        VISITOR_PLAYER1 VARCHAR(255),\
        VISITOR_PLAYER2 VARCHAR(255),\
        VISITOR_PLAYER3 VARCHAR(255),\
        VISITOR_PLAYER4 VARCHAR(255),\
        VISITOR_PLAYER5 VARCHAR(255),\
        PRIMARY KEY(GAME_ID, EVENTNUM)\
        );'
        cursor.execute(pbp_query)

        shots_query = 'CREATE TABLE IF NOT EXISTS shots\
        (\
        GRID_TYPE VARCHAR(255),\
        GAME_ID VARCHAR(255),\
        GAME_EVENT_ID INT,\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        PERIOD INT,\
        MINUTES_REMAINING INT,\
        SECONDS_REMAINING INT,\
        EVENT_TYPE VARCHAR(255),\
        ACTION_TYPE VARCHAR(255),\
        SHOT_TYPE VARCHAR(255),\
        SHOT_ZONE_BASIC VARCHAR(255),\
        SHOT_ZONE_AREA VARCHAR(255),\
        SHOT_ZONE_RANGE VARCHAR(255),\
        SHOT_DISTANCE INT,\
        LOC_X INT,\
        LOC_Y INT,\
        SHOT_ATTEMPTED_FLAG BOOLEAN,\
        SHOT_MADE_FLAG BOOLEAN,\
        PRIMARY KEY(GAME_ID, GAME_EVENT_ID)\
        );'
        cursor.execute(shots_query)

        advanced_boxscores_query = 'CREATE TABLE IF NOT EXISTS advanced_boxscores\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        START_POSITION VARCHAR(255),\
        COMMENT VARCHAR(255),\
        MIN VARCHAR(255),\
        OFF_RATING DOUBLE,\
        DEF_RATING DOUBLE,\
        NET_RATING DOUBLE,\
        AST_PCT DOUBLE,\
        AST_TOV DOUBLE,\
        AST_RATIO DOUBLE,\
        OREB_PCT DOUBLE,\
        DREB_PCT DOUBLE,\
        REB_PCT DOUBLE,\
        TM_TOV_PCT DOUBLE,\
        EFG_PCT DOUBLE,\
        TS_PCT DOUBLE,\
        USG_PCT DOUBLE,\
        PACE DOUBLE,\
        PIE DOUBLE,\
        PRIMARY KEY(GAME_ID, PLAYER_ID)\
        );'
        cursor.execute(advanced_boxscores_query)

        advanced_boxscores_team_query = 'CREATE TABLE IF NOT EXISTS advanced_boxscores_team\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        MIN VARCHAR(255),\
        OFF_RATING DOUBLE,\
        DEF_RATING DOUBLE,\
        NET_RATING DOUBLE,\
        AST_PCT DOUBLE,\
        AST_TOV DOUBLE,\
        AST_RATIO DOUBLE,\
        OREB_PCT DOUBLE,\
        DREB_PCT DOUBLE,\
        REB_PCT DOUBLE,\
        TM_TOV_PCT DOUBLE,\
        EFG_PCT DOUBLE,\
        TS_PCT DOUBLE,\
        USG_PCT DOUBLE,\
        PACE DOUBLE,\
        PIE DOUBLE,\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(advanced_boxscores_team_query)

        traditional_boxscores_query = 'CREATE TABLE IF NOT EXISTS traditional_boxscores\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        START_POSITION VARCHAR(255),\
        COMMENT VARCHAR(255),\
        MIN VARCHAR(255),\
        FGM INT,\
        FGA INT,\
        FG_PCT DOUBLE,\
        FG3M INT,\
        FG3A INT,\
        FG3_PCT DOUBLE,\
        FTM INT,\
        FTA INT,\
        FT_PCT DOUBLE,\
        OREB INT,\
        DREB INT,\
        REB INT,\
        AST INT,\
        STL INT,\
        BLK INT,\
        `TO` INT,\
        PF INT,\
        PTS INT,\
        PLUS_MINUS INT,\
        PRIMARY KEY(GAME_ID, PLAYER_ID)\
        );'
        cursor.execute(traditional_boxscores_query)

        traditional_boxscores_team_query = 'CREATE TABLE IF NOT EXISTS traditional_boxscores_team\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        MIN VARCHAR(255),\
        FGM INT,\
        FGA INT,\
        FG_PCT DOUBLE,\
        FG3M INT,\
        FG3A INT,\
        FG3_PCT DOUBLE,\
        FTM INT,\
        FTA INT,\
        FT_PCT DOUBLE,\
        OREB INT,\
        DREB INT,\
        REB INT,\
        AST INT,\
        STL INT,\
        BLK INT,\
        `TO` INT,\
        PF INT,\
        PTS INT,\
        PLUS_MINUS INT,\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(traditional_boxscores_team_query)

        player_tracking_boxscores_query = 'CREATE TABLE IF NOT EXISTS player_tracking_boxscores\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        START_POSITION VARCHAR(255),\
        COMMENT VARCHAR(255),\
        MIN VARCHAR(255),\
        SPD DOUBLE,\
        DIST DOUBLE,\
        ORBC INT,\
        DRBC INT,\
        RBC INT,\
        TCHS INT,\
        SAST INT,\
        FTAST INT,\
        PASS INT,\
        AST INT,\
        CFGM INT,\
        CFGA INT,\
        CFG_PCT DOUBLE,\
        UFGM INT,\
        UFGA INT,\
        UFG_PCT DOUBLE,\
        FG_PCT DOUBLE,\
        DFGM INT,\
        DFGA INT,\
        DFG_PCT DOUBLE,\
        PRIMARY KEY(GAME_ID, PLAYER_ID)\
        );'
        cursor.execute(player_tracking_boxscores_query)

        player_tracking_boxscores_team_query = 'CREATE TABLE IF NOT EXISTS player_tracking_boxscores_team\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_NICKNAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        MIN VARCHAR(255),\
        SPD DOUBLE,\
        DIST DOUBLE,\
        ORBC INT,\
        DRBC INT,\
        RBC INT,\
        TCHS INT,\
        SAST INT,\
        FTAST INT,\
        PASS INT,\
        AST INT,\
        CFGM INT,\
        CFGA INT,\
        CFG_PCT DOUBLE,\
        UFGM INT,\
        UFGA INT,\
        UFG_PCT DOUBLE,\
        FG_PCT DOUBLE,\
        DFGM INT,\
        DFGA INT,\
        DFG_PCT DOUBLE,\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(player_tracking_boxscores_team_query)

        scoring_boxscores_query = 'CREATE TABLE IF NOT EXISTS scoring_boxscores\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        START_POSITION VARCHAR(255),\
        COMMENT VARCHAR(255),\
        MIN VARCHAR(255),\
        PCT_FGA_2PT DOUBLE,\
        PCT_FGA_3PT DOUBLE,\
        PCT_PTS_2PT DOUBLE,\
        PCT_PTS_2PT_MR DOUBLE,\
        PCT_PTS_3PT DOUBLE,\
        PCT_PTS_FB DOUBLE,\
        PCT_PTS_FT DOUBLE,\
        PCT_PTS_OFF_TOV DOUBLE,\
        PCT_PTS_PAINT DOUBLE,\
        PCT_AST_2PM DOUBLE,\
        PCT_UAST_2PM DOUBLE,\
        PCT_AST_3PM DOUBLE,\
        PCT_UAST_3PM DOUBLE,\
        PCT_AST_FGM DOUBLE,\
        PCT_UAST_FGM DOUBLE,\
        PRIMARY KEY(GAME_ID, PLAYER_ID)\
        );'
        cursor.execute(scoring_boxscores_query)

        scoring_boxscores_team_query = 'CREATE TABLE IF NOT EXISTS scoring_boxscores_team\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        MIN VARCHAR(255),\
        PCT_FGA_2PT DOUBLE,\
        PCT_FGA_3PT DOUBLE,\
        PCT_PTS_2PT DOUBLE,\
        PCT_PTS_2PT_MR DOUBLE,\
        PCT_PTS_3PT DOUBLE,\
        PCT_PTS_FB DOUBLE,\
        PCT_PTS_FT DOUBLE,\
        PCT_PTS_OFF_TOV DOUBLE,\
        PCT_PTS_PAINT DOUBLE,\
        PCT_AST_2PM DOUBLE,\
        PCT_UAST_2PM DOUBLE,\
        PCT_AST_3PM DOUBLE,\
        PCT_UAST_3PM DOUBLE,\
        PCT_AST_FGM DOUBLE,\
        PCT_UAST_FGM DOUBLE,\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(scoring_boxscores_team_query)

        misc_boxscores_query = 'CREATE TABLE IF NOT EXISTS misc_boxscores\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        START_POSITION VARCHAR(255),\
        COMMENT VARCHAR(255),\
        MIN VARCHAR(255),\
        PTS_OFF_TOV INT,\
        PTS_2ND_CHANCE INT,\
        PTS_FB INT,\
        PTS_PAINT INT,\
        OPP_PTS_OFF_TOV INT,\
        OPP_PTS_2ND_CHANCE INT,\
        OPP_PTS_FB INT,\
        OPP_PTS_PAINT INT,\
        BLK INT,\
        BLKA INT,\
        PF INT,\
        PFD INT,\
        PRIMARY KEY(GAME_ID, PLAYER_ID)\
        );'
        cursor.execute(misc_boxscores_query)

        misc_boxscores_team_query = 'CREATE TABLE IF NOT EXISTS misc_boxscores_team\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        MIN VARCHAR(255),\
        PTS_OFF_TOV INT,\
        PTS_2ND_CHANCE INT,\
        PTS_FB INT,\
        PTS_PAINT INT,\
        OPP_PTS_OFF_TOV INT,\
        OPP_PTS_2ND_CHANCE INT,\
        OPP_PTS_FB INT,\
        OPP_PTS_PAINT INT,\
        BLK INT,\
        BLKA INT,\
        PF INT,\
        PFD INT,\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(misc_boxscores_team_query)

        usage_boxscores_query = 'CREATE TABLE IF NOT EXISTS usage_boxscores\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        START_POSITION VARCHAR(255),\
        COMMENT VARCHAR(255),\
        MIN VARCHAR(255),\
        USG_PCT DOUBLE,\
        PCT_FGM DOUBLE,\
        PCT_FGA DOUBLE,\
        PCT_FG3M DOUBLE,\
        PCT_FG3A DOUBLE,\
        PCT_FTM DOUBLE,\
        PCT_FTA DOUBLE,\
        PCT_OREB DOUBLE,\
        PCT_DREB DOUBLE,\
        PCT_REB DOUBLE,\
        PCT_AST DOUBLE,\
        PCT_TOV DOUBLE,\
        PCT_STL DOUBLE,\
        PCT_BLK DOUBLE,\
        PCT_BLKA DOUBLE,\
        PCT_PF DOUBLE,\
        PCT_PFD DOUBLE,\
        PCT_PTS DOUBLE,\
        PRIMARY KEY(GAME_ID, PLAYER_ID)\
        );'
        cursor.execute(usage_boxscores_query)

        four_factors_boxscores_query = 'CREATE TABLE IF NOT EXISTS four_factors_boxscores\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME VARCHAR(255),\
        START_POSITION VARCHAR(255),\
        COMMENT VARCHAR(255),\
        MIN VARCHAR(255),\
        EFG_PCT DOUBLE,\
        FTA_RATE DOUBLE,\
        TM_TOV_PCT DOUBLE,\
        OREB_PCT DOUBLE,\
        OPP_EFG_PCT DOUBLE,\
        OPP_FTA_RATE DOUBLE,\
        OPP_TOV_PCT DOUBLE,\
        OPP_OREB_PCT DOUBLE,\
        PRIMARY KEY(GAME_ID, PLAYER_ID)\
        );'
        cursor.execute(four_factors_boxscores_query)

        four_factors_boxscores_team_query = 'CREATE TABLE IF NOT EXISTS four_factors_boxscores_team\
        (\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        MIN VARCHAR(255),\
        EFG_PCT DOUBLE,\
        FTA_RATE DOUBLE,\
        TM_TOV_PCT DOUBLE,\
        OREB_PCT DOUBLE,\
        OPP_EFG_PCT DOUBLE,\
        OPP_FTA_RATE DOUBLE,\
        OPP_TOV_PCT DOUBLE,\
        OPP_OREB_PCT DOUBLE,\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(four_factors_boxscores_team_query)

        catch_shoot_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_catch_shoot\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PTS DOUBLE,\
        FGM DOUBLE,\
        FGA DOUBLE,\
        FG_PCT DOUBLE,\
        FG3M DOUBLE,\
        FG3A DOUBLE,\
        FG3_PCT DOUBLE,\
        EFG_PCT DOUBLE,\
        PTS_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(catch_shoot_sportvu_query)

        catch_shoot_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_catch_shoot_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PTS DOUBLE,\
        FGM DOUBLE,\
        FGA DOUBLE,\
        FG_PCT DOUBLE,\
        FG3M DOUBLE,\
        FG3A DOUBLE,\
        FG3_PCT DOUBLE,\
        EFG_PCT DOUBLE,\
        PTS_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(catch_shoot_sportvu_team_query)

        defense_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_defense\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        BLK DOUBLE,\
        STL DOUBLE,\
        FGM_DEFEND_RIM DOUBLE,\
        FGA_DEFEND_RIM DOUBLE,\
        FGP_DEFEND_RIM DOUBLE,\
        BLK_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(defense_sportvu_query)

        defense_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_defense_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        BLK DOUBLE,\
        STL DOUBLE,\
        FGM_DEFEND_RIM DOUBLE,\
        FGA_DEFEND_RIM DOUBLE,\
        FGP_DEFEND_RIM DOUBLE,\
        BLK_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(defense_sportvu_team_query)

        drives_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_drives\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        DVS DOUBLE,\
        DPP DOUBLE,\
        DTP DOUBLE,\
        FG_PCT DOUBLE,\
        PTS_48 DOUBLE,\
        DPP_TOT INT,\
        DVS_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(drives_sportvu_query)

        drives_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_drives_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        DVS DOUBLE,\
        DPP DOUBLE,\
        DTP DOUBLE,\
        FG_PCT DOUBLE,\
        PTS_48 DOUBLE,\
        DPP_TOT INT,\
        DVS_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(drives_sportvu_team_query)

        passing_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_passing\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PASS DOUBLE,\
        AST DOUBLE,\
        AST_FT DOUBLE,\
        AST_SEC DOUBLE,\
        AST_POT DOUBLE,\
        PTS_CRT DOUBLE,\
        PTS_CRT_48 DOUBLE,\
        AST_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(passing_sportvu_query)

        passing_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_passing_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PASS DOUBLE,\
        AST DOUBLE,\
        AST_FT DOUBLE,\
        AST_SEC DOUBLE,\
        AST_POT DOUBLE,\
        PTS_CRT DOUBLE,\
        PTS_CRT_48 DOUBLE,\
        AST_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(passing_sportvu_team_query)

        pull_up_shoot_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_pull_up_shoot\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PTS DOUBLE,\
        FGM DOUBLE,\
        FGA DOUBLE,\
        FG_PCT DOUBLE,\
        FG3M DOUBLE,\
        FG3A DOUBLE,\
        FG3_PCT DOUBLE,\
        EFG_PCT DOUBLE,\
        PTS_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(pull_up_shoot_sportvu_query)

        pull_up_shoot_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_pull_up_shoot_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PTS DOUBLE,\
        FGM DOUBLE,\
        FGA DOUBLE,\
        FG_PCT DOUBLE,\
        FG3M DOUBLE,\
        FG3A DOUBLE,\
        FG3_PCT DOUBLE,\
        EFG_PCT DOUBLE,\
        PTS_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(pull_up_shoot_sportvu_team_query)

        rebounding_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_rebounding\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        REB DOUBLE,\
        REB_CHANCE DOUBLE,\
        REB_COL_PCT DOUBLE,\
        REB_CONTESTED DOUBLE,\
        REB_UNCONTESTED DOUBLE,\
        REB_UNCONTESTED_PCT DOUBLE,\
        REB_TOT INT,\
        OREB DOUBLE,\
        OREB_CHANCE DOUBLE,\
        OREB_COL_PCT DOUBLE,\
        OREB_CONTESTED DOUBLE,\
        OREB_UNCONTESTED DOUBLE,\
        OREB_UNCONTESTED_PCT DOUBLE,\
        DREB DOUBLE,\
        DREB_CHANCE DOUBLE,\
        DREB_COL_PCT DOUBLE,\
        DREB_CONTESTED DOUBLE,\
        DREB_UNCONTESTED DOUBLE,\
        DREB_UNCONTESTED_PCT DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(rebounding_sportvu_query)

        rebounding_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_rebounding_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        REB DOUBLE,\
        REB_CHANCE DOUBLE,\
        REB_COL_PCT DOUBLE,\
        REB_CONTESTED DOUBLE,\
        REB_UNCONTESTED DOUBLE,\
        REB_UNCONTESTED_PCT DOUBLE,\
        REB_TOT INT,\
        OREB DOUBLE,\
        OREB_CHANCE DOUBLE,\
        OREB_COL_PCT DOUBLE,\
        OREB_CONTESTED DOUBLE,\
        OREB_UNCONTESTED DOUBLE,\
        OREB_UNCONTESTED_PCT DOUBLE,\
        DREB DOUBLE,\
        DREB_CHANCE DOUBLE,\
        DREB_COL_PCT DOUBLE,\
        DREB_CONTESTED DOUBLE,\
        DREB_UNCONTESTED DOUBLE,\
        DREB_UNCONTESTED_PCT DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(rebounding_sportvu_team_query)

        shooting_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_shooting\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PTS DOUBLE,\
        PTS_DRIVE DOUBLE,\
        FGP_DRIVE DOUBLE,\
        PTS_CLOSE DOUBLE,\
        FGP_CLOSE DOUBLE,\
        PTS_CATCH_SHOOT DOUBLE,\
        FGP_CATCH_SHOOT DOUBLE,\
        PTS_PULL_UP DOUBLE,\
        FGP_PULL_UP DOUBLE,\
        FGA_DRIVE DOUBLE,\
        FGA_CLOSE DOUBLE,\
        FGA_CATCH_SHOOT DOUBLE,\
        FGA_PULL_UP DOUBLE,\
        EFG_PCT DOUBLE,\
        CFGM DOUBLE,\
        CFGA DOUBLE,\
        CFGP DOUBLE,\
        UFGM DOUBLE,\
        UFGA DOUBLE,\
        UFGP DOUBLE,\
        CFG3M DOUBLE,\
        CFG3A DOUBLE,\
        CFG3P DOUBLE,\
        UFG3M DOUBLE,\
        UFG3A DOUBLE,\
        UFG3P DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(shooting_sportvu_query)

        shooting_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_shooting_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        PTS DOUBLE,\
        PTS_DRIVE DOUBLE,\
        FGP_DRIVE DOUBLE,\
        PTS_CLOSE DOUBLE,\
        FGP_CLOSE DOUBLE,\
        PTS_CATCH_SHOOT DOUBLE,\
        FGP_CATCH_SHOOT DOUBLE,\
        PTS_PULL_UP DOUBLE,\
        FGP_PULL_UP DOUBLE,\
        FGA_DRIVE DOUBLE,\
        FGA_CLOSE DOUBLE,\
        FGA_CATCH_SHOOT DOUBLE,\
        FGA_PULL_UP DOUBLE,\
        EFG_PCT DOUBLE,\
        CFGM DOUBLE,\
        CFGA DOUBLE,\
        CFGP DOUBLE,\
        UFGM DOUBLE,\
        UFGA DOUBLE,\
        UFGP DOUBLE,\
        CFG3M DOUBLE,\
        CFG3A DOUBLE,\
        CFG3P DOUBLE,\
        UFG3M DOUBLE,\
        UFG3A DOUBLE,\
        UFG3P DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(shooting_sportvu_team_query)

        speed_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_speed\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        DIST DOUBLE,\
        AV_SPD DOUBLE,\
        DIST_PG DOUBLE,\
        DIST_48 DOUBLE,\
        DIST_OFF DOUBLE,\
        DIST_DEF DOUBLE,\
        AV_SPD_OFF DOUBLE,\
        AV_SPD_DEF DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(speed_sportvu_query)

        speed_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_speed_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        DIST DOUBLE,\
        AV_SPD DOUBLE,\
        DIST_PG DOUBLE,\
        DIST_48 DOUBLE,\
        DIST_OFF DOUBLE,\
        DIST_DEF DOUBLE,\
        AV_SPD_OFF DOUBLE,\
        AV_SPD_DEF DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(speed_sportvu_team_query)

        touches_sportvu_query = 'CREATE TABLE IF NOT EXISTS sportvu_touches\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        TCH DOUBLE,\
        FC_TCH DOUBLE,\
        TOP DOUBLE,\
        CL_TCH DOUBLE,\
        EL_TCH DOUBLE,\
        PTS DOUBLE,\
        PTS_TCH DOUBLE,\
        PTS_HCCT DOUBLE,\
        TCH_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, `DATE`)\
        );'
        cursor.execute(touches_sportvu_query)

        touches_sportvu_team_query = 'CREATE TABLE IF NOT EXISTS sportvu_touches_team\
        (\
        TEAM_ID VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CODE VARCHAR(255),\
        GP INT,\
        MIN DOUBLE,\
        TCH DOUBLE,\
        FC_TCH DOUBLE,\
        TOP DOUBLE,\
        CL_TCH DOUBLE,\
        EL_TCH DOUBLE,\
        PTS DOUBLE,\
        PTS_TCH DOUBLE,\
        PTS_HCCT DOUBLE,\
        TCH_TOT INT,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(touches_sportvu_team_query)

        transition_team_query = 'CREATE TABLE IF NOT EXISTS synergy_transition_team_offense\
        (\
        TEAM_ID VARCHAR(255),\
        TeamName VARCHAR(255),\
        TeamNameAbbreviation VARCHAR(255),\
        TeamShortName VARCHAR(255),\
        GP INT,\
        Poss INT,\
        `Time` DOUBLE,\
        Points INT,\
        FGA INT,\
        FGM INT,\
        PPP DOUBLE,\
        WorsePPP INT,\
        BetterPPP INT,\
        PossG DOUBLE,\
        PPG DOUBLE,\
        FGAG DOUBLE,\
        FGMG DOUBLE,\
        FG_mG DOUBLE,\
        FG_m DOUBLE,\
        FG DOUBLE,\
        aFG DOUBLE,\
        FT DOUBLE,\
        `TO` DOUBLE,\
        SF DOUBLE,\
        PlusOne DOUBLE,\
        Score DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(TEAM_ID, `DATE`)\
        );'
        cursor.execute(transition_team_query)
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_transition_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_isolation_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_isolation_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_ball_handler_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_ball_handler_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_roll_man_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_roll_man_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_post_up_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_post_up_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_spot_up_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_spot_up_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_handoff_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_handoff_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_cut_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_cut_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_off_screen_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_off_screen_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_put_back_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_put_back_team_defense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_misc_team_offense LIKE synergy_transition_team_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_misc_team_defense LIKE synergy_transition_team_offense')

        transition_query = 'CREATE TABLE IF NOT EXISTS synergy_transition_offense\
        (\
        PLAYER_ID VARCHAR(255),\
        PlayerFirstName VARCHAR(255),\
        PlayerLastName VARCHAR(255),\
        PlayerNumber VARCHAR(255),\
        P VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TeamName VARCHAR(255),\
        TeamNameAbbreviation VARCHAR(255),\
        TeamShortName VARCHAR(255),\
        GP INT,\
        Poss INT,\
        `Time` DOUBLE,\
        Points INT,\
        FGA INT,\
        FGM INT,\
        PPP DOUBLE,\
        WorsePPP INT,\
        BetterPPP INT,\
        PossG DOUBLE,\
        PPG DOUBLE,\
        FGAG DOUBLE,\
        FGMG DOUBLE,\
        FG_mG DOUBLE,\
        FG_m DOUBLE,\
        FG DOUBLE,\
        aFG DOUBLE,\
        FT DOUBLE,\
        `TO` DOUBLE,\
        SF DOUBLE,\
        PlusOne DOUBLE,\
        Score DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, TEAM_ID, `DATE`)\
        );'
        cursor.execute(transition_query)
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_isolation_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_isolation_defense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_ball_handler_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_ball_handler_defense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_roll_man_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_pr_roll_man_defense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_post_up_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_post_up_defense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_spot_up_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_spot_up_defense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_handoff_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_handoff_defense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_cut_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_off_screen_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_off_screen_defense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_put_back_offense LIKE synergy_transition_offense')
        cursor.execute('CREATE TABLE IF NOT EXISTS synergy_misc_offense LIKE synergy_transition_offense')

        player_tracking_shot_logs_query = 'CREATE TABLE IF NOT EXISTS player_tracking_shot_logs\
        (\
        PLAYER_ID VARCHAR(255),\
        GAME_ID VARCHAR(255),\
        MATCHUP VARCHAR(255),\
        LOCATION VARCHAR(255),\
        W VARCHAR(255),\
        FINAL_MARGIN INT,\
        SHOT_NUMBER INT,\
        PERIOD INT,\
        GAME_CLOCK VARCHAR(255),\
        SHOT_CLOCK VARCHAR(255),\
        DRIBBLES INT,\
        TOUCH_TIME DOUBLE,\
        SHOT_DIST DOUBLE,\
        PTS_TYPE INT,\
        SHOT_RESULT VARCHAR(255),\
        CLOSEST_DEFENDER VARCHAR(255),\
        CLOSEST_DEFENDER_PLAYER_ID VARCHAR(255),\
        CLOSE_DEF_DIST DOUBLE,\
        FGM BOOLEAN,\
        PTS INT,\
        PRIMARY KEY(PLAYER_ID, GAME_ID, SHOT_NUMBER)\
        );'
        cursor.execute(player_tracking_shot_logs_query)

        player_tracking_rebound_logs_query = 'CREATE TABLE IF NOT EXISTS player_tracking_rebound_logs\
        (\
        PLAYER_ID VARCHAR(255),\
        GAME_ID VARCHAR(255),\
        MATCHUP VARCHAR(255),\
        LOCATION VARCHAR(255),\
        W VARCHAR(255),\
        FINAL_MARGIN INT,\
        REB_NUMBER INT,\
        PERIOD INT,\
        GAME_CLOCK VARCHAR(255),\
        REB_TYPE VARCHAR(255),\
        CONTESTED VARCHAR(255),\
        NUM_CONTESTED INT,\
        REB_DIST DOUBLE,\
        SHOOTER VARCHAR(255),\
        SHOOTER_PLAYER_ID VARCHAR(255),\
        SHOT_DIST DOUBLE,\
        SHOT_TYPE VARCHAR(255),\
        OREB BOOLEAN,\
        DREB BOOLEAN,\
        REB BOOLEAN,\
        PRIMARY KEY(PLAYER_ID, GAME_ID, REB_NUMBER)\
        );'
        cursor.execute(player_tracking_rebound_logs_query)

        player_tracking_passes_made_query = 'CREATE TABLE IF NOT EXISTS player_tracking_passes_made\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME_LAST_FIRST VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        PASS_TYPE VARCHAR(255),\
        G INT,\
        PASS_TO VARCHAR(255),\
        PASS_TEAMMATE_PLAYER_ID VARCHAR(255),\
        FREQUENCY DOUBLE,\
        PASS VARCHAR(255),\
        AST VARCHAR(255),\
        FGM INT,\
        FGA INT,\
        FG_PCT DOUBLE,\
        FG2M INT,\
        FG2A INT,\
        FG2_PCT DOUBLE,\
        FG3M INT,\
        FG3A INT,\
        FG3_PCT DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, PASS_TEAMMATE_PLAYER_ID, TEAM_ID, `DATE`)\
        );'
        cursor.execute(player_tracking_passes_made_query)

        player_tracking_passes_received_query = 'CREATE TABLE IF NOT EXISTS player_tracking_passes_received\
        (\
        PLAYER_ID VARCHAR(255),\
        PLAYER_NAME_LAST_FIRST VARCHAR(255),\
        TEAM_NAME VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        PASS_TYPE VARCHAR(255),\
        G INT,\
        PASS_FROM VARCHAR(255),\
        PASS_TEAMMATE_PLAYER_ID VARCHAR(255),\
        FREQUENCY DOUBLE,\
        PASS VARCHAR(255),\
        AST VARCHAR(255),\
        FGM INT,\
        FGA INT,\
        FG_PCT DOUBLE,\
        FG2M INT,\
        FG2A INT,\
        FG2_PCT DOUBLE,\
        FG3M INT,\
        FG3A INT,\
        FG3_PCT DOUBLE,\
        `DATE` DATE,\
        PRIMARY KEY(PLAYER_ID, PASS_TEAMMATE_PLAYER_ID, TEAM_ID, `DATE`)\
        );'
        cursor.execute(player_tracking_passes_received_query)

        game_info_query = 'CREATE TABLE IF NOT EXISTS game_info\
        (\
        GAME_DATE VARCHAR(255),\
        ATTENDANCE INT,\
        GAME_TIME VARCHAR(255),\
        GAME_ID VARCHAR(255),\
        PRIMARY KEY(GAME_ID)\
        );'
        cursor.execute(game_info_query)

        game_summary_query = 'CREATE TABLE IF NOT EXISTS game_summary\
        (\
        GAME_DATE_EST VARCHAR(255),\
        GAME_SEQUENCE INT,\
        GAME_ID VARCHAR(255),\
        GAME_STATUS_ID VARCHAR(255),\
        GAME_STATUS_TEXT VARCHAR(255),\
        GAMECODE VARCHAR(255),\
        HOME_TEAM_ID VARCHAR(255),\
        VISITOR_TEAM_ID VARCHAR(255),\
        SEASON VARCHAR(255),\
        LIVE_PERIOD INT,\
        LIVE_PC_TIME VARCHAR(255),\
        NATL_TV_BROADCASTER_ABBREVIATION VARCHAR(255),\
        LIVE_PERIOD_TIME_BCAST VARCHAR(255),\
        WH_STATUS VARCHAR(255),\
        PRIMARY KEY(GAME_ID)\
        );'
        cursor.execute(game_summary_query)

        officials_query = 'CREATE TABLE IF NOT EXISTS officials\
        (\
        OFFICIAL_ID VARCHAR(255),\
        FIRST_NAME VARCHAR(255),\
        LAST_NAME VARCHAR(255),\
        JERSEY_NUM INT,\
        GAME_ID VARCHAR(255),\
        PRIMARY KEY(GAME_ID, OFFICIAL_ID)\
        );'
        cursor.execute(officials_query)

        other_stats_query = 'CREATE TABLE IF NOT EXISTS other_stats\
        (\
        LEAGUE_ID VARCHAR(255),\
        SEASON_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY VARCHAR(255),\
        PTS_PAINT INT,\
        PTS_2ND_CHANCE INT,\
        PTS_FB INT,\
        LARGEST_LEAD INT,\
        LEAD_CHANGES INT,\
        TIMES_TIED INT,\
        GAME_ID VARCHAR(255),\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(other_stats_query)

        line_score_query = 'CREATE TABLE IF NOT EXISTS line_score\
        (\
        GAME_DATE_EST VARCHAR(255),\
        GAME_SEQUENCE INT,\
        GAME_ID VARCHAR(255),\
        TEAM_ID VARCHAR(255),\
        TEAM_ABBREVIATION VARCHAR(255),\
        TEAM_CITY_NAME VARCHAR(255),\
        TEAM_NICKNAME VARCHAR(255),\
        TEAM_WINS_LOSSES VARCHAR(255),\
        PTS_QTR1 INT,\
        PTS_QTR2 INT,\
        PTS_QTR3 INT,\
        PTS_QTR4 INT,\
        PTS_OT1 INT,\
        PTS_OT2 INT,\
        PTS_OT3 INT,\
        PTS_OT4 INT,\
        PTS_OT5 INT,\
        PTS_OT6 INT,\
        PTS_OT7 INT,\
        PTS_OT8 INT,\
        PTS_OT9 INT,\
        PTS_OT10 INT,\
        PTS INT,\
        PRIMARY KEY(GAME_ID, TEAM_ID)\
        );'
        cursor.execute(line_score_query)

        conn.commit()
        conn.close()
