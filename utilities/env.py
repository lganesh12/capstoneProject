<<<<<<< HEAD
from dotenv import load_dotenv
import os
=======
import os

from dotenv import load_dotenv

>>>>>>> ef4417a (Added files)
from features.variable import PROJECT_ROOT


def load_env():
<<<<<<< HEAD
    env_path = PROJECT_ROOT/".env"
    load_dotenv(dotenv_path=env_path)

=======
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(dotenv_path=env_path)


>>>>>>> ef4417a (Added files)
def get_env_value(name):
    value = os.getenv(name)
    if value is None:
        raise KeyError(f"Environment variable {name} not found.")
    return value

<<<<<<< HEAD
def is_truthy(bool_as_string: str):
    bool_as_string = {"1": "true", "0": "false"}.get(bool_as_string, bool_as_string)
    return bool_as_string.lower() == "true"
=======

def is_truthy(bool_as_string: str):
    bool_as_string = {"1": "true", "0": "false"}.get(bool_as_string, bool_as_string)
    return bool_as_string.lower() == "true"
>>>>>>> ef4417a (Added files)
