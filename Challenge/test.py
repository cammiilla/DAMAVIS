import unittest

import main.challenge as challenge

class TestNumberOfAvailableDifferentPaths(unittest.TestCase):
    def test_number_of_available_different_paths(self):
        self.assertEqual(challenge.number_of_available_different_paths([4, 3],[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]],3),7)
        self.assertEqual(challenge.number_of_available_different_paths([2, 3],[[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]], 10) ,1)
        self.assertEqual(challenge.number_of_available_different_paths([10, 10],[[5,5], [5,4], [4,4], [4,5]],4),81)

if __name__ == '__main__':
    unittest.main()