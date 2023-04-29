from src.infrastructure.db.clients.sqlite_client import SqliteClient
import os


class MoodRepository:
    def __init__(self):
        db_file = os.path.abspath(
            "./src/infrastructure/db/database/moody.db")
        self.client = SqliteClient(db_file)

        pass

    def get_by_id(self, id: str) -> any:
        self.client.connect()
        result = self.client.execute_query_single(
            "SELECT * FROM moods WHERE id = ?", (id,))

        self.client.disconnect()
        return result

    def get_all(self):
        self.client.connect()

        result = self.client.execute_query(
            "SELECT * FROM moods")

        self.client.disconnect()
        return result

    def create(self, mood: any):
        self.client.connect()

        result = self.client.execute_insert(
            "INSERT INTO moods (title, description, url, duration, thumbnail_url, published_at, channel_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (mood.title, mood.description, mood.url, mood.duration, mood.thumbnail_url, mood.published_at, mood.channel_id))
        print(result)
        self.client.disconnect()
        return result

    def update(self, mood: any, id: str):
        self.client.connect()

        result = self.client.execute_insert(
            "UPDATE moods SET title = ?, description = ?, url = ?, duration = ?, thumbnail_url = ?, published_at = ?, channel_id = ? WHERE id = ?", (mood.title, mood.description, mood.url, mood.duration, mood.thumbnail_url, mood.published_at, mood.channel_id, id))

        self.client.disconnect()
        return result
    
    def delete(self, id: str):
        self.client.connect()

        result = self.client.execute_insert(
            "DELETE FROM moods WHERE id = ?", (id,))

        self.client.disconnect()
        return result


    def migration(self):
        # Define the SQL commands to create the moods table and insert a row of data
        sql_commands = [
            '''
            CREATE TABLE IF NOT EXISTS moods (
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

        self.client.connect()
        self.client.execute_query_single(sql_commands[0])
        self.client.disconnect()
