
from unittest import TestCase
from unittest.mock import patch, mock_open, Mock
from data import import_data


class TestImport(TestCase):

    @patch("data.import_data.Episode")
    @patch("data.import_data.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_create_episodes(
            self,
            open_mock: Mock,
            load_mock: Mock,
            episode_mock: Mock):
        episode_raw = {"id": 1, "name": "Pilot", "air_date": "December 2, 2013",
                       "episode": "S01E01", "characters": [1, 2]}
        load_mock.return_value = [episode_raw]
        file_name = Mock()

        episodes = import_data.create_episodes(file_name)

        open_mock.assert_called_with(file_name, 'r')
        load_mock.assert_called_with(open_mock.return_value)
        episode_mock.assert_called_with(id=episode_raw['id'],
                                        name=episode_raw['name'],
                                        air_date=episode_raw['air_date'],
                                        episode=episode_raw['episode'])
        self.assertEqual(episodes, [None, episode_mock.return_value])

    @patch("data.import_data.User")
    @patch("data.import_data.json.load")
    @patch("builtins.open", new_callable=mock_open)
    def test_create_users(
            self,
            open_mock: Mock,
            load_mock: Mock,
            user_mock: Mock):
        user_raw = {"id": 1, "name": "Rick Sanchez", "status": "Alive",
                    "species": "Human", "type": "", "gender": "Male",
                    "episode": [1]}
        episodes = [None, Mock(), Mock()]
        load_mock.return_value = [user_raw]
        file_name = Mock()

        users = import_data.create_users(file_name, episodes)

        open_mock.assert_called_with(file_name, 'r')
        load_mock.assert_called_with(open_mock.return_value)
        user_mock.assert_called_with(id=user_raw['id'],
                                     name=user_raw['name'],
                                     status=user_raw['status'],
                                     species=user_raw['species'],
                                     type=user_raw['type'],
                                     gender=user_raw['gender'])
        self.assertEqual(users, [user_mock.return_value])
        users[0].episodes.append.assert_called_with(episodes[1])

