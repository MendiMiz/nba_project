import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI


def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)


def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    
    CREATE TABLE IF NOT EXISTS players (
        id VARCHAR(50) PRIMARY KEY,
        player_name VARCHAR(255) NOT NULL  
    );

    CREATE TABLE IF NOT EXISTS players_in_season (
        id INT NOT NULL,
        player_name VARCHAR(255) NOT NULL,
        position VARCHAR(50) NOT NULL,
        games INT NOT NULL,
        field_goals INT NOT NULL,
        field_attempts INT NOT NULL,
        field_percent INT NOT NULL,
        three_fg INT NOT NULL,
        three_attempts INT NOT NULL,
        three_percent FLOAT NOT NULL,
        two_fg INT NOT NULL,
        two_attempts INT NOT NULL,
        two_percent FLOAT NOT NULL,
        effect_fg_percent FLOAT NOT NULL,
        ft INT NOT NULL,
        ft_attempts INT NOT NULL,
        assists INT NOT NULL,
        steals INT NOT NULL,
        blocks INT NOT NULL,
        turnovers INT NOT NULL,
        personal_fouls INT NOT NULL,
        points INT NOT NULL,
        team VARCHAR(255) NOT NULL,
        season INT NOT NULL,
        player_id VARCHAR(50) NOT NULL,
        FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
    );

    
    CREATE TABLE IF NOT EXISTS fantasy_team (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        C VARCHAR(50) NOT NULL,
        PF VARCHAR(50) NOT NULL,
        SF VARCHAR(50) NOT NULL,
        SG VARCHAR(50) NOT NULL,
        PG VARCHAR(50) NOT NULL,
        FOREIGN KEY (C) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (PF) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (SF) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (SG) REFERENCES players(id) ON DELETE CASCADE,
        FOREIGN KEY (PG) REFERENCES players(id) ON DELETE CASCADE
    );

    ''')

    connection.commit()
    cursor.close()
    connection.close()
