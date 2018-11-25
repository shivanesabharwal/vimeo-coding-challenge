import csv
import re
def write_to_output(filename, objs, fieldnames):
	with open(filename + ".csv", 'w') as f:
		d = csv.DictWriter(f, fieldnames=fieldnames)
		d.writeheader()
		for o in objs:
			d.writerow(o)


def check_validity(filename,
					  privacy: str = None, 
					  like_count: int = None, 
					  play_count: int = None, 
					  title_length: int = None,
					  comment_count: int = None,
					  valid_file: str = "valid",
					  invalid_file: str = "invalid",
					  output_cols: list = ['id']):
	"""""
	This function checks the validity of a given csv file. The keyword arguments are essentially switches
	that users can "turn on" by providing. If they are provided, the result will match the attributes provided, e.g. 
	like count above a certain number, or only public videos.
	One caveat is that they must match the type which is provided in the above function header. This makes the code
	more resilient to user mistakes, given python does not check for type errors at compile time.
	"""
	# open csv file for analysis	
	with open(filename, 'r') as f:
		reader = csv.DictReader(f)
		valid = []
		invalid = []
		result = True
		# check conditions
		for row in reader:
			if privacy is not None:
				result = row['privacy'] == 'anybody'
			if like_count is not None:
				result = result and int(row['total_likes']) > like_count
			if play_count is not None:
				result = result and (int(row['total_plays']) > play_count)
			if title_length is not None:
				# counts all non whitespace characters
				result = result and len(re.findall(r"[^\s]", row['title'])) < title_length
			if comment_count is not None:
				result = result and row['total_comments'] > comment_count
			# put in to valid and invalid lists based on matching filters
			tmp = {}
			if result:
				for i in output_cols:
					tmp[i] = row[i]
				valid.append(tmp)
			else:
				for i in output_cols:
					tmp[i] = row[i]
				invalid.append(tmp)
		# write to appropriate valid and invalid files
		write_to_output(valid_file, valid, output_cols)
		write_to_output(invalid_file, invalid, output_cols)

def main():
	check_validity('clips.csv', privacy='anybody', like_count=10, play_count=200, title_length=30)
if __name__ == '__main__':
	main()






