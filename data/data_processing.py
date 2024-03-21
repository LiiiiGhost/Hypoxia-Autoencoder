import pandas as pd
   
df = pd.read_csv('new_rnaseq_s1_s2.csv') 

filtered_df = df[['file_id', 'case_id']]

filtered_df.to_csv('new_file_to_case.tsv', sep='\t', index=False)