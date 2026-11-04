"""Regression checks for the VideosIA fork's deliberate privacy defaults."""
import os
import tomllib
from pathlib import Path
from unittest.mock import patch

from app.services import version_checker


def test_background_update_check_is_disabled_without_opt_in():
    with patch.dict(os.environ, {}, clear=True), patch.object(
        version_checker._ASYNC_UPDATE_CHECKER, "poll"
    ) as poll:
        snapshot = version_checker.poll_available_update("1.3.9")
    assert snapshot.complete is True
    assert snapshot.available_version is None
    poll.assert_not_called()


def test_background_update_check_can_be_explicitly_enabled():
    with patch.dict(os.environ, {"MPT_CHECK_UPDATES": "1"}), patch.object(
        version_checker._ASYNC_UPDATE_CHECKER, "poll"
    ) as poll:
        version_checker.poll_available_update("1.3.9")
    poll.assert_called_once_with("1.3.9")


def test_example_is_loopback_with_private_logging():
    config = tomllib.loads(
        (Path(__file__).resolve().parents[2] / "config.example.toml").read_text("utf-8")
    )
    assert config["listen_host"] == "127.0.0.1"
    assert config["log_level"] == "WARNING"
    assert config["diagnostics"]["log_requests"] is False
