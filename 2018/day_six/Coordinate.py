class Coordinate:

    def __init__(self, raw_coordinate: str):
        coordinate = raw_coordinate.split(', ')
        self.x = int(coordinate[0])
        self.y = int(coordinate[1])