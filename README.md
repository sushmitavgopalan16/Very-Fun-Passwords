# Very-Fun-Passwords

Looking for trends and insights from `berzerk0`'s [repository of leaked passwords](https://github.com/berzerk0/Probable-Wordlists).

### Useful Commands

#### Finding substrings between all possible pairs of passwords
* To create password_pairs.txt, which contains all possible pairs of passwords:
  * `python3 all_possible_pairs.py [file.txt]`
* To run the MapReduce file with the created file:
  * `python3 mr_substring.py --jobconf mapreduce.job.reduces=1 password_pairs.txt`

#### Connecting to Google Cloud
* Sushmita logs in and makes VM instance
  * We take note of external IP address and run this:
    * ssh -i ~/.ssh/google-cloud-cs123 sushmitavgopalan@ExTERNAL-IP
    * sudo mkdir /mnt/storage
    * sudo mount /dev/sdb /mnt/storage
    * sudo chmod 777 /mnt/storage
    * cd /mnt/storage
    * sudo apt-get install python3-pip
