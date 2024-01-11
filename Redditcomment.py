import json
import praw

def serialize(entry):
    return {k: v for k, v in entry.__dict__.items() if isinstance(v, (bool, str, int, float, type(None)))}

def save_records(filename, records):
    with open(filename, "w") as f:
        json.dump(records, f, indent=4)

def main():
    USER = "ZeDominion"  # Replace with the Reddit username

    # Set up praw with your credentials
    reddit = praw.Reddit(
        client_id='6il3CGWBkKDyPNzIvn1Tlw',        # Replace with your client ID
        client_secret='f7dJJOqY3N9fryAiEukqsoBknEq39w',# Replace with your client secret
        user_agent='python:myredditapp:v1.0 (by /u/ZeDominion)',      # Replace with your user agent
        username=USER,                   # Your Reddit username
        password='Louati1404!'          # Your Reddit password
    )

    user = reddit.redditor(USER)

    # Getting the latest comments
    comments = user.comments.new(limit=100)  # Retrieves the last 10 comments
    comments_data = [serialize(comment) for comment in comments]
    save_records("comments.json", comments_data)

    # Getting the latest submissions
    submissions = user.submissions.new(limit=10)  # Retrieves the last 10 submissions
    submissions_data = [serialize(submission) for submission in submissions]
    save_records("submissions.json", submissions_data)

    print("Backup completed.")

if __name__ == "__main__":
    main()
