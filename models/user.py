class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # In production, hash this

    @staticmethod
    def authenticate(username, password):
        # Demo auth, replace with DB query
        return True  # Simplified for demo

