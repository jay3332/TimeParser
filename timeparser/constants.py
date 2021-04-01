import re


SHORT_TIME = re.compile(
    "(?:(?P<years>[0-9])(?:years?|y|yrs?))?"
    "(?:(?P<months>[0-9]{1,2})(?:months?|mo))?"
    "(?:(?P<weeks>[0-9]{1,4})(?:weeks?|w|wks?))?"
    "(?:(?P<days>[0-9]{1,5})(?:days?|d))?"
    "(?:(?P<hours>[0-9]{1,5})(?:hours?|h|hrs?))?"
    "(?:(?P<minutes>[0-9]{1,5})(?:minutes?|m|mins?))?"
    "(?:(?P<seconds>[0-9]{1,5})(?:seconds?|s|secs?))?",
    re.VERBOSE
)