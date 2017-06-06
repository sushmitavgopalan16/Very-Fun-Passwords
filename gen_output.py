# This file collects output files from Google Storage and then copies them to
# Google Compute Engine and then contatenates them.
import os

cat_prefix = ''

for i in range(12):
        filename_prefix = 'part-0000' if (i < 10) else 'part-000'
        filename = filename_prefix + str(i)

        cat_prefix += (filename + ' ')
        os.system('gsutil cp gs://very_fun_passwords_output/password_june5_1/' + filename + ' ' + filename)

os.system('cat ' + cat_prefix + ' > password_mr_june5.txt')
