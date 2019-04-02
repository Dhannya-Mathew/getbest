import unittest
import os
import getbest


this_dir = os.path.dirname(__file__)

class TestExclude(unittest.TestCase):

    def test_Col(self):
	test_data1,test_data2 = getbest.getCols(os.path.join(this_dir,"bestdat0.csv"))
        self.assertEqual(test_data1,2)

    def test_Row(self):
	test_data1,test_data2 = getbest.getCols(os.path.join(this_dir,"bestdat0.csv"))
        self.assertIs(test_data2,3)

    def test_Top(self):
	num_col = 2;
	mark_col = 3;
	test_data1,test_data2 = getbest.findTop()
	top, best = getbest.findTop(os.path.join(this_dir,"bestdat0.csv"),num_col,mark_col)
        self.assertEqual(test_data2,90)

    def test_Top(self):
	num_col = 2;
	mark_col = 3;
	test_data1,test_data2 = getbest.findTop()
	top, best = getbest.findTop(os.path.join(this_dir,"bestdat0.csv"),num_col,mark_col)
        self.assertEqual(test_data1,1)

if __name__ == '__main__':


unittest.main()
