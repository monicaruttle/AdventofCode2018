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

day_one_part_two()    
