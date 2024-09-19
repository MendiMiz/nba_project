import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI


def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)


def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''

    CREATE TABLE IF NOT EXISTS players_in_season (
        id INT NOT NULL,
        playerName VARCHAR(255) NOT NULL,
        position VARCHAR(50) NOT NULL,
        games INT NOT NULL,
        fieldGoals INT NOT NULL,
        fieldAttempts INT NOT NULL,
        fieldPercent INT NOT NULL,
        threeFg INT NOT NULL,
        threeAttempts INT NOT NULL,
        threePercent FLOAT NOT NULL,
        twoFg INT NOT NULL,
        twoAttempts INT NOT NULL,
        twoPercent FLOAT NOT NULL,
        effectFgPercent FLOAT NOT NULL,
        ft INT NOT NULL,
        ftAttempts INT NOT NULL,
        ftPercent FLOAT NOT NULL,
        assists INT NOT NULL,
        steals INT NOT NULL,
        blocks INT NOT NULL,
        turnovers INT NOT NULL,
        personalFouls INT NOT NULL,
        points INT NOT NULL,
        team INT NOT NULL,
        season INT NOT NULL,
        playerId VARCHAR(50) NOT NULL,
        FOREIGN KEY (playerId) REFERENCES players(id)
    );

    CREATE TABLE IF NOT EXISTS players (
        id VARCHAR(50) PRIMARY KEY,
        playerName VARCHAR(255) NOT NULL  
    );
    
    CREATE TABLE IF NOT EXISTS fantasy_team (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        C VARCHAR(50) NOT NULL,
        PF VARCHAR(50) NOT NULL,
        SF VARCHAR(50) NOT NULL,
        SG VARCHAR(50) NOT NULL,
        PG VARCHAR(50) NOT NULL,
        FOREIGN KEY (C) REFERENCES players(id),
        FOREIGN KEY (PF) REFERENCES players(id),
        FOREIGN KEY (SF) REFERENCES players(id),
        FOREIGN KEY (SG) REFERENCES players(id),
        FOREIGN KEY (PG) REFERENCES players(id)
    );

    ''')

    connection.commit()
    cursor.close()
    connection.close()
