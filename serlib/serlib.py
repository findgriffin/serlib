import json
import logging
from typing import Optional, Union
import argparse


Primitive = Union[int, str, bool, float]
Serializable = Union[Primitive, list]
# List[Primitive|Struct|Dict]


def to_json(obj: Serializable) -> str:
    return json.dumps(obj)


def from_json(data: str) -> Serializable:
    return json.loads(data)


def setup(argv) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="This is a Python 3 project.")
    parser.add_argument("--name", type=str, required=False,
                        help="Your name, for example 'Margaret'.")
    parser.add_argument("-v", "--verbose",  action="store_true",
                        help="Enable verbose logging.")
    return parser.parse_args(argv)


def run(name: Optional[str] = None) -> str:
    if name:
        logging.debug("Name given.")
        return f"Hello, {name}!"
    else:
        logging.debug("No name given.")
        return "Hello, world!"
