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

time1= Time(17,80, 42)
print(time1)