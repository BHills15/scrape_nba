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

        conn.close()
