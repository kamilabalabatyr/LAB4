from datetime import datetime, timedelta

# Subtract five days from the current date
def subtract_five_days():
    current_date = datetime.now()
    return current_date - timedelta(days=5)

# Print yesterday, today, and tomorrow
def get_dates():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday, today, tomorrow

# Drop microseconds from datetime
def drop_microseconds():
    return datetime.now().replace(microsecond=0)

# Calculate difference between two dates in seconds
def date_difference_in_seconds(date1, date2):
    return abs((date2 - date1).total_seconds())

