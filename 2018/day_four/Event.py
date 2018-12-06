import re
from enum import Enum
from datetime import datetime

class Event:
    def __init__(self, raw_input):
        self.raw_input = raw_input
        self.time = datetime.strptime(raw_input[1:17], '%Y-%m-%d %H:%M')
        if 'wakes up' in raw_input:
            self.event_type = EventType.wake
        elif 'falls asleep' in raw_input:
            self.event_type = EventType.sleep
        else:
            self.guard_id = raw_input.split(' ')[3][1:]
            self.event_type = EventType.start


class EventType(Enum):
    wake = 1
    sleep = 2
    start = 3