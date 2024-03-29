# coding: utf-8

"""
    GitLab API

    An OpenAPI definition for the GitLab REST API. Few API resources or endpoints are currently included. The intent is to expand this to match the entire Markdown documentation of the API: <https://docs.gitlab.com/ee/api/>. Contributions are welcome.  When viewing this on gitlab.com, you can test API calls directly from the browser against the `gitlab.com` instance, if you are logged in. The feature uses the current [GitLab session cookie](https://docs.gitlab.com/ee/api/index.html#session-cookie), so each request is made using your account.  Instructions for using this tool can be found in [Interactive API Documentation](https://docs.gitlab.com/ee/api/openapi/openapi_interactive.html) 

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.broadcast_messages_api import BroadcastMessagesApi


class TestBroadcastMessagesApi(unittest.TestCase):
    """BroadcastMessagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BroadcastMessagesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_api_v4_broadcast_messages_id(self) -> None:
        """Test case for delete_api_v4_broadcast_messages_id

        Delete a broadcast message
        """
        pass

    def test_get_api_v4_broadcast_messages(self) -> None:
        """Test case for get_api_v4_broadcast_messages

        Get all broadcast messages
        """
        pass

    def test_get_api_v4_broadcast_messages_id(self) -> None:
        """Test case for get_api_v4_broadcast_messages_id

        Get a specific broadcast message
        """
        pass

    def test_post_api_v4_broadcast_messages(self) -> None:
        """Test case for post_api_v4_broadcast_messages

        Create a broadcast message
        """
        pass

    def test_put_api_v4_broadcast_messages_id(self) -> None:
        """Test case for put_api_v4_broadcast_messages_id

        Update a broadcast message
        """
        pass


if __name__ == '__main__':
    unittest.main()
