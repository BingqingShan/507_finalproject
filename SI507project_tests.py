from SI507project_tools import *
import unittest
import sqlite3

class PartOne(unittest.TestCase):
    def setUp(self):
        self.file = open('data.csv','r')
        self.contents = self.file.readlines()
        self.file.close()
    def test_data_amount(self):
        self.assertTrue(len(self.contents) >= 60, "Testing that there are at least 60 lines in data csv file")


class PartTow(unittest.TestCase):
	def setUp(self):
		self.conn = sqlite3.connect("data.db") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_for_uniquess_1(self):
		res = self.cur.execute("select * from stages")
		data = res.fetchall()
		self.assertTrue(len(data)==5, 'Testing that you have 5 stages in the stages table')

	def test_for_uniquess_2(self):
		res = self.cur.execute("select * from purposes")
		data = res.fetchall()
		self.assertTrue(len(data)==2, 'Testing that you have 2 purposes in the purposes table')

	def tearDown(self):
		self.conn.commit()
		self.conn.close()

class PartThree(unittest.TestCase):
	def setUp(self):
		self.conn = sqlite3.connect("data.db") # Connecting to database that should exist in autograder
		self.cur = self.conn.cursor()

	def test_foreign_key_approach_1(self):
		res = self.cur.execute("select * from approaches INNER JOIN purposes ON approaches.purpose_id = purposes.id")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between approaches and purposes does work")

	def test_foreign_key_approach_2(self):
		res = self.cur.execute("select * from approaches INNER JOIN stages ON approaches.stage_id = stages.id")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between approaches and stages does work")

	def tearDown(self):
		self.conn.commit()
		self.conn.close()

if __name__ == '__main__':
    unittest.main()
