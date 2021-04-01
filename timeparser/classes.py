from datetime import datetime
try:
    from discord.ext.commands import Converter, ConversionError
    _has_discord = True
except ImportError:
    _has_discord = False
    ConversionError = None
    Converter = None


def _human_readable(iterable):
    if len(iterable) <= 2:
        return " and ".join(iterable)
    return ", ".join(iterable[:-1]) + f", and {iterable[-1]}"


class Time:
    """
    Represents a time parsed from the parser.
    Has information such as the datetime, reason, and elapsed time.
    """
    def __init__(self, dt, reason=None):
        self.time = dt
        self.reason = reason
        self.delta = dt - datetime.utcnow()

        self.unix = (dt - datetime.utcfromtimestamp(0)).total_seconds()
        self.raw_delta = self.delta.total_seconds()

    def __str__(self):
        """ A shortcut for self.human_delta """
        return self.human_delta()

    def __repr__(self):
        """ Returns the repr of the datetime """
        return "timeparser.Time(%s, delta=%i)" % (repr(self.time), self.raw_delta)

    def human_delta(self, depth=3):
        """
        Converts a raw second delta measurement into a human friendly string.

        :param depth: The amount of units to be accurate to
        :return: A string representing the raw delta. E.g. 4 minutes and 6 seconds
        """
        force_round = False
        if self.raw_delta <= 0:
            return '0 seconds'
        if self.raw_delta >= 60:
            force_round = True

        m, s = divmod(self.raw_delta, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        mo, d = divmod(d, 30)
        y, mo = divmod(mo, 12)

        if int(s) == s or force_round:
            s = int(s)

        if y > 100: return ">100 years"

        y, mo, d, h, m = round(y), round(mo), round(d), round(h), round(m)
        measurements = ((y, 'year'), (mo, 'month'), (d, 'day'), (h, 'hour'), (m, 'minute'), (s, 'second'))

        as_list = [f"{c[0]} {c[1]}{'s' if c[0] != 1 else ''}" for c in measurements if c[0] > 0]
        return _human_readable(as_list[0:depth])


if _has_discord:
    from . import parser
    from abc import ABC

    class TimeConversionError(ConversionError):
        pass


    class TimeConverter(Converter, ABC):
        """
        If this user has the discord package,
        then this class will exist so that the user won't have to implement
        their own TimeConverter.

        Usage is as so:
            @commands.command()
            async def get_time(ctx, time: timeparser.TimeConverter):
                await ctx.send(time)  # Should automatically cast to string
        """
        async def convert(self, ctx, arg):
            arg = parser.parse(arg, tz="utc", suppress=True)
            if not arg:
                raise TimeConversionError('Could not convert "%s" to a time or date.' % arg)
            return arg

else:
    class TimeConverter: pass
    class TimeConversionError(Exception): pass
