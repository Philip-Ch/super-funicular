# Generated by Django 3.1.5 on 2021-02-22 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('likes', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='posts/%Y/%m/%d/%t')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.IntegerField(default=0, verbose_name='profile_followers')),
                ('following', models.IntegerField(default=0, verbose_name='profile_following')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('following_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_id', to='profiles.profile')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_id', to='profiles.profile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=500)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author_id', to='profiles.profile')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.profile'),
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.postcomment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.AddConstraint(
            model_name='userfollowing',
            constraint=models.UniqueConstraint(fields=('profile_id', 'following_profile_id'), name='unique_followers'),
        ),
        migrations.AddConstraint(
            model_name='userfollowing',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, profile_id=django.db.models.expressions.F('following_profile_id')), name='followed_and_follower_different_constraint'),
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('profile_id', 'following_profile_id')},
        ),
    ]
