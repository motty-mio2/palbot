from abc import ABCMeta, abstractmethod

import docker  # type:ignore
import docker.errors  # type:ignore
import docker.models  # type:ignore
import docker.models.containers  # type:ignore

from palbot.models import msg  # type: ignore


class ContainerMNG(metaclass=ABCMeta):
    def __init__(self, container_name: str) -> None:
        self.client = docker.from_env()

        self.container: docker.models.containers.Container | None = None
        self.container_name: str = container_name

        try:
            self._create_container()
        except docker.errors.APIError:
            self._delete_container()
            self._create_container()

    @abstractmethod
    def _create_container(self) -> None:
        pass

    def _delete_container(self) -> None:
        cid: list[docker.models.containers.Container] = self.client.containers.list(
            all=True, filters={"name": self.container_name}
        )
        cid[0].stop()
        cid[0].remove()

    def _is_container_running(self) -> bool:
        if self.container is None:
            return False
        else:
            self.container.reload()
            if self.container.status == "running":
                return True
            else:
                return False

    def start_container(self) -> msg:
        if self._is_container_running():
            return msg(status=True, msg="Container already running.")
        else:
            if self.container is not None:
                self.container.start()

            if self._is_container_running():
                return msg(status=True, msg="Container Start.")
            else:
                return msg(status=False, msg="Failed to Start Container.")

    def stop_container(self) -> msg:
        if self.container is not None:
            self.container.stop()

        if self._is_container_running():
            return msg(status=False, msg="Failed to Stop Container.")
        return msg(status=True, msg="Container Stopped.")
