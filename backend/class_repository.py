import random

class Repository:
    """Repository class for managing quotes and jokes."""
    
    def __init__(self):
        # Initialize with some default quotes and jokes
        self.quotes = [
            "Life is what happens when you're busy making other plans.",
            "The way to get started is to quit talking and begin doing.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "If life were predictable it would cease to be life, and be without flavor.",
            "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."
        ]
        
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
    
    def get_random_quote(self) -> str:
        """Return a random quote from the repository."""
        return {"type": "quote", "content": random.choice(self.quotes)}
    
    def get_random_joke(self) -> str:
        """Return a random joke from the repository."""
        return {"type": "joke", "content": random.choice(self.jokes)}
    
    def get_random_content(self) -> dict[str, str]:
        """Return either a random quote or joke with its type."""
        content_type = random.choice(["quote", "joke"])
        
        if content_type == "quote":
            return self.get_random_quote()
        else:
            return self.get_random_joke()

if __name__ == "__main__":

    repository = Repository()
    print(repository.get_random_joke())