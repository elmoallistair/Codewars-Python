# Written: 27-Apr-2020
# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    if not seconds: return 'now'

    times = [
        (31536000, ' years'),
        (86400, ' days'),
        (3600, ' hours'),
        (60, ' minutes'),
        (1, ' seconds')
    ]

    format = []
    for unit, name in times:
        value, seconds = divmod(seconds, unit)
        if value > 0:
            formatted.append(str(value) + (name if value > 1 else name[:-1]))

    # if len(format) == 1:
    #     return ''.join(format)
    # elif len(formatted) == 2:
    #     return ' and '.join(format)
    # else:
    #     return ', '.join(format[:-1]) + ' and ' + format[-1]
    return ', '.join([str(val) for val in format[:-1]]) + (' and ' if len(format) > 1 else '') + format[-1]