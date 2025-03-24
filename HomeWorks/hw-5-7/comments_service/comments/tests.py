from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Post, Comment, Like


@pytest.mark.django_db
def test_register_user():
    client = APIClient()
    data = {'username': 'Назар Закревский', 'password': 'Назар2005'}
    response = client.post('/register/', data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_login_user():
    client = APIClient()
    user = User.objects.create_user(username='Назар Закревский', password='Назар2005')
    data = {'username': 'Назар Закревский', 'password': 'Назар2005'}
    response = client.post('/login/', data)
    assert response.status_code == 200
    assert 'access' in response.data


@pytest.mark.django_db
def test_create_post():
    client = APIClient()
    user = User.objects.create_user(username='Назар Закревский', password='Назар2005')
    client.force_authenticate(user=user)
    data = {
        'title': 'Постик',
        'content': 'Тестовый постик.',
    }
    response = client.post('/api/posts/', data)
    assert response.status_code == 201
    assert response.data['title'] == 'Test Post'
    assert response.data['author'] == user.id


@pytest.mark.django_db
def test_create_comment():
    client = APIClient()
    user = User.objects.create_user(username='Назар Закревский', password='Назар2005')
    post = Post.objects.create(title='пост-5', content='данные-5', author=user)
    client.force_authenticate(user=user)
    data = {
        'content': 'Комментик тестовый.',
    }
    response = client.post(f'/api/posts/{post.id}/comments/', data)
    assert response.status_code == 201
    assert response.data['content'] == 'This is a test comment.'
    assert response.data['author'] == user.id
    assert response.data['post'] == post.id


@pytest.mark.django_db
def test_like_post():
    client = APIClient()
    user = User.objects.create_user(username='Назар Закревский', password='Назар2005')
    post = Post.objects.create(title='пост-4', content='контентик', author=user)
    client.force_authenticate(user=user)
    response = client.post(f'/api/posts/{post.id}/like/')
    assert response.status_code == 201
    assert response.data['user'] == user.id
    assert response.data['post'] == post.id


@pytest.mark.django_db
def test_like_comment():
    client = APIClient()
    user = User.objects.create_user(username='Назар Закревский', password='Назар2005')
    post = Post.objects.create(title='пост-3', content='данные-3', author=user)
    comment = Comment.objects.create(post=post, author=user, content="коммент-1")
    client.force_authenticate(user=user)
    response = client.post(f'/api/comments/{comment.id}/like/')
    assert response.status_code == 201
    assert response.data['user'] == user.id
    assert response.data['comment'] == comment.id


@pytest.mark.django_db
def test_get_posts():
    client = APIClient()
    user = User.objects.create_user(username='Назар Закревский', password='Назар2005')
    Post.objects.create(title='пост-1', content='данные-1', author=user)
    response = client.get('/api/posts/')
    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_get_comments():
    client = APIClient()
    user = User.objects.create_user(username='Назар Закревский', password='Назар2005')
    post = Post.objects.create(title='пост-2', content='данные-2', author=user)
    Comment.objects.create(post=post, author=user, content="бла бла")
    response = client.get(f'/api/posts/{post.id}/comments/')
    assert response.status_code == 200
    assert len(response.data) > 0
