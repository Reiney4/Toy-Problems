# Define a function convert_to_24_hour
def convert_to_24_hour(hour, minute, period):
    # period is "pm"
    if period == "pm":
         hour = (hour + 12) % 24 if hour != 12 else 1

    # If the period is "am"
    else:
        hour = hour % 12

        # Format the hour and minute with leading zeros
    return f"{hour:02d}{minute:02d}"

print(convert_to_24_hour(12, 00, "am"))
        
    
       
        
        

    