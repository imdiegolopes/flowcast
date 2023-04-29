class Mood:
    def __init__(self, id: str, date: str, feeling: str, intensity: int, comments: str, activity: str):
        self.validate(id, date, feeling, intensity, comments, activity)

        self.id = id
        self.date = date
        self.feeling = feeling
        self.intensity = intensity
        self.comments = comments
        self.activity = activity
        pass

    def get_value(self) -> dict:
        pass

    def validate(self, id, date, feeling, intensity, comments, activity) -> bool:
        if date is None:
            raise ValueError("date is required")
        
        if feeling is None:
            raise ValueError("feeling is required")
        
        if intensity is None:
            raise ValueError("intensity is required")
        
        if intensity < 0:
            raise ValueError("intensity should be greater than zero")
        
        if intensity > 19:
            raise ValueError("intensity should be equal or less than 10")
        
        if comments is None:
            raise ValueError("comments is required")
        
        if activity is None:
            raise ValueError("activity is required")

        return True

