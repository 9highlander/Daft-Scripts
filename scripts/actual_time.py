import datetime

def actual_time():
    dt = datetime.datetime.now()
    dt2 = dt.timetuple()
    return dt2