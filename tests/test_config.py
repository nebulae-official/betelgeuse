from importlib import reload
import pytest

import notion_manager.config


def test_missing_api_key(monkeypatch):
    monkeypatch.delenv('NOTION_API_KEY', raising=False)
    with pytest.raises(
        ValueError, match='NOTION_API_KEY must be set in the environment variables.'
    ):
        notion_manager.config.check_notion_api_key()


def test_empty_api_key(monkeypatch):
    monkeypatch.setenv('NOTION_API_KEY', '')
    with pytest.raises(
        ValueError, match='NOTION_API_KEY must be set in the environment variables.'
    ):
        reload(notion_manager.config)


def test_valid_api_key_default_version(monkeypatch):
    valid_key = 'valid_api_key'
    monkeypatch.setenv('NOTION_API_KEY', valid_key)
    monkeypatch.delenv('NOTION_VERSION', raising=False)
    mod = reload(notion_manager.config)
    assert mod.NOTION_API_KEY == valid_key
    assert mod.NOTION_VERSION == '2022-06-28'


def test_valid_api_key_custom_version(monkeypatch):
    valid_key = 'valid_api_key'
    custom_version = '2023-01-01'
    monkeypatch.setenv('NOTION_API_KEY', valid_key)
    monkeypatch.setenv('NOTION_VERSION', custom_version)
    mod = reload(notion_manager.config)
    assert mod.NOTION_API_KEY == valid_key
    assert mod.NOTION_VERSION == custom_version
