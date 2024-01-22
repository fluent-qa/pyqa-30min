import logging

from revisited.r_config.dynaconf_settings_demo import settings


def test_ensure_env_settings():
    print("setting db_url:",settings.db_url)
    logging.info("setting db_url:",settings.db_url)
    assert settings.db_url== "postgresql://postgres:changeit@test:7432/test_hub"
