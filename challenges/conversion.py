def convert_to_24_hour(hour, minute, period):
    if period == "pm":
        hour = (hour + 12) % 24 if hour != 12 else 12
    else:
        hour = hour % 12

    return f"{hour:02d}{minute:02d}"