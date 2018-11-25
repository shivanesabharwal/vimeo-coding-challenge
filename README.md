# vimeo-coding-challenge
This is Shivane Sabharwal's submission to Vimeo's Live Platform Engineering coding challenge.

The code for checking validity of clips.csv is contained in challenge.py. It contains one main function: `check_validity`. It takes a csv file and loads it into a csv.DictReader object. This allows for a quick way to iterate through every row of the csv file and index it into it using column names in the csv file. This function classifies each row in the csv file as "valid" or "invalid" given the particular arguments provided (the parameters from the coding challenge are used if we run `python challenge.py`). It also contains a couple useful parameters such as the names for the output csv files as well as the columns desired in the output csv files.
Some design notes:
1. The function contains multiple keyword arguments that can be considered "switches" to turn on if the user would like to filter on a certain column. They default to None values otherwise. This allows a user to customize the filters they would like to a higher degree.
2. The DictReader objects are used for ease of indexing and more readable code. Although in this exercise, the output was simply a list of `clip_id`'s, it made sense to use the DictWriter anyway because it would allow the code to be easily extended to write other columns to the output file as well.
3. There is a `write_to_output` function also called by `check_validity`. This is a useful subroutine as it can be used in almost any use case. It accepts 3 arguments: a filename that the output file will be written to, a list of objs (rows of a csv), and fieldnames, which are the columns of the output csv file.
4. One tricky problem was looking at title length. I made the decision to only consider non-whitespace characters in the title, as I didn't think whitespace conveyed anything useful inherently, merely where to separate certain characters. In order to count the number of non whitespace characters, I used a regex that matched everything except those characters, and used the `re.findall` method.

There is also a test provided in `test_challenge.py`. I used the first 7 rows of `clips.csv` and handclassified them into `test_valid.csv` and `test_invalid.csv`. The test can be run by calling `python test_challenge.py`.

Final notes:
Currently, `check_validity` checks a certain type of inequality, e.g. less than, greater than, for each attribute. While I considered using pandas to write a more modular solution, I believe this code is still easy to extend for different inequalities based on user input, maybe from the command line.

Also, this code was written and tested using Python 3.5, so it may be a good idea to configure an environment like such in order to run the script if there are compatibility issues.

Happy Holidays!
