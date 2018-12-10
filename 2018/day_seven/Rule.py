class Rule:
    def __init__(self, instructions):
        instruction_parts = instructions.split(' ')
        self.first = instruction_parts[1]
        self.second = instruction_parts[7]