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
					  invalid_file: str = "invalid"):
	"""""
	This function checks the validity of a given csv file. The keyword arguments are essentially switches
	that users can "turn on" by providing. If they are provided, the result will match the attributes provided, e.g. 
	like count above a certain number, or only public videos.
	One caveat is that they must match the type which is provided in the above function header.

	notes- discuss dictwriter performance, 'extrasaction'=ignore argument, python, opportunities for further dev
	"""
	# Write header to csv file
	with open(filename, 'r') as f:
		reader = csv.DictReader(f)
		valid = []
		invalid = []
		result = None
		for row in reader:
			if privacy is not None:
				result = row['privacy'] == 'anybody'
			if like_count is not None:
				result = result and int(row['total_likes']) > like_count
			if play_count is not None:
				result = result and int(row['total_plays']) > play_count
			if title_length is not None:
				result = result and len(re.findall(r"[^\s]", row['title'])) < title_length
			if comment_count is not None:
				result = result and row['total_comments'] > comment_count
	# put in to valid and invalid lists based on matching filters
			if result:
				valid.append(row)
			else:
				invalid.append(row)
		write_to_output(valid_file, valid, ['id','title','privacy','total_plays','total_comments','total_likes'])
		write_to_output(invalid_file, invalid, ['id','title','privacy','total_plays','total_comments','total_likes'])

def main():
	check_validity('clips.csv', privacy='anybody', like_count=20, play_count=200, title_length=30)
if __name__ == '__main__':
	main()






