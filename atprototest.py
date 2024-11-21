from atproto import Client
import getpass

# Create a client instance
client = Client()

# Log in with the provided credentials
try:
    client.login('jaredleve.bsky.social', '')
    print("Login successful!")

    # Send a post
    post = client.send_post("test")
    print("Post sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
