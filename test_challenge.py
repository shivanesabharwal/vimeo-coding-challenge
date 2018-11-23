import unittest.TestCase
import challenge
import random.randint
class CheckValidityTest(TestCase):
	def setUp(self):
		# randomly generate input csv file like clips.csv
		with open("test.csv", 'w') as testFile:
			fieldnames = ['id', 'title', 'privacy', 'total_plays', 'total_comments', 'total_likes']
			self.randomClips = csv.DictWriter(testFile, fieldnames=fieldnames)
			self.randomClips.writeheader()
			for i in range(200):
				self.randomClips.writerow({'id': randint(150000, 300000),
										  'title': ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25)),
										  'privacy': random.choice([True, False]),
										  'total_plays': randint(0, 600),
										  'total_comments': randint(0, 50),
										  'total_likes': randint(0,50)})
	def test_read_csv(filename):
		challenge.read_csv(filename)
		self.rando



			