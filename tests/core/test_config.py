import pytest

from app.core.config import Settings


def test_settings_load_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/test")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")

    settings = Settings(_env_file=None)

    assert settings.database_url == "postgresql://user:pass@localhost:5432/test"
    assert settings.openai_api_key.get_secret_value() == "sk-test-key"


def test_api_key_is_hidden_in_repr(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/test")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")

    settings = Settings(_env_file=None)

    assert "sk-test-key" not in repr(settings)
