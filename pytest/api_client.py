import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    return requests.get(f"{BASE_URL}/posts")

def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")

def get_posts_by_user(user_id):
    return requests.get(f"{BASE_URL}/posts", params={"userId": user_id})

def create_post(title, body, user_id):
    data = {
        "title" : title,
        "body" : body,
        "user_id" : user_id
    }
    return requests.post(f"{BASE_URL}/posts", json=data)

def get_comments(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}/comments")