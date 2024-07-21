from dataclasses import dataclass


@dataclass
class msg:
    status: bool
    msg: str
