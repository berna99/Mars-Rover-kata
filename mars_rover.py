class MarsRover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.directions = ['N', 'E', 'S', 'W']
        self.grid_size = 10

    def Execute(self, command):
        for cmd in command:
            if cmd == 'L':
                self._turn_left()
            elif cmd == 'R':
                self._turn_right()
            elif cmd == 'M':
                self._move()
        return f"{self.x}:{self.y}:{self.direction}"

    def _turn_left(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index - 1) % 4]

    def _turn_right(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index + 1) % 4]

    def _move(self):
        if self.direction == 'N':
            self.y = (self.y + 1) % self.grid_size
        elif self.direction == 'E':
            self.x = (self.x + 1) % self.grid_size
        elif self.direction == 'S':
            self.y = (self.y - 1 + self.grid_size) % self.grid_size
        elif self.direction == 'W':
            self.x = (self.x - 1 + self.grid_size) % self.grid_size


