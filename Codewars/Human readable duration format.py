"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
It is much easier to understand with an example:
* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.
Note that spaces are important.
"""

seconds = 136625465
def format_duration(seconds):
    if seconds == 0:
        return 'now'
    units = [
        (31536000, 'year'),
        (86400, 'day'),
        (3600, 'hour'),
        (60, 'minute'),
        (1, 'second')
    ]
    parts = []
    for secs, name in units:
        qty, seconds = divmod(seconds, secs)
        if qty > 0:
            parts.append(f"{qty} {name}{'s' if qty > 1 else ''}")

    if len(parts) == 1:
        return parts[0]
    return ', '.join(parts[:-1]) + ' and ' + parts[-1]

test = format_duration(seconds)
print(test)