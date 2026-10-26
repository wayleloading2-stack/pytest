import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts():
    return requests.get(f"{BASE_URL}/posts", timeout=10)


def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)


def get_posts_by_user(user_id):
    return requests.get(
        f"{BASE_URL}/posts", params={"userId": user_id}, timeout=10
    )


def create_post(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id,
    }
    return requests.post(f"{BASE_URL}/posts", json=data, timeout=10)


def update_post(post_id, title, body, user_id):
    data = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id,
    }
    return requests.put(f"{BASE_URL}/posts/{post_id}", json=data, timeout=10)


def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}", timeout=10)


def get_comments(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}/comments", timeout=10)
