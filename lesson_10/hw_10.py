from abc import ABC, abstractmethod
from time import time


class SocialChannel(ABC):
    def __init__(self, type_: str, subs: int):
        self.type = type_
        self.subs = subs

    @abstractmethod
    def post_message(self, message: str, timestamp: int):
        pass

    def process_schedule(self, posts):
        current_time = int(time())
        for post in posts:
            message, post_timestamp = post
            if post_timestamp <= current_time:
                self.post_message(message, post_timestamp)


class YouTube(SocialChannel):
    def __init__(self, subs):
        super().__init__("YouTube", subs)

    def post_message(self, message: str, timestamp: int):
        # Implementation for posting to YouTube
        print(f"Posting to YouTube: {message}")


class Twitter(SocialChannel):
    def __init__(self, subs):
        super().__init__("Twitter", subs)

    def post_message(self, message: str, timestamp: int):
        # Implementation for posting to Twitter
        print(f"Posting to Twitter: {message}")


class Facebook(SocialChannel):
    def __init__(self, subs):
        super().__init__("Facebook", subs)

    def post_message(self, message: str, timestamp: int):
        # Implementation for posting to Facebook
        print(f"Posting to Facebook: {message}")


# # Define a function to process social channels
def process_social_channel(channel: SocialChannel, posts: list):
    channel.process_schedule(posts)
    print(int(time()))
    print(time())


# Create instances of social channels
youtube_channel = YouTube(1909876)
twitter_channel = Twitter(17654)
facebook_channel = Facebook(2345678)

# Define posts as tuples
post1 = ("New video on YouTube!", int(time()))
post2 = ("Check out our Twitter page!", int(time()))
post3 = ("Like us on Facebook!", int(time()))
post4 = ("New video on our channel!", 1697321005)
post5 = ("Exciting news coming soon!", 1997321005)

# Create a list of posts
posts = [post1, post2, post3, post4, post5]

# Process the social channels and post messages
process_social_channel(youtube_channel, posts)
process_social_channel(twitter_channel, posts)
process_social_channel(facebook_channel, posts)
