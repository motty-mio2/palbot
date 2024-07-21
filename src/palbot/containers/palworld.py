from dotenv import dotenv_values

from palbot.config import config  # type: ignore

from ._base import ContainerMNG  # type:ignore


class PalworldMNG(ContainerMNG):
    def _create_container(self) -> None:
        env = dotenv_values(dotenv_path=config.root_dir / "pal.env")

        self.client.images.pull(repository=config.image_name)

        self.container = self.client.containers.create(
            image=config.image_name,
            name=config.container_name,
            detach=True,
            environment=env,
            ports={"8211/udp": "8211", "27015/udp": "27015", "8212/tcp": "8212"},
            volumes={config.volume_name: {"bind": "/palworld", "mode": "rw"}},
        )


cnmg = PalworldMNG(container_name=config.container_name)
