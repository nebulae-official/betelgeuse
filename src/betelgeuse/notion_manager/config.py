import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env if available


def check_notion_api_key() -> bool:
    """Check if the NOTION_API_KEY environment variable is missing, empty, or set to None.

    Returns:
        bool: True if the NOTION_API_KEY is not set, is an empty string, or is None. Otherwise, returns False.
    """
    if (
        'NOTION_API_KEY' not in os.environ
        or os.environ['NOTION_API_KEY'] == ''
        or os.environ['NOTION_API_KEY'] is None
    ):
        raise ValueError('NOTION_API_KEY must be set in the environment variables.')
    return True


# Ensure that the NOTION_API_KEY is set
check_notion_api_key()


NOTION_API_KEY = os.getenv('NOTION_API_KEY')
NOTION_VERSION = os.getenv('NOTION_VERSION', '2022-06-28')
