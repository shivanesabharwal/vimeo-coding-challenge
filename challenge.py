import csv
import regex as re
def read_csv(filename):
	# needs docs
	with open(filename, 'r') as f:
		d = csv.DictReader(f)
	return d

def write_to_output(filename, objs):
 	with open(filename + ".csv") as f:
 			d = csv.DictWriter(f)
 			d.writeheader()
 		 	for o in objs:
 				d.writerow(o)


def check_validity(d, public: bool = None, 
					  like_count: int = None, 
					  play_count: int = None, 
					  title_length: int = None
					  valid_file: str = "valid",
					  invalid_file: str = "invalid"):
	"""""
	This function checks the validity of a csv.DictReader object. The keyword arguments are essentially switches
	that users can "turn on" by providing. If they are provided, the result will match the attributes provided, e.g. 
	like count above a certain number, or only public videos.
	One caveat is that they must match the type which is provided in the above function header.

	notes- discuss dictwriter performance, 'extrasaction'=ignore argument, python, opportunities for further dev
	"""
	# Write header to csv file
	valid = []
	invalid = []
	result = None
	for row in d:
		if public is not None:
		 result = row['public'] == True:
		if like_count is not None:
			result = result and row['like_count'] > like_count
		if play_count is not None:
 			result = result and row ['play_count'] > play_count
 		if title_length is not None:
 			result = result and str(row['title_length']).count(r'[^\S]') > title_length
 		# put in to valid and invalid lists based on matching filters
 		if result:
 			valid.append(row)
 		else:
 			invalid.append(row)
 	write_to_output(d, valid_file, valid)
 	write_to_output(d, invalid_file, invalid)

if __name__ == '__main__':
	main()
 
def main():
	






