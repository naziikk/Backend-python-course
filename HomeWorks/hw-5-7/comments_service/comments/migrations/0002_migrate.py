from django.db import migrations


def create_mock_data(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Post = apps.get_model("comments", "Post")
    Comment = apps.get_model("comments", "Comment")
    Like = apps.get_model("comments", "Like")

    users = [
        User.objects.create_user(username=f"user{i}", password="password") for i in range(1, 11)
    ]

    posts = [
        Post.objects.create(title=f"Пост {i}", content=f"Содержимое поста {i}", author=users[i % 10])
        for i in range(1, 11)
    ]

    comments = [
        Comment.objects.create(post=posts[i % 10], author=users[(i + 1) % 10], content=f"Комментарий к посту {i}")
        for i in range(1, 11)
    ]

    likes = [
        Like.objects.create(user=users[i % 10], post=posts[i % 10])
        for i in range(1, 11)
    ]
    likes += [
        Like.objects.create(user=users[i % 10], comment=comments[i % 10])
        for i in range(1, 11)
    ]


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_mock_data),
    ]
