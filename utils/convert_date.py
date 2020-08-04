from datetime import datetime, date

# Converts ISO 8601 date into readable format
def convert_date(date_to_convert):
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    year = int(date_to_convert[0:4])
    month = 0 + int(date_to_convert[6:7])
    day = 0 + int(date_to_convert[8:10])

    # temp fix
    while month < 1:
        month += 1

    converted_date = days[date(year, month, day).weekday(
    )] + " " + months[month-1] + " " + str(day) + ", " + str(year)
    return converted_date