import tweepy
import os
import random

# Twitter API credentials
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Set up Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to generate Mocking SpongeBob-style text
def generate_mocking_text(original_text):
    return ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in original_text)

# Function to respond to mentions
def respond_to_mentions():
    mentions = api.mentions_timeline(count=10)
    for mention in mentions:
        original_text = mention.text
        mocking_text = generate_mocking_text(original_text)
        response_text = f"Mocking SpongeBob says: {mocking_text}"
        api.update_status(status=response_text, in_reply_to_status_id=mention.id)

# Run the bot
if __name__ == "__main__":
    respond_to_mentions()
