
import duckdb
import os
import time

# record start time
start = time.time()

### Import CSV
duck_app = duckdb.read_csv("Google-Playstore.csv")
duck_app

# record end time
end = time.time()

# Execution Time
print("The time of execution of above program is: ",(end-start) * 10**3, "ms")