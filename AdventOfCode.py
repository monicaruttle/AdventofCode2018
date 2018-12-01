def day_one_part_one():
    with open('Samples/DayOne.txt') as frequency_file:
        frequencies = frequency_file.readlines()

    frequencies = [frequency.strip() for frequency in frequencies]

    total = 0
    for frequency in frequencies:
            if frequency[0] == '-':
                total -= int(frequency[1:])
            else:
                total += int(frequency[1:])
    
    print(total)


def day_one_part_two():
    with open('Samples/DayOne.txt') as frequency_file:
        frequencies = frequency_file.readlines()

    frequencies = [frequency.strip() for frequency in frequencies]

    total = 0
    history = []
    history.append(total)
    while (True):
        for frequency in frequencies:
            if frequency[0] == '-':
                total -= int(frequency[1:])
            else:
                total += int(frequency[1:])
            
            if total in history:
                print(total)
                exit()

            history.append(total)
    