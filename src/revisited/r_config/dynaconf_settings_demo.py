import os

from dynaconf import Dynaconf

settings = Dynaconf(
    envar_prefix="fluent",
    settings_file=["configs/settings.toml", "configs/.secrets.toml",
                   "settings.toml", ".secrets.toml"],
    environment=True,
    load_dotenv=True,
    dotenv_path="/.env",  # custom path for .env file to be loaded
    includes=["../config/custom_settings.toml"],
)

settings.validators.validate()


def ensure_env_settings(env_name: str):
    env_switcher_key = settings.ENV_SWITCHER_FOR_DYNACONF
    os.environ[env_switcher_key] = env_name
    settings.reload()


if __name__ == '__main__':
    ensure_env_settings("dev")
    print(settings.db_url)
    ensure_env_settings("test")
    print(settings.db_url)
