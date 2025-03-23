from django.db import migrations


def create_mock_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Post = apps.get_model("comments", "Post")
    Comment = apps.get_model("comments", "Comment")
    Like = apps.get_model("comments", "Like")

    user1 = User.objects.create_user(username="user1", password="password")
    user2 = User.objects.create_user(username="user2", password="password")

    post1 = Post.objects.create(title="Первый пост", content="Содержимое поста 1", author=user1)
    post2 = Post.objects.create(title="Второй пост", content="Содержимое поста 2", author=user2)

    comment1 = Comment.objects.create(post=post1, author=user2, content="Комментарий к посту 1")
    comment2 = Comment.objects.create(post=post2, author=user1, content="Комментарий к посту 2")

    Like.objects.create(user=user1, post=post1)
    Like.objects.create(user=user2, post=post2)
    Like.objects.create(user=user1, comment=comment2)


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_mock_data),
    ]
