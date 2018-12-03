def day_one_part_one():
    with open('Samples/DayOne.txt') as frequency_file:
        frequencies = frequency_file.readlines()

    total = 0
    for frequency in frequencies:
            total += int(frequency)
    
    print(total)


def day_one_part_two():
    with open('Samples/DayOne.txt') as frequency_file:
        frequencies = frequency_file.readlines()

    total = 0
    history = []
    history.append(total)
    while (True):
        for frequency in frequencies:
            total += int(frequency)
            
            if total in history:
                print(total)
                exit()

            history.append(total)


def day_two_part_one():
    with open('Samples/DayTwo.txt') as ids_file:
        ids = ids_file.readlines()

    total_two = 0
    total_three = 0

    for id in ids:
        char_count = {}
        for char in id:
            if char in char_count:
                occurences = char_count[char]
                occurences += 1
                char_count[char] = occurences
            else:
                char_count[char] = 1
        if 2 in char_count.values():
            total_two += 1
        if 3 in char_count.values():
            total_three += 1
    
    print(total_three * total_two)


def day_two_part_two():
    with open('Samples/DayTwo.txt') as ids_file:
        ids = ids_file.readlines()
    
    for id_anchor in ids:
        for id_current in ids:
            if id_current == id_anchor:
                continue
            
            number_of_differences = 0
            char_idx = 0
            while char_idx < len(id_current):
                if id_anchor[char_idx] != id_current[char_idx]:
                    number_of_differences += 1
                char_idx += 1
            if number_of_differences == 1:
                print ('Anchor: {}, Current: {}'.format(id_anchor, id_current))

day_two_part_two()
