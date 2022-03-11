def add_time(start, duration):

    clock, am_or_pm = start.split()

    hour, minutes = clock.split(":")

    passed_h, passed_m = duration.split(":")

    total_minute = int(minutes) + int(passed_m)

    hour_from_minute = total_minute // 60

    new_minute = total_minute % 60

    new_hour = int(hour) + int(passed_h) + hour_from_minute

    if new_minute < 10:

        new_minute = "0" + str(new_minute)

    if am_or_pm == "AM":

        if new_hour > 12:

            new_hour = new_hour - 12

            new_time = f"{new_hour}:{new_minute} PM"

        elif new_hour == 12:

            new_time = f"{new_hour}:{new_minute} PM"

        else:

            new_time = f"{new_hour}:{new_minute} AM"

    elif am_or_pm == "PM":

        if new_hour > 12:

            new_hour = new_hour - 12

            new_time = f"{new_hour}:{new_minute} AM"

        elif new_hour == 12:

            new_time = f"{new_hour}:{new_minute} AM"

        else:

            new_time = f"{new_hour}:{new_minute} PM"

    return new_time


print(add_time("11:06 PM", "2:02"))

print(add_time("11:43 AM", "00:20"))

print(add_time("10:10 PM", "3:30"))

print(add_time("3:00 PM", "3:10"))

