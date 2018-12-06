def day_two_part_one():
    with open('DayTwo.txt') as ids_file:
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
    with open('DayTwo.txt') as ids_file:
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

if __name__ == "__main__":
    day_two_part_two()