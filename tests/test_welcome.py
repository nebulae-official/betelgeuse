"""Tests for the welcome module of the Betelgeuse CLI."""

import re
from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest
from colorama import Fore, Style

from betelgeuse.cli.welcome import get_welcome_message


@pytest.fixture
def mock_hostname() -> Generator[MagicMock, None, None]:
    """Fixture to mock the socket.gethostname function."""
    with patch("socket.gethostname", return_value="test-host") as mock:
        yield mock


@pytest.fixture
def mock_version() -> Generator[MagicMock, None, None]:
    """Fixture to mock the betelgeuse version."""
    with patch("betelgeuse.cli.welcome.betelgeuse_version", "1.2.3") as mock:
        yield mock


class TestWelcome:
    """Test suite for welcome module functionality."""

    def test_get_welcome_message_returns_string(self) -> None:
        """Test that get_welcome_message returns a non-empty string."""
        message = get_welcome_message()
        assert isinstance(message, str)
        assert len(message) > 0

    @pytest.mark.parametrize(
        "expected_text",
        [
            "Welcome to Betelgeuse",
            "Embark on a stellar journey",
            "documentation, tutorials",
            "powerful tools",
            "guide you through",
            "https://github.com",
        ],
    )
    def test_welcome_message_contains_expected_phrases(
        self,
        expected_text: str,
    ) -> None:
        """Test that welcome message contains key informational phrases."""
        message = get_welcome_message()
        assert expected_text in message

    def test_welcome_message_contains_version(self, mock_version: MagicMock) -> None:
        """Test that welcome message contains version information."""
        message = get_welcome_message()
        assert "v1.2.3" in message

    @pytest.mark.parametrize(
        "color_code",
        [Fore.BLUE, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Style.BRIGHT],
    )
    def test_welcome_message_has_color_codes(self, color_code: str) -> None:
        """Test that welcome message includes specific color formatting codes."""
        message = get_welcome_message()
        assert color_code in message

    def test_welcome_message_mentions_betelgeuse(self) -> None:
        """Test that welcome message mentions Betelgeuse."""
        message = get_welcome_message()
        assert "Betelgeuse" in message

    def test_welcome_message_includes_hostname(self, mock_hostname: MagicMock) -> None:
        """Test welcome message includes the hostname."""
        message = get_welcome_message()
        assert "test-host" in message
        mock_hostname.assert_called_once()

    def test_github_url_in_welcome_message(self) -> None:
        """Test that welcome message includes GitHub URL."""
        message = get_welcome_message()
        assert re.search(r"https://github\.com/[\w-]+/betelgeuse", message) is not None

    @patch("socket.gethostname", side_effect=OSError("Network error"))
    def test_welcome_message_handles_hostname_error(
        self,
        mock_hostname_error: MagicMock,
    ) -> None:
        """Test that welcome message handles errors when getting hostname."""
        try:
            # This should raise an exception if not properly handled in the code
            message = get_welcome_message()
            # If we reach here, the function is handling the error, which is good
            assert isinstance(message, str)
            assert "Welcome to Betelgeuse" in message
        except OSError as e:
            pytest.fail(f"get_welcome_message() did not handle hostname error: {e}")
