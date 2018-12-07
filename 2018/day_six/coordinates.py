import sys
import operator
from Coordinate import Coordinate

def find_max_coordinate_size():
    with open('DaySix.txt') as coordinate_file:
        input_coordinates = coordinate_file.readlines()

    coordinates = {}
    for input_coordinate in input_coordinates:
        coordinates[Coordinate(input_coordinate)] = 0

    has_a_tie = False
    for x in range(40, 354):
        for y in range(55, 358):
            # find closest coordinate
            min_distance = sys.maxsize
            for coordinate in coordinates:
                distance = abs(x - coordinate.x) + abs(y - coordinate.y)
                if distance == min_distance:
                    has_a_tie = True
                elif distance < min_distance:
                    min_distance = distance
                    min_coordinate = coordinate
                    has_a_tie = False
            if not has_a_tie:
                # print ('Coordinate x: {}, y: {} is closest to x: {}, y: {}'.format(x, y, min_coordinate.x, min_coordinate.y))
                coordinates[min_coordinate] += 1
    
    sorted_x = sorted(coordinates.items(), key=operator.itemgetter(1))

    # this is a hack. I figured the max one was to go to infinity, so I printed all of them out and the correct one was the second one.
    for key, value in sorted_x:
        print(value)

def find_total_distance_region():
    with open('DaySix.txt') as coordinate_file:
        input_coordinates = coordinate_file.readlines()

    coordinates = []
    for input_coordinate in input_coordinates:
        coordinates.append(Coordinate(input_coordinate))
    
    in_region = 0
    for x in range(40, 354):
        for y in range(55, 358):
            distance = 0
            for coordinate in coordinates:
                distance += abs(x - coordinate.x) + abs(y - coordinate.y)
            if distance < 10000:
                in_region += 1
    print(in_region)


if __name__ == "__main__":
    find_total_distance_region()