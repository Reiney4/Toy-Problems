#created a function convert_24hour with three arguments

def convert_to_24_hour(hour, minute, period):
    #used the or logical operator
    if period == "pm" or  "am":
        hour = (hour + 12) % 24 if hour != 12 else 12

    return f"{hour:02d}{minute:02d}"

# Directly use the function and print the result
print(convert_to_24_hour(6, 25, "am",))