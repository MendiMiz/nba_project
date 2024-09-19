import pytest
from repository.seed_database import create_tables, get_db_connection


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    write_users_to_db()
    yield
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS user_answers;
        DROP TABLE IF EXISTS answer;
        DROP TABLE IF EXISTS question;
        DROP TABLE IF EXISTS trivia_user;
    """)
    connection.commit()
    cursor.close()
    connection.close()