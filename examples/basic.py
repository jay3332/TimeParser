from timeparser import parse

tests = (
    "15 minutes",
    "in 5 hours sleep",
    "eat lunch in an hour",
    "on wednesday",
    "in a month, school ends",
    "5:25 EST",
    "in a second",
    "on christmas day",
    "do this stuff tomorrow",
    "august",
    "august 2022",
    "8/3/2023",
    "13-5-2022"
)

for test in tests:
    print(parse(test, tz="utc"))
