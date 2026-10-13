import datetime

def time_difference(date1, date2):
    diff = (date2 - date1).days
    if diff < 0:
        print(abs(diff))
    return diff