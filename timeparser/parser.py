from datetime import datetime
from .classes import Time
from . import constants


class TimeParseError(Exception):
    pass


def parse(time, **options):
    """
    Parses a string, which should represent a time or timedelta, into
    it's actual datetime form. Should return a timeparser.Time object.

    Supports:
        Simple time-deltas
            e.g. 2h30m

    Options:
        tz: The timezone if it can't parse it through the string
            Default: UTC
        fallback: The fallback time if the parser can't find a time.
            Default: None
        cls: What class to initialize once parsed.
            Default: timeparser.Time
            Note: The class should inherit from timeparser.Time or a TypeError will be raised.
        now: What to interpret as the current time.
            Default: What is returned by datetime.datetime.utcnow()
            Note: This should be a datetime.datetime object.
        suppress: Whether or not to return None rather than raise an error if a time could not be parsed.
            Default: False

    :param time: The string to be parsed.
    :param options: The options for when parsing the string.
    :return: A `timeparser.Time` object representing the output time.
    """
    _timezone = options.get("tz", "UTC")
    _fallback = options.get("fallback", None)
    _cls = options.get("cls", Time)
    _now = options.get("now", datetime.utcnow())
    _suppress = options.get("suppress", False)
    if not isinstance(_now, datetime):
        raise TypeError("Options `now` must be of type datetime.datetime.")
    if not isinstance(_cls, type):
        raise TypeError("Option `cls` must be a class that inherits from timeparser.Time.")
    if not issubclass(_cls, Time):
        raise TypeError("Option `cls` must inherit from timeparser.Time.")

    def _raise(message: str = f"Could not convert \"{time}\" to time."):
        if _fallback:
            return _fallback
        if _suppress:
            return None
        raise TimeParseError(message)

    _total = 0
    if match := constants.SHORT_TIME.fullmatch(time):
        for possible_group in (intervals := {
            "seconds": 1,
            "minutes": 60,
            "hours": 3600,
            "days": 86400,
            "weeks": 86400*7,
            "months": 86400*30,
            "years": 86400*365
        }):
            if group := match.group(possible_group):
                try:
                    _value = float(group)
                except ValueError:
                    return _raise()
                else:
                    _total += intervals[possible_group]*_value

        _timestamp = (_now - datetime.utcfromtimestamp(0)).total_seconds()
        return _cls(datetime.utcfromtimestamp(_timestamp + _total))
