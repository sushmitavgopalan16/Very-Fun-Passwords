# Very-Fun-Passwords

Looking for trends and insights from `berzerk0`'s [repository of leaked passwords](https://github.com/berzerk0/Probable-Wordlists).

### Useful Commands

#### Finding substrings between all possible pairs of passwords
* To create password_pairs.txt, which contains all possible pairs of passwords:
  * `python3 all_possible_pairs.py [file.txt]`
* To run the MapReduce file with the created file:
  * `python3 distance_between_pairs.py --jobconf mapreduce.job.reduces=1 password_pairs.txt`
