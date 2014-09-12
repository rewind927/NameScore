import unittest
from NameScore import *

class NameScoreTestCase(unittest.TestCase):
    def test_name_score1(self):
        self.assertEquals(countNameScoreUsingListComprehension(["ABC","CDEF","FIJK"]),150)
    def test_name_score2(self):
        self.assertEquals(countNameScoreUsingListComprehension(["ABC","ABCDEFG","CDEF","FIJK"]),260)

if __name__ == '__main__':
    unittest.main()
