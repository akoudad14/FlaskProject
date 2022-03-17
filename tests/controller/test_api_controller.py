
from unittest import TestCase
from unittest.mock import patch, Mock

from Controller.ApiController import ApiController


class TestApiController(TestCase):

    @patch("Controller.ApiController.CharacterService")
    def test_all_characters(
            self,
            service_mock: Mock):
        controller = ApiController()

        controller.get_all_characters()

        service_mock.assert_called_with()
        service_mock.return_value.get_all.assert_called_with()

    @patch("Controller.ApiController.EpisodeService")
    def test_all_episodes(
            self,
            service_mock: Mock):
        controller = ApiController()

        controller.get_all_episodes()

        service_mock.assert_called_with()
        service_mock.return_value.get_all.assert_called_with()

    @patch("Controller.ApiController.CommentService")
    def test_all_comments(
            self,
            service_mock: Mock):
        controller = ApiController()

        controller.get_all_comments()

        service_mock.assert_called_with()
        service_mock.return_value.get_all.assert_called_with()

    @patch("Controller.ApiController.CommentService")
    @patch("Controller.ApiController.EpisodeService")
    @patch("Controller.ApiController.CharacterService")
    def test_add_character_episode_comment(
            self,
            character_mock: Mock,
            episode_mock: Mock,
            comment_mock: Mock):
        controller = ApiController()
        comment = Mock()
        episode_id = Mock()
        character_id = Mock()
        comment_dict = {'comment': comment,
                        'episode_id': episode_id,
                        'character_id': character_id}

        controller.add_comment(comment_dict)

        character_mock.assert_called_with()
        character_mock.return_value.get_one.assert_called_with(character_id,
                                                               dump=False)
        episode_mock.assert_called_with()
        episode_mock.return_value.get_one.assert_called_with(episode_id,
                                                             dump=False)
        comment_mock.assert_called_with()
        character = character_mock.return_value.get_one.return_value
        episode = episode_mock.return_value.get_one.return_value
        comment_mock.return_value.insert.assert_called_with({
            'comment': comment_dict['comment'],
            'episode': [episode],
            'character': [character]
        })

    @patch("Controller.ApiController.CommentService")
    @patch("Controller.ApiController.EpisodeService")
    @patch("Controller.ApiController.CharacterService")
    def test_add_character_comment(
            self,
            character_mock: Mock,
            episode_mock: Mock,
            comment_mock: Mock):
        controller = ApiController()
        comment = Mock()
        character_id = Mock()
        comment_dict = {'comment': comment,
                        'character_id': character_id}

        controller.add_comment(comment_dict)

        character_mock.assert_called_with()
        character_mock.return_value.get_one.assert_called_with(character_id,
                                                               dump=False)
        episode_mock.assert_not_called()

        comment_mock.assert_called_with()
        character = character_mock.return_value.get_one.return_value
        comment_mock.return_value.insert.assert_called_with({
            'comment': comment_dict['comment'],
            'character': [character]
        })

    @patch("Controller.ApiController.CommentService")
    @patch("Controller.ApiController.EpisodeService")
    @patch("Controller.ApiController.CharacterService")
    def test_add_episode_comment(
            self,
            character_mock: Mock,
            episode_mock: Mock,
            comment_mock: Mock):
        controller = ApiController()
        comment = Mock()
        episode_id = Mock()
        comment_dict = {'comment': comment,
                        'episode_id': episode_id}

        controller.add_comment(comment_dict)

        character_mock.assert_not_called()
        episode_mock.assert_called_with()
        episode_mock.return_value.get_one.assert_called_with(episode_id,
                                                             dump=False)
        comment_mock.assert_called_with()
        episode = episode_mock.return_value.get_one.return_value
        comment_mock.return_value.insert.assert_called_with({
            'comment': comment_dict['comment'],
            'episode': [episode]
        })

    @patch("Controller.ApiController.CommentService")
    @patch("Controller.ApiController.EpisodeService")
    @patch("Controller.ApiController.CharacterService")
    def test_update_comment(
            self,
            character_mock: Mock,
            episode_mock: Mock,
            comment_mock: Mock):
        controller = ApiController()
        comment_id = Mock()
        comment = Mock()
        comment_dict = {'comment': comment}

        controller.update_comment(comment_id, comment_dict)

        character_mock.assert_not_called()
        episode_mock.assert_not_called()
        comment_mock.assert_called_with()
        update_comment_dict = {
            'comment': comment_dict['comment']
        }
        comment_mock.return_value.update.assert_called_with(
            comment_id,
            **update_comment_dict
        )
