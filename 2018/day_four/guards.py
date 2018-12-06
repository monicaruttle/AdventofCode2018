from Event import Event
from Event import EventType

def find_best_guard():
    events = generate_sorted_event_list()

    guard_sleeps = {}
    current_guard_id = 0
    sleep_time = 0
    for event in events:
        if event.event_type == EventType.start:
            current_guard_id = event.guard_id
        elif event.event_type == EventType.sleep:
            sleep_time = event.time.minute
            event.guard_id = current_guard_id
        elif event.event_type == EventType.wake:
            guard_sleeps[current_guard_id] = guard_sleeps.get(current_guard_id, 0) + event.time.minute - sleep_time
            event.guard_id = current_guard_id
    
    max_guard_id = max(guard_sleeps, key=guard_sleeps.get)

    minutes = {}
    for event in events:
        if event.guard_id != max_guard_id or event.event_type == EventType.start:
            continue
        elif event.event_type == EventType.sleep:
            sleep_time = event.time.minute
        elif event.event_type == EventType.wake:
            for i in range(sleep_time, event.time.minute):
                minutes[i] = minutes.get(i, 0) + 1

    most_likely_minutes = max(minutes, key=minutes.get)
    print(int(max_guard_id) * most_likely_minutes)

def generate_sorted_event_list():
    with open('DayFour.txt') as event_file:
        raw_events = event_file.readlines()

    events = []
    for event in raw_events:
        events.append(Event(event))

    events.sort(key=lambda x: x.time, reverse=False)
    return events

def find_most_frequent_asleep_guard():
    events = generate_sorted_event_list()
    for event in events:
        if event.event_type == EventType.start:
            current_guard_id = event.guard_id

        event.guard_id = current_guard_id
    
    guard_ids = set([event.guard_id for event in events])
    most_common_minute_overall = 0
    most_common_minute_value_overall = 0
    most_common_guard_id = 0
    for guard_id in guard_ids:
        minutes = {}
        for event in events:
            if event.guard_id != guard_id or event.event_type == EventType.start:
                continue
            elif event.event_type == EventType.sleep:
                sleep_time = event.time.minute
            elif event.event_type == EventType.wake:
                for i in range(sleep_time, event.time.minute):
                    minutes[i] = minutes.get(i, 0) + 1
        if minutes == {}:
            continue
        most_common_minute = max(minutes, key=minutes.get)
        most_common_minute_value = minutes[most_common_minute]
        if most_common_minute_value > most_common_minute_value_overall:
            most_common_minute_overall = most_common_minute
            most_common_minute_value_overall = most_common_minute_value
            most_common_guard_id = guard_id
        print('guard ID: {}, minute: {}, number of times: {}'.format(guard_id, most_common_minute, most_common_minute_value))

    print(int(most_common_guard_id) * most_common_minute_overall)


if __name__ == "__main__":
    find_most_frequent_asleep_guard()