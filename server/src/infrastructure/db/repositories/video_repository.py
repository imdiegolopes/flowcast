from src.infrastructure.db.clients.sqlite_client import SqliteClient
import os


class VideoRepository:
    def __init__(self):
        pass

    def get_by_id(self, id: str) -> any:
        db_file = os.path.abspath(
            "./src/infrastructure/db/database/flowcast.db")
        print(db_file)
        client = SqliteClient(db_file)
        client.connect()
        result = client.execute_query_single(
            "SELECT * FROM videos WHERE id = ?", (id,))

        client.disconnect()
        return result

    def get_all(self):
        db_file = os.path.abspath(
            "./src/infrastructure/db/database/flowcast.db")
        client = SqliteClient(db_file)
        client.connect()

        result = client.execute_query_single(
            "SELECT * FROM videos")

        client.disconnect()
        return result

    def migration(self):
        # Define the SQL commands to create the videos table and insert a row of data
        sql_commands = [
            '''
            CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                url TEXT,
                duration INTEGER,
                thumbnail_url TEXT,
                published_at TEXT,
                channel_id TEXT DEFAULT NULL
            );
            ''',
        ]

        # Connect to the database and execute the SQL commands
        client = SqliteClient("../flowcast.db")
        client.connect()
        client.execute_query_single(sql_commands[0])
        client.disconnect()
