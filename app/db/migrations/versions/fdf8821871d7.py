"""main tables

Revision ID: fdf8821871d7
Revises:
Create Date: 2019-09-22 01:36:44.791880

"""
from typing import Tuple

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func
from app.services import security

revision = "fdf8821871d7"
down_revision = None
branch_labels = None
depends_on = None

def create_updated_at_trigger() -> None:
    op.execute(
        """
    CREATE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS
    $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """
    )


def timestamps() -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
            onupdate=func.current_timestamp(),
        ),
    )


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("email", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("salt", sa.Text, nullable=False),
        sa.Column("hashed_password", sa.Text),
        sa.Column("bio", sa.Text, nullable=False, server_default=""),
        sa.Column("image", sa.Text),
        sa.Column("admin", sa.Boolean, nullable=False, default=False),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_user_modtime
            BEFORE UPDATE
            ON users
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_followers_to_followings_table() -> None:
    op.create_table(
        "followers_to_followings",
        sa.Column(
            "follower_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "following_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
    )
    op.create_primary_key(
        "pk_followers_to_followings",
        "followers_to_followings",
        ["follower_id", "following_id"],
    )


def create_articles_table() -> None:
    op.create_table(
        "articles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("slug", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("title", sa.Text, nullable=False),
        sa.Column("description", sa.Text, nullable=False),
        sa.Column("body", sa.Text, nullable=False),
        sa.Column(
            "author_id", sa.Integer, sa.ForeignKey("users.id", ondelete="SET NULL")
        ),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_article_modtime
            BEFORE UPDATE
            ON articles
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_tags_table() -> None:
    op.create_table("tags", sa.Column("tag", sa.Text, primary_key=True))


def create_articles_to_tags_table() -> None:
    op.create_table(
        "articles_to_tags",
        sa.Column(
            "article_id",
            sa.Integer,
            sa.ForeignKey("articles.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "tag",
            sa.Text,
            sa.ForeignKey("tags.tag", ondelete="CASCADE"),
            nullable=False,
        ),
    )
    op.create_primary_key(
        "pk_articles_to_tags", "articles_to_tags", ["article_id", "tag"]
    )


def create_favorites_table() -> None:
    op.create_table(
        "favorites",
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "article_id",
            sa.Integer,
            sa.ForeignKey("articles.id", ondelete="CASCADE"),
            nullable=False,
        ),
    )
    op.create_primary_key("pk_favorites", "favorites", ["user_id", "article_id"])


def create_commentaries_table() -> None:
    op.create_table(
        "commentaries",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("body", sa.Text, nullable=False),
        sa.Column(
            "author_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "article_id",
            sa.Integer,
            sa.ForeignKey("articles.id", ondelete="CASCADE"),
            nullable=False,
        ),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_comment_modtime
            BEFORE UPDATE
            ON commentaries
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def add_tags(tags, article_id):
    connection = op.get_bind()
    for tag in tags:
        exists = False
        res = connection.execute(
            f"""
            SELECT * from tags 
            WHERE tag = '{tag}'

        """)
        for row in res:
            if row['tag']:
                exists = True
        if not exists:
            op.execute(
                f"""    
                INSERT INTO tags(tag)
                VALUES('{tag}')
            """)
        op.execute(
            f"""    
            INSERT INTO articles_to_tags(article_id, tag)
            VALUES('{article_id}', '{tag}')
        """)


def create_new_user(username, email, password, admin=False, image="") -> None:
    salt = security.generate_salt()
    hashed_password = security.get_password_hash(salt + password)

    op.execute(
        f"""    
        INSERT INTO users(username, email, salt, hashed_password, admin, image)
        VALUES('{username}','{email}', '{salt}', '{hashed_password}','{admin}', '{image}')
    """)


def create_new_article(slug, title, description, body, author_id, tags=[]) -> None:
    connection = op.get_bind()
    res = connection.execute(
        f"""
        INSERT INTO articles (slug, title, description, body, author_id)
        VALUES ('{slug}', '{title}', '{description}', '{body}', '{author_id}')
        RETURNING id
    """)
    for row in res:
        if tags:
            add_tags(tags, row['id'])


def create_new_comment(body, author_id, article_id) -> None:
    op.execute(
        f"""       
        INSERT INTO commentaries (body, author_id, article_id)
        VALUES ('{body}', '{author_id}', '{article_id}')
    """)


def upgrade() -> None:
    create_updated_at_trigger()
    create_users_table()
    create_followers_to_followings_table()
    create_articles_table()
    create_tags_table()
    create_articles_to_tags_table()
    create_favorites_table()
    create_commentaries_table()
    create_new_user(username="Pikachu", email="Pikachu@checkmarx.com", password="snorlax", image="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/30e23551-c869-487d-a6d4-4aa73c102731/d553a9m-94352d40-78c7-433f-b867-801e0a04f563.jpg/v1/fill/w_900,h_900,q_75,strp/pikachu_wallpaper_by_moustachegirl05_d553a9m-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTAwIiwicGF0aCI6IlwvZlwvMzBlMjM1NTEtYzg2OS00ODdkLWE2ZDQtNGFhNzNjMTAyNzMxXC9kNTUzYTltLTk0MzUyZDQwLTc4YzctNDMzZi1iODY3LTgwMWUwYTA0ZjU2My5qcGciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.MLpVI785Bl0H8UKlTJeqil4l2Dr2lERfgkYCrotQ4Yg")
    create_new_user(username="Bob_the_dev", email="bob_dev@checkmarx.com", password="IamDev", image="https://res.cloudinary.com/practicaldev/image/fetch/s--h93cj2BI--/c_fill,f_auto,fl_progressive,h_320,q_auto,w_320/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/336281/766eff39-964e-4acc-a390-bc0e2bc9d459.jpg")
    create_new_article(slug="Dev_updates_1", title="Dev updates #1",
                       description="First update after launch",
                       body="1. Updating the typings in ts\n2. Integrating the new Redis db for caching\n3. Updating the main docker image version\n4. Changing the API functions to async IO",
                       author_id="2",
                       tags = ["dev", "updates"])
    create_new_article(slug="Dev_updates_2", title="Dev updates #2",
                       description="Improvments and bug fixes",
                       body="1. Fixed the UI bug after uploading an article\n2. Updated redis versions\n3. Improvments in the enviorment for speed\n4. Updated dependencies\n5. Removed the notification feature",
                       author_id="2",
                       tags=["dev", "updates"])
    create_new_user(username="Hodor", email="holdthedoor@checkmarx.com", password="NoSecIssues", image="https://pyxis.nymag.com/v1/imgs/9bc/c6e/b9ba697b64de36b21e4d2dfb1755b20bbb-23-got-ep-5-002.rsquare.w700.jpg")
    create_new_article(slug="Dev_updates_3", title="Dev updates #3",
                       description="Security push",
                       body="1. Updated 6 packages with high sevierity vulnerabilities\n2. Fixed the stored XSS via the tag input",
                       author_id="3",
                       tags=["security", "dev", "updates"])
    create_new_article(slug="Dev_updates_4", title="Dev updates #4",
                       description="Un secured endpoints",
                       body="Unfortunately, we didnt have time to fix all issues..\nThere are few endpoints which are open to the world while they should have been restricted\nIm afaraid that some of them might be very sensitive ones like devops or administrative endpoints",
                       author_id="3",
                       tags=["security", "dev", "updates"])
    create_new_article(slug="I am Pikachu!", title="I am Pikachu!", description="I am the only Pikachu here, you cant have it!",
                       body="There is only one Pikachu! you can be Balbazur if you want.. contact me at Pikachu@checkmarx.com", author_id="1",
                       tags=["pokemon"])
    create_new_article(slug="My favourite pokemon!", title="My favourites pokemon!",
                       description="You will never guess what are my favourite pokemons!",
                       body="flygon\nluxray\ngarchomp\ngyarados\nabsol\nninetales\ntorterra\nkomala\nlurantis\ncharizard\ngengar\narcanine\nbulbasaur\ndragonite\nBlaziken\nsnorlax\nMudkip\nJigglypuff\nninetals\nsquirtle",
                       author_id="1",
                       tags=["pokemon"])
    create_new_user(username="Ash Ketchum", email="Ash Ketchum@checkmarx.com", password="Gotta Catch ’Em All", image="https://i.stack.imgur.com/3N48C.png?s=256&g=1")
    create_new_user(username="Blastoise", email="Blastoise@checkmarx.com", password="powerfulwater", image="https://www.serebii.net/dungeonrescueteamdx/pokemon/009.png")
    create_new_user(username="Dragonite", email="Dragonite@checkmarx.com", password="firebomb", image="https://static.wikia.nocookie.net/pkmnshuffle/images/a/a6/Dragonite.png/revision/latest?cb=20170407191605")
    create_new_user(username="Gengar", email="Gengar@checkmarx.com", password="ghostly", image="https://i.pinimg.com/736x/54/2c/7f/542c7f7e89f0deb1186bbf9242ebc3ae.jpg")
    create_new_article(slug="Gotta Catch ’Em All!", title="Gotta Catch ’Em All!",
                       description="My Pokemon Team is faster than light. Surrender now or you’re in for a fight!",
                       body="Maybe you think I’m a little too brash. But the Master is here! And my name is Ash",
                       author_id="4",
                       tags=["pokemon"])
    create_new_article(slug="THIS IS MY AWESOME POST!", title="THIS IS MY AWESOME POST!",
                       description="Whoever comment first will get 1,000,000$ from Pikachu!",
                       body="Cmon! Lets see who will be first to comment!",
                       author_id="5",
                       tags=["pokemon", "prize"])
    create_new_comment(body="Im the first! Im the first!", author_id="5", article_id="8")
    create_new_comment(body="Oh no.. I never have luck with that, I wish I could be the first comment", author_id="2", article_id="8")

    create_new_user(username="TeamR$cket", email="TeamR$cket@checkmarx.com", password="iamsorich", image="data:image/png;base64,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")
    create_new_article(slug="TeamR$cket", title="TeamR$cket", description="Money Money",
                       body="We have so much money, we will win everyone!", author_id="8",
                       tags=["pokemon", "bitcoin"])

def downgrade() -> None:
    op.drop_table("commentaries")
    op.drop_table("favorites")
    op.drop_table("articles_to_tags")
    op.drop_table("tags")
    op.drop_table("articles")
    op.drop_table("followers_to_followings")
    op.drop_table("users")
    op.execute("DROP FUNCTION update_updated_at_column")
