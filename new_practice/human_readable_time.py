def make_readable(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if hours > 99:
        return "Out of range"
    
    return "%02d:%02d:%02d" % (hours, minutes, seconds)

print(make_readable(90))