# Very-Fun-Passwords

Looking for trends and insights from `berzerk0`'s [repository of leaked passwords](https://github.com/berzerk0/Probable-Wordlists).

### Useful Commands

#### Connecting to Google Cloud
* Make a VM instance
* Take note of external IP address and run this:
  * `ssh -i ~/.ssh/mapreduce username@ExTERNAL-IP`
  * `sudo mkdir /mnt/storage`
  * `sudo mount /dev/sdb /mnt/storage`
  * `sudo chmod 777 /mnt/storage`
  * `cd /mnt/storage`
  * `sudo apt-get install python3-pip`
  * `sudo apt-get install git`

#### Creating pairs of passwords on Compute Engine
Within the VM instance, you will create all possible pairs of the passwords found in your data set, by running the following command, with the appropriate name and location of your data and the final number indicating the number of desired threads:
```
python3 all_possible_pairs_threading.py ./../megatools-1.9.98/Top95Thousand-probable.txt 4
```
The output of this file should then be moved into Google Store using:
```
gsutil cp password_pairs.txt gs://very_fun_passwords_input/password_pairs.txt
```
#### Running MRJob on Dataproc

##### Getting substrings and classifications

The following command will run the MRJob on Google cloud dataproc:

```
python3 mr_substring.py -r dataproc --no-output --output-dir=gs://very_fun_passwords_output/output_substring --conf-path=./mrjob.conf gs://very_fun_passwords_input/all_password_pairs.txt
```
Make sure to alter the output directory each time you run.

In order to combine the outputs of the MRJob script, edit `gen_output.py` to reflect where the files are kept and run `gen_output.py` within the VM instance. You can then move the combined output file to google storage using the following command, with the appropriate names:

```
gsutil cp combined_output_file.txt gs://very_fun_passwords_input/first_mr_output.txt
```
##### Finding password patterns

This output from the first MRJob (`mr_substring.py`) should be fed into the second MRJob, (`passwords/mr_password.py`), using the following command, with the appropriate names:

```
python3 mr_password.py -r dataproc --no-output --output-dir=gs://very_fun_passwords_output/password_output --conf-path=./mrjob.conf gs://very_fun_passwords_input/first_mr_output.txt
```

This output can again be combined using the same `gen_output.py` and `gsutil cp` steps as found above. The copied file can then be directly accessed from your Google Storage GUI.

##### Counting the patterns found

The output from the above step can be processed through the following script in order to give a count of the total number of passwords that subscribe to each pattern:

```
python3 mr_get_pattern.py -r dataproc --no-output --output-dir=gs://very_fun_passwords_final/patterns --conf-path=./mrjob.conf gs://very_fun_passwords_input/mr_password_output.txt
```

##### Getting interesting stats

The output from created in the 'Finding password patterns' step can be fed directly into any of the scripts found in the `stats/` folder. These scripts will calculate distributions such as number of passwords of each length, counts of how many of each type of subsequences were found in all passwords present in the data set, and the most common female names/male names/words/single numbers used in passwords.

The following is an example command that can be run using `mr_simplecounts` within the `stats/` folder:

```
python3 mr_simplecounts.py -r dataproc --no-output --output-dir=gs://very_fun_passwords_final/simplecounts --conf-path=./mrjob.conf gs://very_fun_passwords_input/mr_password_output.txt
```
