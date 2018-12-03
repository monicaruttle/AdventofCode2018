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


def day_three_part_one():
    with open('Samples/DayThree.txt') as claims_file:
        claims = claims_file.readlines()

    w, h = 1000, 1000
    grid = [[0 for x in range(w)] for y in range(h)]
    create_grid(claims, grid)
    
    count = 0
    x = 0
    y = 0
    while x < w:
        while y < h:
            if grid[x][y] > 1:
                count += 1
            y += 1
        x += 1
        y = 0
    
    print(count)

def day_three_part_two():
    with open('Samples/DayThree.txt') as claims_file:
        claims = claims_file.readlines()

    w, h = 1000, 1000
    grid = [[0 for x in range(w)] for y in range(h)]
    create_grid(claims, grid)
    
    for claim in claims:
        claim_split = claim.split(' ')
        claim_id = claim_split[0]
        dists_string = claim_split[2][:-1]
        dists = dists_string.split(',')
        dist_to_left = int(dists[0])
        dist_to_top = int(dists[1])

        size = claim_split[3].split('x')
        width = int(size[0])
        height = int(size[1])

        # iterate through pattern
        more_than_one = False
        x = dist_to_left
        while x < width + dist_to_left:
            y = dist_to_top
            while y < height + dist_to_top:
                if grid[x][y] > 1:
                    more_than_one = True
                y += 1
            x += 1
        
        if not more_than_one:
            print(claim_id)
            exit()

def create_grid(claims, grid):
    for claim in claims:
        claim_split = claim.split(' ')
        dists_string = claim_split[2][:-1]
        dists = dists_string.split(',')
        dist_to_left = int(dists[0])
        dist_to_top = int(dists[1])

        size = claim_split[3].split('x')
        width = int(size[0])
        height = int(size[1])

        # iterate through pattern
        x = dist_to_left
        while x < width + dist_to_left:
            y = dist_to_top
            while y < height + dist_to_top:
                grid[x][y] = grid[x][y] + 1
                y += 1
            x += 1

day_three_part_two()
