import unittest

import getbest


class TestExclude(unittest.TestCase):

    def test_Col(self):
	headings = "Course,Student Number,Mark"
        num_col,mark_col = getbest.getCols(headings)
        self.assertEqual(num_col,2)

    def test_Row(self):
	headings = "Course,Student Number,Mark"
        num_col,mark_col = getbest.getCols(headings)
        self.assertIs(mark_col,3)

    def test_Top(self):
	num_col = 2;
	mark_col = 3;
	marks = "72,71,90"
	top_ind, top_Mark = getbest.findTop(marks,num_col,mark_col)
        self.assertEqual(top_Mark,90)

    def test_Idx(self):
	num_col = 2;
	mark_col = 3;
	marks = "72,71,90"
	top_ind, top_Mark = getbest.findTop(marks,num_col,mark_col)
        self.assertEqual(top_ind,1)

if __name__ == '__main__':


unittest.main()
