import json
from typing import Any


def to_pretty_json(obj: dict) -> str:
    def handle_recursive_objects(o: Any) -> dict | list | str:
        if isinstance(o, dict):
            return {k: handle_recursive_objects(v) for k, v in o.items()}
        if isinstance(o, list):
            return [handle_recursive_objects(v) for v in o]
        if hasattr(o, "__dict__"):
            return handle_recursive_objects(o.__dict__)
        return str(o)

    return json.dumps(handle_recursive_objects(obj), indent=4)


# def to_pretty_json(obj: dict) -> str:
#    def handle_recursive_objects(o):
#        if isinstance(o, dict):
#            return {k: handle_recursive_objects(v) for k, v in o.items()}
#        elif isinstance(o, list):
#            return [handle_recursive_objects(v) for v in o]
#        elif hasattr(o, "__dict__"):
#            return handle_recursive_objects(o.__dict__)
#        else:
#            return str(o)
#
#    return json.dumps(handle_recursive_objects(obj), indent=4)
