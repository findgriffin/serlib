import json
import logging
from typing import Optional, Union, Type, cast, NamedTuple
import argparse


Primitive = Union[int, str, bool, float]
Struct = dict[str, list[Primitive] | Primitive | Optional[Primitive]]
Serializable = Struct | list[Struct]


TYPE_MAP: dict[str, Type] = {}


def parsable(type_def: Type):
    TYPE_MAP[type_def.__name__] = type_def
    return type_def


def _is_namedtuple(obj: Serializable) -> bool:
    return (
            isinstance(obj, tuple) and
            hasattr(obj, '_asdict') and
            hasattr(obj, '_fields')
    )


def to_json(obj: Serializable) -> str:
    if _is_namedtuple(obj):
        nt_dict = cast(NamedTuple, obj)._asdict()
        return json.dumps({obj.__class__.__name__: nt_dict})
    else:
        return json.dumps(obj)


def from_json(data: str, decodable: Optional[dict[str, Type]] = None
              ) -> Serializable:
    loaded = json.loads(data)
    if decodable and len(loaded) == 1:
        key = next(iter(loaded))
        if key in decodable.keys():
            return decodable[key](**loaded[key])
    return loaded


def setup(argv) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="This is a Python 3 project.")
    parser.add_argument("--name", type=str, required=False,
                        help="Your name, for example 'Margaret'.")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose logging.")
    return parser.parse_args(argv)


def run(name: Optional[str] = None) -> str:
    if name:
        logging.debug("Name given.")
        return f"Hello, {name}!"
    else:
        logging.debug("No name given.")
        return "Hello, world!"
