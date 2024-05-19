
import pandas as pd
import os
import time

# record start time
start = time.time()

# Read csv
df_app = pd.read_csv('Google-Playstore.csv', usecols = ['App Name', 'Category', 'Rating', 'Installs', 'Free', 'Developer Id', 'Released', 'Last Updated'])
df_app.head(5)

# record end time
end = time.time()

# Execution Time
print("The time of execution of above program is: ",(end-start) * 10**3, "ms")
