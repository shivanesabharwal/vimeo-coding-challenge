import unittest
import challenge
import csv
class TestAll(unittest.TestCase):
	def setUp(self, filename='test.csv'):
		self.filename = filename
	
	def testValidity(self):
		challenge.check_validity(self.filename, 
					  privacy='anybody', 
					  like_count=10, 
					  play_count=200, 
					  title_length=30,
					  valid_file="valid",
					  invalid_file="invalid",
					  output_cols=['id', 'title'])
		with open('valid.csv', 'r') as f1, open('test_valid.csv', 'r') as f2:
			for (line_f1, line_f2) in zip(f1, f2):
				self.assertEqual(line_f1, line_f2)
		with open('invalid.csv', 'r') as f1, open('test_invalid.csv', 'r') as f2:
			for (line_f1, line_f2) in zip(f1, f2):
				self.assertEqual(line_f1, line_f2)

        		



# Run all tests
if __name__ == '__main__':
    unittest.main()

			