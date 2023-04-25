from src.infrastructure.db.clients.sqlite_client import SqliteClient
import os


class VideoRepository:
    def __init__(self):
        db_file = os.path.abspath(
            "./src/infrastructure/db/database/flowcast.db")
        self.client = SqliteClient(db_file)

        pass

    def get_by_id(self, id: str) -> any:
        self.client.connect()
        result = self.client.execute_query_single(
            "SELECT * FROM videos WHERE id = ?", (id,))

        self.client.disconnect()
        return result

    def get_all(self):
        self.client.connect()

        result = self.client.execute_query(
            "SELECT * FROM videos")

        self.client.disconnect()
        return result

    def create(self, video: any):
        self.client.connect()

        result = self.client.execute_insert(
            "INSERT INTO videos (title, description, url, duration, thumbnail_url, published_at, channel_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (video.title, video.description, video.url, video.duration, video.thumbnail_url, video.published_at, video.channel_id))
        print(result)
        self.client.disconnect()
        return result

    def update(self, video: any, id: str):
        self.client.connect()

        result = self.client.execute_insert(
            "UPDATE videos SET title = ?, description = ?, url = ?, duration = ?, thumbnail_url = ?, published_at = ?, channel_id = ? WHERE id = ?", (video.title, video.description, video.url, video.duration, video.thumbnail_url, video.published_at, video.channel_id, id))

        self.client.disconnect()
        return result
    
    def delete(self, id: str):
        self.client.connect()

        result = self.client.execute_insert(
            "DELETE FROM videos WHERE id = ?", (id,))

        self.client.disconnect()
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

        self.client.connect()
        self.client.execute_query_single(sql_commands[0])
        self.client.disconnect()
