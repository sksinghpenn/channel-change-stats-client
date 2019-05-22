from random import randrange
from datetime import timedelta

import time;
import datetime;

class localTZ(datetime.tzinfo):
    def utcoffset(self, dt): return datetime.timedelta(seconds=-time.timezone);

now = datetime.datetime.now().replace(microsecond=0,tzinfo=localTZ());
        

def get_random_start_date_time():
    # This function will return a random datetime between two datetime  objects.  
   
    number_of_seconds_in_date = 24*60*60 # any time in 24 hours 
    
    random_second_to_add_in_start = randrange(number_of_seconds_in_date)
    now = datetime.datetime.now().replace(microsecond=0,tzinfo=localTZ());
    
    random_start_time = now + timedelta(seconds=random_second_to_add_in_start)
 
    return random_start_time
        


def get_random_end_date_time(random_start_time):
    number_of_seconds_in_hour = 60*60           
    random_second_to_add_in_end = randrange(number_of_seconds_in_hour)
    random_end_time = random_start_time + timedelta(seconds=random_second_to_add_in_end)
    return random_end_time   


