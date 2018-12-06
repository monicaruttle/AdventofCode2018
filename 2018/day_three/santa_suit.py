def day_three_part_one():
    with open('DayThree.txt') as claims_file:
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
    with open('DayThree.txt') as claims_file:
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

if __name__ == "__main__":
    day_three_part_two()