print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
def time_to_seconds(t):
    return t.hour * 3600 + t.minute * 60 + t.second
def seconds_to_time(seconds):
    hour, rem = divmod(int(seconds), 3600)
    minute, second = divmod(rem, 60)
    return Time(hour, minute, second)
def multiply_time(t, factor):
    return seconds_to_time(time_to_seconds(t) * factor)
def average_pace(finish_time, distance):
    return multiply_time(finish_time, 1 / distance)
finish = Time(1, 23, 45)
distance = 3.1
pace = average_pace(finish, distance)
print(f"Average pace per mile: {pace.hour:02d}:{pace.minute:02d}:{pace.second:02d}")

