"""Tests for the welcome module of the Betelgeuse CLI."""

import logging
from collections.abc import Generator
from unittest.mock import MagicMock, patch
import socket

import pytest
from colorama import Fore, Style

from nebulae_betelgeuse.welcome import (
    get_welcome_message, 
    display_welcome,
    get_hostname
)


@pytest.fixture
def mock_hostname() -> Generator[MagicMock, None, None]:
    """Fixture to mock the socket.gethostname function."""
    with patch("socket.gethostname", return_value="test-host") as mock:
        yield mock


@pytest.fixture
def mock_version() -> Generator[MagicMock, None, None]:
    """Fixture to mock the betelgeuse version."""
    with patch("nebulae_betelgeuse.welcome.betelgeuse_version", "1.2.3") as mock:
        yield mock


class TestWelcome:
    """Test suite for welcome module functionality."""

    def test_get_welcome_message_basic(self, mock_version: MagicMock) -> None:
        """Test that get_welcome_message returns a properly formatted message."""
        message = get_welcome_message()
        assert isinstance(message, str)
        assert len(message) > 0
        assert "Welcome to Betelgeuse v1.2.3" in message
        assert "https://github.com" in message

    def test_welcome_message_includes_hostname(self, mock_hostname: MagicMock) -> None:
        """Test welcome message includes the hostname."""
        message = get_welcome_message()
        assert "test-host" in message
        mock_hostname.assert_called_once()

    def test_get_hostname_error_handling(self) -> None:
        """Test that get_hostname handles errors properly."""
        with patch("socket.gethostname", side_effect=OSError("Test error")):
            hostname = get_hostname()
            assert hostname == "unknown-host"

    @patch("nebulae_betelgeuse.welcome.get_welcome_message", return_value="Test welcome message")
    @patch("nebulae_betelgeuse.welcome.logging.info")
    def test_display_welcome(self, mock_info: MagicMock, mock_welcome: MagicMock) -> None:
        """Test that display_welcome calls logging.info with the welcome message."""
        display_welcome()
        mock_welcome.assert_called_once()
        mock_info.assert_called_once_with("Test welcome message")
