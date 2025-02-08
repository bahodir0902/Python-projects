import time
from playsound import playsound
import os

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


class Alarm:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    def sound(self, seconds):
        #print(CLEAR)
        time_left = self.seconds
        while time_left > 0:
            time.sleep(1)
            time_left -= 1
            self.minutes = (time_left % 3600) // 60
            self.hours = time_left // 3600
            self.seconds_left = time_left % 60
            
            print(f"\rAlarm will sound in:  {self.hours:02d} : {self.minutes:02d} : {self.seconds_left:02d} seconds", end="")
        playsound("alarm_audio.mp3")       

    def get_input(self):
        while True:
            try:
                self.hours = int(input("How many hours to set an alarm?: "))
                self.minutes = int(input("How many mintues to set an alarm?: "))  
                self.seconds = int(input("How many seconds to set an alarm?: "))    
                if(self.hours < 0 or self.minutes < 0 or self.seconds < 0):
                    print("Time must be non-negative.")
                    raise ValueError
                    
                total_time = self.hours * 3600 + self.minutes * 60 + self.seconds 
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
        
        return total_time


clock = Alarm()

user_input = clock.get_input()
clock.sound(user_input)



os.system("pause")       