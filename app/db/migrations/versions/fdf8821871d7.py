"""main tables

Revision ID: fdf8821871d7
Revises:
Create Date: 2019-09-22 01:36:44.791880

"""

from app.db.migrations.alembic_interface import *

revision = "fdf8821871d7"
down_revision = None
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    create_updated_at_trigger_helper()


def timestamps() -> Tuple[sa.Column, sa.Column]:
    return timestamps_helper()


def create_users_table() -> None:
    create_users_table_helper()


def create_followers_to_followings_table() -> None:
    create_followers_to_followings_table_helper()


def create_articles_table() -> None:
    create_articles_table()


def create_tags_table() -> None:
    create_tags_table_helper()


def create_articles_to_tags_table() -> None:
    create_articles_to_tags_table_helper()


def create_favorites_table() -> None:
    create_favorites_table_helper()


def create_commentaries_table() -> None:
    create_commentaries_table_helper()


def add_tags(tags, article_id):
    add_tags_helper(tags, article_id)


def create_new_user(username, email, password, admin=False, image="") -> None:
    create_new_user_helper(username, email, password, admin, image)


def create_new_article(slug, title, description, body, author_id, tags=[]) -> None:
    create_new_article_helper(slug, title, description, body, author_id, tags)


def create_new_comment(body, author_id, article_id) -> None:
    create_new_comment_helper(body, author_id, article_id)


def upgrade() -> None:
    upgrade_helper()


def downgrade() -> None:
    downgrade_helper()
