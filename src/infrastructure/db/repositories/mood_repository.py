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
            "INSERT INTO moods (id, date, feeling, intensity, comments, activity, created_on, updated_on) VALUES(?,?,?,?,?,?,?,?)", (str(mood.id), mood.date, mood.feeling, mood.intensity, mood.comments, mood.activity, mood.created_on, mood.updated_on))
        print(result)
        self.client.disconnect()
        return result

    def update(self, mood: any, id: str):
        self.client.connect()

        result = self.client.execute_insert(
            "UPDATE moods SET date = ?, feeling = ?, intensity = ?, comments = ?, activity = ?, updated_on = ? WHERE id = ?", (mood.date, mood.feeling, mood.intensity, mood.comments, mood.activity, mood.updated_on,  id))
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
                id TEXT PRIMARY KEY,
                date TEXT NOT NULL,
                feeling TEXT NOT NULL,
                intensity INTEGER NOT NULL,
                comments TEXT NOT NULL,
                activity TEXT NOT NULL,
                created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            ''',
        ]

        self.client.connect()
        self.client.execute_query_single(sql_commands[0])
        self.client.disconnect()
