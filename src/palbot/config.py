from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    root_dir: Path = Path(__file__).parents[2]
    image_name: str = "thijsvanloef/palworld-server-docker:latest"
    container_name: str = "palworld"
    volume_name: str = "palworld_paldata"


config = Config()
