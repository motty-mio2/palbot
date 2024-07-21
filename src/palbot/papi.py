from typing import cast

import requests
import requests.auth
from dotenv import dotenv_values

from palbot.config import config


def get_players() -> int | None:
    env = dotenv_values(dotenv_path=config.root_dir / ".env")

    url = "http://localhost:8212/v1/api/players"

    try:
        response = requests.get(
            url=url,
            auth=requests.auth.HTTPBasicAuth(
                "admin", cast(str, env.get("ADMIN_PASSWORD", "PassWord"))
            ),
        )
        return len(response.json()["players"])

    except requests.exceptions.ConnectionError:
        return None
