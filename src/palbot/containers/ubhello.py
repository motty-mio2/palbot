from ._base import ContainerMNG  # type:ignore


class UbuntuMNG(ContainerMNG):
    def _create_container(self) -> None:
        self.client.images.pull(repository="ubuntu:latest")

        self.container = self.client.containers.create(
            image="ubuntu:latest",
            command="sleep 1000",
            name="ub",
            detach=True,
        )


cnmg = UbuntuMNG(container_name="ub")
