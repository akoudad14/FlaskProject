
import argparse
import json
from database.models.Episode import Episode
from database.models.User import User
from app import app
from database import db

app.app_context().push()

db.init_app(app)


def create_users(file_users: str, episodes: list):
    """Create users based on the User's model.

    :param file_users: File containing users (JSON format).
    :param episodes: List of Episodes (based on Episode's model).
    :return: List of Users.
    """
    with open(file_users, 'r') as fp:
        users_raw = json.load(fp)
    users = []
    for user_raw in users_raw:
        episode_ids = set(user_raw.pop('episode'))
        user = User(**user_raw)
        for episode_id in episode_ids:
            user.episodes.append(episodes[episode_id])
        users.append(user)
    return users


def create_episodes(file_episodes: str) -> list:
    """Create episodes based on the Episode's model.

    :param file_episodes: File containing episodes (JSON format).
    :return: List of Episodes.
    """
    with open(file_episodes, 'r') as fp:
        episodes_raw = json.load(fp)
    episodes = [None] * (len(episodes_raw) + 1)
    for episode_raw in episodes_raw:
        episode_raw.pop('characters')
        episode = Episode(**episode_raw)
        episodes[episode.id] = episode
    return episodes


def store(file_users: str, file_episodes: str):
    """Store users and episodes.

    :param file_users: File containing users (JSON format).
    :param file_episodes: File containing episodes (JSON format).
    """
    episodes = create_episodes(file_episodes)
    users = create_users(file_users, episodes)
    db.session.add_all(users)
    db.session.commit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--users", "-u",
                        default="rick_morty-characters_v1.json")
    parser.add_argument("--episodes", "-e",
                        default="rick_morty-episodes_v1.json")
    args = parser.parse_args()
    store(args.users, args.episodes)
