import MySQLdb

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

        conn.close()
