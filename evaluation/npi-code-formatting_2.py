import csv
import re
# Current evaluation values
mean_avg_prec = 0.0;avg_reca = 0.0;avg_mrr = 0.0;
# Possible evaluation values in the future
avg_accuracy = 0.0;avg_sensitivity = 0.0;

local_file = []; print('Enter csv file name: '); file_name = input();

with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    # Check if file is empty or not
    row_count = 0;
    for rows in csvreader:
        row_count += 1; local_file.append(rows);
    print('Row count:\t', row_count)
    # Case if file is empty    
    if row_count == 0:
        print('====Evaluation Result====');print('Mean Avg. Prec.:\t', mean_avg_prec);print('Avg. Recall: \t', avg_reca);print('Avg. MMR: \t', avg_mrr)