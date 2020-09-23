from dataclasses import dataclass


@dataclass
class Entity:
    context: str = '/Users/hong/Desktop/sbaproject/titanic/data/'
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''
