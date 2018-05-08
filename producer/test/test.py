import unittest, sys, os
sys.path.append(os.path.abspath("./src"))
from arrayPartition1 import Solution

class TestArrayPartition1(unittest.TestCase):
    def setUp(self):
        self.sln = Solution()

    def test_basic(self):
        self.assertEqual(self.sln.ArrayPairSum([1,6,2,3]), 6)
    #add two more	

if __name__ == '__main__':
 #    unittest.main()
     import xmlrunner
     unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
