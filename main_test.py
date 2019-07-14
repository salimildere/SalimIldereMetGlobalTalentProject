import unittest
import main

class test (unittest.TestCase):

    def test_find_locations_list_assertEqual (self):
        checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
        self.assertEqual(main.find_locations_list(checkers), [[1, 1], [2, 1], [3, 1], [4, 6], [5, 10], [6, 10], [7, 12], [8, 13]])

    def test_find_combinition_stamp_assertIn(self):
        locations=[[1, 1], [2, 1], [3, 1], [4, 6], [5, 10], [6, 10], [7, 12], [8, 13]]
        dice1=5
        dice2=2
        self.assertIn([1, 6, 0],main.find_combinition_stamp(locations, dice1, dice2))

    def test_find_combinition_stamp_assertIsInstance(self):
        locations = [[1, 1], [2, 1], [3, 1], [4, 6], [5, 10], [6, 10], [7, 12], [8, 13]]
        dice1 = 5
        dice2 = 2
        self.assertIsInstance(main.find_combinition_stamp(locations, dice1, dice2), list)

if __name__=='__main__' :
    unittest.main()