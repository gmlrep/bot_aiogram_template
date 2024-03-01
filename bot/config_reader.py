from os import getenv
from pathlib import Path

from pydantic import SecretStr, BaseModel
from yaml import load as yaml_load

try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import Loader


class BotSettings(BaseModel):
    token: SecretStr
    admin_list_id: str
    language: str
    throttling: int


class Settings(BaseModel):
    bot: BotSettings


def parse_settings(local_file_name: str = "settings.yml") -> Settings:
    file_path = getenv("FEEDBACK_BOT_CONFIG_PATH")
    if file_path is not None:
        # Check if path exists
        if not Path(file_path).is_file():
            raise ValueError("Path %s is not a file or doesn't exist", file_path)
    else:
        parent_dir = Path(__file__).parent.parent
        settings_file = Path(Path.joinpath(parent_dir, local_file_name))
        if not Path(settings_file).is_file():
            raise ValueError("Path %s is not a file or doesn't exist", settings_file)
        file_path = settings_file.absolute()
    with open(file_path, "rt") as file:
        config_data = yaml_load(file, Loader)
    return Settings.model_validate(config_data)
