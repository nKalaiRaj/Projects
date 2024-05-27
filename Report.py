#Python Program 
import pandas as pd
# Data Frame df is created using read-csv in pandas
df = pd.read_csv('balance.txt', delim_whitespace=True)
print(df)
#Average income based on Ethnicity
print("Average income based on Ethnicity : \n ", df.groupby('Ethnicity')['Income'].mean())
# On Average Married or Single have higher balance
print("On Average Married or Single have higher balance  :\n ", df.groupby('Married')['Balance'].mean())
# Getting the highest Income in our dataset
print("Highest Income in our dataset :\t", df['Income'].max())
# Getting the Lowest Income in our dataset
print("Lowest Income in our dataset :\t", df['Income'].min())
# Total number of cards in our dataset
print("Total number of Cards in our dataset :\t",df['Cards'].sum())
#Female Vs Male Information
print("Female Vs Male Information : ",df['Gender'].value_counts())