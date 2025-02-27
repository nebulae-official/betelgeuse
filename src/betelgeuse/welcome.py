"""Welcome module for the Betelgeuse CLI application.

This module provides functionality to generate and display colorful welcome message
when users interact with the Betelgeuse library. It includes version information,
hostname identification, and links to documentation resources.

Functions:
    get_welcome_message(): Generates a formatted welcome message string
    display_welcome(): Prints the welcome message to the console
"""

import logging
import socket

from colorama import Fore, Style, init

from betelgeuse import __version__ as betelgeuse_version

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_hostname() -> str:
    """Get the system's hostname safely.

    Returns:
        str: The hostname or 'unknown-host' if unable to retrieve.

    """
    try:
        return socket.gethostname()
    except (socket.herror, socket.gaierror, OSError) as e:
        logging.debug("Could not retrieve hostname: %s", e)
        return "unknown-host"


def get_welcome_message() -> str:
    """Generate a welcome message for Betelgeuse library.

    Returns:
        str: A formatted welcome message with colors and emojis.

    """
    # Initialize colorama to support ANSI colors on Windows as well
    init(autoreset=True)

    # Get hostname
    hostname = get_hostname()

    return (
        f"{Fore.BLUE}{Style.BRIGHT}🌟 Welcome to Betelgeuse v{betelgeuse_version}! 🚀\n"
        f"{Fore.YELLOW}Hello, {hostname}! Embark on a stellar journey as you explore"
        " powerful tools designed to illuminate your projects. ☄️\n"
        f"{Fore.GREEN}Betelgeuse is here to guide you through the cosmos of data"
        " processing and analysis.\n"
        f"For documentation, tutorials, and support, visit: {Fore.CYAN}https://github.com/nebulae-official/betelgeuse\n"
        f"{Style.RESET_ALL}"
    )


def display_welcome() -> None:
    """Print the welcome message to the console."""
    logging.info(get_welcome_message())


if __name__ == "__main__":
    display_welcome()
