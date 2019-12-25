from ast import literal_eval
from common import redb


def get_common_prefix_redis_keys(prefix):
    return redb.scan_iter(f"{prefix}*")


def string_splitter(source_str: str, split_by: str, prefix=None) -> list:
    split_list = source_str.split(split_by)
    if prefix:
        return [f"{prefix}_{val}" for val in split_list]
    return split_list


def get_key(key: str) -> str:
    return string_splitter(key, ':')[1]


def get_redis_data(key: str) -> str:
    return redb.get(key)


def isiterable(val):
    if isinstance(val, dict) or isinstance(val, list):
        return True
    return


def set_redis_iterable_data(key, value) -> None:
    return redb.set(key, str(value))


def set_redis_data(key: str, value: str) -> None:
    if isiterable(value):
        return set_redis_iterable_data(key, value)
    return redb.set(key, value)


def set_ttl(key: str, time_to_live: int = 5) -> None:
    return redb.expire(key, time_to_live)


def reset_ttl(key):
    return set_ttl(key)


def string_to_dict(data: bytes) -> str:
    return literal_eval(data.decode())



