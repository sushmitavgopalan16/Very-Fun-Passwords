# Very-Fun-Passwords

Looking for trends and insights from `berzerk0`'s [repository of leaked passwords](https://github.com/berzerk0/Probable-Wordlists).

### Useful Commands

#### Connecting to Google Cloud
* Sushmita logs in and makes VM instance
  * make sure there is no squiggly line next to the vm instance
* We take note of external IP address and run this:
  * `ssh -i ~/.ssh/mapreduce sushmitavgopalan@ExTERNAL-IP`
  * `sudo mkdir /mnt/storage`
  * `sudo mount /dev/sdb /mnt/storage`
  * `sudo chmod 777 /mnt/storage`
  * `cd /mnt/storage`
  * `sudo apt-get install python3-pip`
  * `sudo apt-get install git`

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

##### Getting interesting stats

The output from created in the above step can be fed directly into any of the scripts found in the `stats/` folder. These scripts will calculate distributions such as number of passwords of each length, counts of how many of each type of subsequences were found in all passwords present in the data set, and the most common female names/male names/words/single numbers used in passwords.

The following is an example command that can be run using `mr_simplecounts` within the `stats/` folder:

```
python3 mr_simplecounts.py -r dataproc --no-output --output-dir=gs://very_fun_passwords_final/simplecounts --conf-path=./mrjob.conf gs://very_fun_passwords_input/mr_password_output.txt
```
