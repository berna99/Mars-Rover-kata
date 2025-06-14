import unittest
from mars_rover import MarsRover

class TestMarsRover(unittest.TestCase):

    def test_initial_position(self):
        rover = MarsRover()
        self.assertEqual(rover.Execute(""), "0:0:N")

    def test_rotate_right(self):
        rover = MarsRover()
        self.assertEqual(rover.Execute("R"), "0:0:E")
        rover = MarsRover()
        self.assertEqual(rover.Execute("RR"), "0:0:S")
        rover = MarsRover()
        self.assertEqual(rover.Execute("RRR"), "0:0:W")
        rover = MarsRover()
        self.assertEqual(rover.Execute("RRRR"), "0:0:N")

    def test_rotate_left(self):
        rover = MarsRover()
        self.assertEqual(rover.Execute("L"), "0:0:W")
        rover = MarsRover()
        self.assertEqual(rover.Execute("LL"), "0:0:S")
        rover = MarsRover()
        self.assertEqual(rover.Execute("LLL"), "0:0:E")
        rover = MarsRover()
        self.assertEqual(rover.Execute("LLLL"), "0:0:N")

    def test_move_north(self):
        rover = MarsRover()
        self.assertEqual(rover.Execute("M"), "0:1:N")
        rover = MarsRover()
        self.assertEqual(rover.Execute("MM"), "0:2:N")

    def test_move_east(self):
        rover = MarsRover()
        rover.Execute("R")
        self.assertEqual(rover.Execute("M"), "1:0:E")

    def test_move_south(self):
        rover = MarsRover()
        rover.Execute("RR")
        self.assertEqual(rover.Execute("M"), "0:9:S") 

    def test_move_west(self):
        rover = MarsRover()
        rover.Execute("L")
        self.assertEqual(rover.Execute("M"), "9:0:W") 

    def test_example_one(self):
        rover = MarsRover()
        self.assertEqual(rover.Execute("MMRMMLM"), "2:3:N")

    def test_example_two_wrap_around(self):
        rover = MarsRover()
        self.assertEqual(rover.Execute("MMMMMMMMMM"), "0:0:N")

    def test_complex_movement(self):
        rover = MarsRover()
        self.assertEqual(rover.Execute("RMMLMMLM"), "1:2:W")

if __name__ == '__main__':
    unittest.main()


