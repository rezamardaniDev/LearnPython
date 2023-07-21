import os
os.system("cls")

class Time:
    def __init__(self, hours, minutes, seconds) -> None:
        if hours >= 24:
            raise ValueError("hours should be less than 23")
        if minutes >= 60:
            raise ValueError("minutes should be less than 23")
        if seconds >= 60:
            raise ValueError("seconds should be less than 23")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    
    def __add__(self, other):
        hours = self.hours + other.hours
        minutes = self.minutes + other.minutes
        seconds = self.seconds + other.seconds
        return Time(hours%24, minutes%60, seconds%60)
    
    def __gt__(self, other):
        return (self.hours > other.hours) \
        or (self.hours == other.hours and self.minutes > other.minutes) \
        or (self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds)
    
    def __eq__(self,other) -> bool:
        return (id(self) != id(other) and (self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds))

time1= Time(1,1, 10)
time2= Time(1,1, 1)
print(time1 == time2)