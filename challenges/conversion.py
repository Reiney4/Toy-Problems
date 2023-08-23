# Define the function to convert 12-hour time to 24-hour time
def convert_to_24_hour(hour, minute, period):
    # If the period is "pm"
    if period == "pm":
        # Add 12 to the hour (unless it's 12 PM, then set it to 12)
        hour = (hour + 12) % 24 if hour != 12 else 12
    else:
        # If the period is "am", convert 12 AM to 0 hour, otherwise keep the same hour
        hour = hour % 12

    # Format the hour and minute with leading zeros, if needed, and combine them
    return f"{hour:02d}{minute:02d}"

print(convert_to_24_hour(8, 30, "am"))