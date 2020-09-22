from dataclasses import dataclass


@dataclass
class Entity:

    id = str
    name = str
    phone = str
    email = str
    addr = str
