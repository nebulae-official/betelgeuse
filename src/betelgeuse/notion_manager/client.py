"""Notion Manager API Client.

This module provides a client for interacting with the Notion API.
"""

import requests
from typing import Any, Dict

from .config import NOTION_API_KEY, NOTION_VERSION


class NotionClient:
    """Client for interacting with the Notion API.

    Attributes:
        base_url (str): The base URL for the Notion API.
        headers (Dict[str, str]): HTTP headers for authentication and content type.
    """

    def __init__(self) -> None:
        """Initialize the NotionClient with base URL and authentication headers."""
        self.base_url: str = 'https://api.notion.com/v1'
        self.headers: Dict[str, str] = {
            'Authorization': f'Bearer {NOTION_API_KEY}',
            'Notion-Version': NOTION_VERSION,
            'Content-Type': 'application/json',
        }

    def request(self, method: str, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        """Make a generic HTTP request to the Notion API.

        Args:
            method (str): HTTP method (e.g., "GET", "POST", "PATCH", "DELETE").
            endpoint (str): API endpoint (e.g., "databases/<database_id>").
            **kwargs (Any): Additional keyword arguments for requests.request.

        Returns:
            Dict[str, Any]: Parsed JSON response from the API.

        Raises:
            requests.HTTPError: If the request returns an unsuccessful status code.
        """
        url: str = f'{self.base_url}/{endpoint}'
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_database(self, database_id: str) -> Dict[str, Any]:
        """Retrieve details of a Notion database.

        Args:
            database_id (str): The unique identifier of the Notion database.

        Returns:
            Dict[str, Any]: JSON response containing the database details.
        """
        endpoint: str = f'databases/{database_id}'
        return self.request('GET', endpoint)


def main() -> None:
    """Demonstration of the NotionClient usage."""
    client = NotionClient()
    # Replace 'your_database_id' with a valid Notion database ID for testing.
    database_id = '1a5aede4f2d380bcb38c000c3ac750b6'
    try:
        database = client.get_database(database_id)
        print(database)
    except requests.HTTPError as http_err:
        # Attempt to check if the error is due to integration not being shared.
        try:
            error_data = http_err.response.json()
            error_message = error_data.get('message', '').lower()
        except Exception:
            error_message = ''

        if 'not shared' in error_message or 'access' in error_message:
            answer = input(
                'The integration does not have access to the item. '
                'Have you added (shared) the integration with this item? (y/n): '
            )
            if answer.strip().lower() == 'y':
                print('Please ensure the integration is shared with the item in Notion.')
            else:
                print('Integration not shared. Please add the integration to the item to continue.')
        else:
            print('HTTP error occurred:', http_err)
    except Exception as e:
        print('Error retrieving database:', e)


if __name__ == '__main__':
    main()
