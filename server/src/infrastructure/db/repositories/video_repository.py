from ..clients.sqlite_client import SqliteClient

class VideoRepository:
    def __init__(self):
        pass

    def get_by_id(self, id: str) -> any:
        client = SqliteClient("../database/flowcast.db")
        client.connect()
        result = client.execute_query_single("SELECT * FROM videos WHERE id = ?", (id,))
        print(result)
        client.disconnect()
        pass


video_repository = VideoRepository()
video_repository.get_by_id("1")