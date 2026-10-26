from api_client import *
import pytest

def test_get_all_posts():
    response = get_posts()
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    
    post = posts[0]
    assert "id" in post
    assert "userId" in post
    assert "body" in post
    assert "title" in post

def test_get_post_id():
    response = get_post(1)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert post["userId"] == 1
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)
    assert post["title"] != ""
    assert post["body"] != ""

@pytest.mark.parametrize("post_id", [1, 3, 10, 77, 98])
def test_get_post_exist(post_id): 
    response = get_post(post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_create_post():
    title = 'Мой тестовый пост'
    body = 'Создан он мной'
    user_id = 1
    response = create_post(title, body, user_id)
    assert response.status_code == 201
    
    created_post = response.json()
    assert created_post["title"] == title
    assert created_post["body"] == body
    assert created_post["userId"] == user_id
    assert "id" in created_post


def test_get_comments():
    response = get_comments(1)
    assert response.status_code == 200

    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) > 0

    for com in comments:
        assert con["postId"] == 1
        assert "email" in con
        assert "name" in con
        assert "body" in con

def test_get_notpost():
    response = get_post(999)
    assert response.status_code == 404
    assert response.json() == {}
