import datetime

import pytz


def time_to_epoch(year:int, month:int, day:int, hour:int, minute:int, timezone:str):
    tz = pytz.timezone(timezone)

    date_time = tz.localize(datetime.datetime(year, month, day, hour, minute))

    epoch = datetime.datetime(1970, 1, 1, tzinfo=pytz.utc)
    delta = date_time - epoch
    return int(delta.total_seconds())

def tz():
    tz = 'Europe/Paris'
    return tz
