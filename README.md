# Comparing-Pandas-Polars-and-Duckdb

# Description

In this project the idea is to compare Pandas, Polars and Duckdb as well as checking the most downloaded and popular app from google play store. 
As for this comparison I decide to choose a bigger dataset, so we can better evaluate the time difference of those 3 libraries 

The dataset Google-Playstore.csv has a size of 676 MB and was downloaded from Kaggle: https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps

# Libraries
Pandas 2.2.2

Polars 0.20.26

Duckdb 0.10.2

# Results
For the ingestion of the dataset to python both Polars and Duckdb are a superior option in time and optimization with duckdb being the best. While pandas took almost 17 seconds to read the dataset, polars took only half a second and duckdb even less with 0.16 seconds.

The Results are the following:

Pandas Exec

![pandas](https://github.com/RafaelMotta01/Comparing-Pandas-Polars-and-Duckdb/assets/167834271/7aa816a5-d472-44d3-8350-343af750e9c2)

Polars Exec

![polars](https://github.com/RafaelMotta01/Comparing-Pandas-Polars-and-Duckdb/assets/167834271/07f07676-a000-4848-9c9d-2e1c8e1b76aa)

Duckdb Exec

![duckdb](https://github.com/RafaelMotta01/Comparing-Pandas-Polars-and-Duckdb/assets/167834271/aca80a59-b2cf-43fc-81c2-c24e9a3ad4de)

# Conclusion
Not only Duckdb is a higher-speed option for heavy workloads but is also a better performance than the others. Also it has a built in sql query language for data analyses which can be by itself is a big help when dealing with large datasets and does not require other dependencies to download in python.

As for the apps listed on the dataset:
Since the variable "Installs" dont show especific numbers, only agreggations (ex: 5.000+, 10.000+), we won't be able to find an exactly most downloaded app. Also the only app with 10,000,000,000+ its the google play app itself we can disconsider it 
and use the second largest amount of downloads which is 5,000,000,000+. As result we have the following:

![Apps](https://github.com/RafaelMotta01/Comparing-Pandas-Polars-and-Duckdb/assets/167834271/427d9191-1728-4bfe-942f-423287fb1eed)

For those 14 apps listed on the 5,000,000,000+ downloads threshold we have 5 belonging to the " Communication " category, follow by 3 in the "Tools" and in third place the " Video Players & Editors " with 2 apps.
