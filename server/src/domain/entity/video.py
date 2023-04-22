import validators

class Video:
    def __init__(self, id: str, title: str, description: str, url: str, duration: int, thumbnail_url: str, published_at: str, channel_id):
        self.validate(id, title, description, url, duration, thumbnail_url, published_at, channel_id)

        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.duration = duration
        self.thumbnail_url = thumbnail_url
        self.published_at = published_at
        self.channel_id = channel_id
    
    def get_value(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "duration": self.duration,
            "thumbnail_url": self.thumbnail_url,
            "published_at": self.published_at,
            "channel_id": self.channel_id
        }
    
    def validate(self, id, title, description, url, duration, thumbnail_url, published_at, channel_id) -> bool:
        if title is None:
            raise ValueError("title is required")
        
        if description is None:
            raise ValueError("description is required")
        
        if url is None:
            raise ValueError("url is required")
        
        if not validators.url(url):
            raise ValueError("url is invalid")

        if duration is None:
            raise ValueError("duration is required")
        
        if duration < 0:
            raise ValueError("duration should be greater than zero")
        
        if thumbnail_url is None:
            raise ValueError("thumbnail_url is required")
        
        if not validators.url(thumbnail_url):
            raise ValueError("thumbnail_url is invalid")
        
        if published_at is None:
            raise ValueError("published_at is required")

        return True 