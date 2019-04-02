import unittest

import getbest


class TestExclude(unittest.TestCase):

    def test_Col(self):
	headings = "Course,Student Number,Mark"
        num_col = getbest.getCols(headings)
        self.assertEqual(num_col,2)

    def test_Row(self):
	headings = "Course,Student Number,Mark"
        mark_col = getbest.getCols(headings)
        self.assertIs(mark_col,3)

    def test_Top(self):
	num_col = 2;
	mark_col = 3;
	marks = "72,71,90"
	top, best = getbest.findTop(marks,num_col,mark_col)
        self.assertEqual(top,90)

if __name__ == '__main__':


unittest.main()
