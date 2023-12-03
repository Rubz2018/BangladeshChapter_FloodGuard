# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:56:45 2023

@author: ThinkPad
"""

import pandas as pd
import matplotlib.pyplot as plt


####### Rajshahi data missing values #######

Rajshahi = pd.read_csv(r'D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Swati/Rajshahi_C,km.csv')

Rajshahi.info() #50 columns, 4247 entries
#33 float, 8 int and 9 object

#non empty record in missing values colmuns
#preciptype - 2280, snow-585, snowdepth - 585, windgust - 604
#sealevelpressure-4175, visibility - 4175, severerisk - 585

#preciptype column shows rainy days which can't be everyday
#snow and snowdepth columns rae giving zero for some records which hold no meaning, ignored
##Like snow columns, severerisk was introduced from 10/01/2022 only which accounts for missing values

# convert the 'date' column to datetime format
Rajshahi['datetime'] = pd.to_datetime(Rajshahi['datetime'])

# display the updated dataframe
Rajshahi.head(50)

# plot the time series data
#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Rajshahi['datetime'], Rajshahi['windgust'], marker='o', linestyle='-')
#It seems that before 10/01/2022, the wind gust was measure only if greter than >30-35 but now, we have values for each day
#The values lies in the months of March, April and May

# Create a plot of the time series data for sea level pressure
plt.figure(figsize=(12, 6))
plt.plot(Rajshahi['datetime'], Rajshahi['sealevelpressure'], marker='o', linestyle='-')

# Identify the missing data points
missing_data_points = Rajshahi[Rajshahi['sealevelpressure'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps = missing_data_points['datetime']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps, [1] * len(missing_timestamps), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing Sea Level Pressure Data')
#Missing at random, can be ignored and impuated with mean

# Create a plot of the time series data for visibility
plt.figure(figsize=(12, 6))
plt.plot(Rajshahi['datetime'], Rajshahi['visibility'], marker='o', linestyle='-')
#the visibility is suddenly changing in 2022, more visisbilty showing good quality after 2012
#while it may not be correct as this peak also came on 10/01/2022 when four new columns were introduced
# Identify the missing data points
missing_data_points = Rajshahi[Rajshahi['visibility'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps = missing_data_points['datetime']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps, [1] * len(missing_timestamps), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing visibility Data')
#same as sea level pressure data



#####Chittagong data missing values#######
Chittagong = pd.read_csv(r'D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/weather/ekoue/Chittagong/Chittagong.csv')

Chittagong.info() #33 columns, 3947 entries
#22 float, 2 int, 9 object

#non empty record in missing values colmuns
#preciptype - 2359, snow-645, snowdepth - empty, windgust - 702
#sealevelpressure-3914, visibility - 3914, severerisk - 651

#snow column was introduced on 16/01/22 and has 0 values, snowdepth has all null values
#Like observed before, severrisk column was introduced on 10/01/22

#windgust
plt.figure(figsize=(12, 6))
plt.plot(Chittagong['datetime'], Chittagong['windgust'], marker='o', linestyle='-')
#For Chittagong, the measurements were made >20 and all over the year as wind gust has high values in winter too
#interesting to see

# convert the 'date' column to datetime format
Chittagong['datetime'] = pd.to_datetime(Chittagong['datetime'])

# display the updated dataframe
Chittagong.head(50)

# Create a plot of the time series data for sea level pressure
plt.figure(figsize=(12, 6))
plt.plot(Chittagong['datetime'], Chittagong['sealevelpressure'], marker='o', linestyle='-')
plt.show()

# Identify the missing data points
missing_data_points = Chittagong[Chittagong['sealevelpressure'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps = missing_data_points['datetime']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps, [1] * len(missing_timestamps), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing Sea Level Pressure Data')
#Missing at random, can be ignored and impuated with mean

# Create a plot of the time series data for visibility
plt.figure(figsize=(12, 6))
plt.plot(Chittagong['datetime'], Chittagong['visibility'], marker='o', linestyle='-')
plt.show()

#the visibility is suddenly changing in 2022, more visisbilty showing good quality after 2012
#while it may not be correct as this peak also came on 11/01/2022 when four new columns were introduced
# Identify the missing data points
missing_data_points = Chittagong[Chittagong['visibility'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps = missing_data_points['datetime']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps, [1] * len(missing_timestamps), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing visibility Data')
#same as sea level pressure data

# for the impuatation, we see how visibility is changing over the year
start_date = Chittagong['datetime'].min()
end_date = start_date.replace(day=1, month=1)  # Set the end date to January 1st of the same year
end_date = end_date + pd.DateOffset(days=365)  # Add 365 days

filtered_data = Chittagong[(Chittagong['datetime'] >= start_date) & (Chittagong['datetime'] <= end_date)]

# Create the plot for the first 365 days
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['datetime'], filtered_data['visibility'], marker='o', linestyle='-')

# Label your plot, add title, x-axis, and y-axis labels, etc.
plt.xlabel('Date')
plt.ylabel('Visibility')
plt.title('Visibility for the First 365 Days of the Year')
plt.grid(True)
#we can safely replace missing data with the mean of that month or from the previous year data



#####Sylhet data missing values#######
Sylhet = pd.read_csv(r'D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Swati/Sylhet_C,km.csv')

Sylhet.info() #33 columns, 3895 entries
#22 float, 2 int, 9 object

#non empty record in missing values colmuns
#preciptype - 2424, snow-599, snowdepth - 600, windgust - 646
#sealevelpressure-3872, visibility - 3877, severerisk - 599

#snow column was introduced on 16/01/22 and has 0 values, snowdepth has all null values
#Like observed before severrisk column was introduced on 10/01/22

# convert the 'date' column to datetime format
Sylhet['datetime'] = pd.to_datetime(Sylhet['datetime'])

# display the updated dataframe
Sylhet.head(50)

#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Sylhet['datetime'], Sylhet['windgust'], marker='o', linestyle='-')
#It seems that before 10/01/2022, the wind gust was measure only if greter than >40 but now, we have values for each day

# Let's see how it is changing over the year
start_date = Sylhet['datetime'].min()
end_date = start_date.replace(day=1, month=1)  # Set the end date to January 1st of the same year
end_date = end_date + pd.DateOffset(days=365)  # Add 365 days

filtered_data = Sylhet[(Sylhet['datetime'] >= start_date) & (Sylhet['datetime'] <= end_date)]

# Create the plot for the first 365 days
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['datetime'], filtered_data['windgust'], marker='o', linestyle='-')

# Label your plot, add title, x-axis, and y-axis labels, etc.
plt.xlabel('Date')
plt.ylabel('windgust')
plt.title('windgust for the First 365 Days of the Year')
plt.grid(True)
#only observed for some days in april and May each year

# Create a plot of the time series data for sea level pressure
plt.figure(figsize=(12, 6))
plt.plot(Sylhet['datetime'], Sylhet['sealevelpressure'], marker='o', linestyle='-')

# Identify the missing data points
missing_data_points = Sylhet[Sylhet['sealevelpressure'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps = missing_data_points['datetime']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps, [1] * len(missing_timestamps), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing Sea Level Pressure Data')
#Missing at random, can be ignored and impuated with mean

# Create a plot of the time series data for visibility
plt.figure(figsize=(12, 6))
plt.plot(Sylhet['datetime'], Sylhet['visibility'], marker='o', linestyle='-')
#the visibility is suddenly changing in 2022, more visisbilty showing good quality after 2012
#while it may not be correct as this peak also came on 10/01/2022 when four new columns were introduced
# Identify the missing data points
missing_data_points = Sylhet[Sylhet['visibility'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps = missing_data_points['datetime']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps, [1] * len(missing_timestamps), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing visibility Data')
#same as sea level pressure data, only some less values



###########Bogra################
Bogra = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Raj_Weather_combined/Bogra_Weather_combined.csv")
Bogra.info() #47 columns, 3895 entries

# convert the 'date' column to datetime format
Bogra['datetime'] = pd.to_datetime(Bogra['datetime'])

#non empty record in missing values colmuns
#preciptype - 2153, snow-585, snowdepth - 585, windgust - 614
#sealevelpressure-3807, visibility - 3807, severerisk - 585

#all the columns show same behavior, lets check for wind gust
#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Bogra['datetime'], Bogra['windgust'], marker='o', linestyle='-')
#Like Rajshahi, Bogra has windgust values recorded >40 and observed mainly in April and May with quite few entries in March, June



############Barisal###############
Barisal = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Raj_Weather_combined/Barisal_Weather_combined.csv")

# convert the 'date' column to datetime format
Barisal['datetime'] = pd.to_datetime(Barisal['datetime'])
Barisal.head(50)

Barisal.info()
#non empty record in missing values colmuns
#preciptype - 2279, snow-585, snowdepth - 585, windgust - 617
#sealevelpressure-3111, visibility - 3111, severerisk - 585

#all the columns show same behavior, lets check for wind gust
#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Barisal['datetime'], Barisal['windgust'], marker='o', linestyle='-')
# Bogra has windgust values recorded >40 and observed mainly in April and May with quite few entries in March, June



#############Dhaka#################
Dhaka = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Raj_Weather_combined/Dhaka_Weather_combined.csv")

# convert the 'date' column to datetime format
def convert_to_datetime(date_str):
    formats = ["%m/%d/%Y", "%d-%m-%Y"]
    for date_format in formats:
        try:
            return pd.to_datetime(date_str, format=date_format)
        except ValueError:
            pass
    return pd.NaT  # If none of the formats match, return Not a Timestamp (NaT)

# Apply the custom function to the 'datetime' column
Dhaka['datetime'] = Dhaka['datetime'].apply(convert_to_datetime)

Dhaka.head(50)

Dhaka.info()
#non empty record in missing values colmuns
#preciptype - 2202, snow-585, snowdepth - 585, windgust - 634
#sealevelpressure-3878, visibility - 3878, severerisk - 585

#all the columns show same behavior, lets check for wind gust
#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Dhaka['datetime'], Dhaka['windgust'], marker='o', linestyle='-')
#Like Chittagong, high values all over the year, will be another intersting case to study



##############Khulna##############
Khulna = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Raj_Weather_combined/Khulna_Weather_combined.csv")

# convert the 'date' column to datetime format
def convert_to_datetime(date_str):
    formats = ["%d/%m/%Y", "%d-%m-%Y"]
    for date_format in formats:
        try:
            return pd.to_datetime(date_str, format=date_format)
        except ValueError:
            pass
    return pd.NaT  # If none of the formats match, return Not a Timestamp (NaT)

# Apply the custom function to the 'datetime' column
Khulna['datetime'] = Khulna['datetime'].apply(convert_to_datetime)

# Sort the DataFrame by the 'datetime' column in increasing order
Khulna.sort_values(by='datetime', ascending=True, inplace=True)

# Reset the index if needed
Khulna.reset_index(drop=True, inplace=True)
Khulna.head(50)

Khulna.info()
#non empty record in missing values colmuns
#preciptype - 1805, snow-585, snowdepth - 587, windgust - 608
#sealevelpressure-2914 visibility - 2913, severerisk - 585

#all the columns show same behavior, lets check for wind gust
#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Khulna['datetime'], Khulna['windgust'], marker='o', linestyle='-')
#windgust values recorded >30 d observed mainly in April and May



###################Mymensingh################
Mymensing = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Raj_Weather_combined/Mymensigh_Weather_combined.csv")

# convert the 'date' column to datetime format
def convert_to_datetime(date_str):
    formats = ["%d/%m/%Y", "%d-%m-%Y"]
    for date_format in formats:
        try:
            return pd.to_datetime(date_str, format=date_format)
        except ValueError:
            pass
    return pd.NaT  # If none of the formats match, return Not a Timestamp (NaT)

# Apply the custom function to the 'datetime' column
Mymensing['datetime'] =Mymensing['datetime'].apply(convert_to_datetime)

# Sort the DataFrame by the 'datetime' column in increasing order
Mymensing.sort_values(by='datetime', ascending=True, inplace=True)

# Reset the index if needed
Mymensing.reset_index(drop=True, inplace=True)
Mymensing.head(50)

Mymensing.info()
#non empty record in missing values colmuns
#preciptype - 2186, snow-585, snowdepth - 586, windgust - 626
#sealevelpressure-3051, visibility - 3051, severerisk - 585

#all the columns show same behavior, lets check for wind gust
#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Mymensing['datetime'], Mymensing['windgust'], marker='o', linestyle='-')
#windgust values recorded >30 d observed mainly in May with fw vlaues in April and June



#############Narayanganj##############
Narayanganj = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Swati/Narayanganj_C,km.csv")

# convert the 'date' column to datetime format
Narayanganj['datetime'] = pd.to_datetime(Narayanganj['datetime'])
Narayanganj.head(50)

Narayanganj.info()
#non empty record in missing values colmuns
#preciptype - 2215, snow-599, snowdepth - 599, windgust - 650
#sealevelpressure-3892, severerisk - 599

#all the columns show same behavior, lets check for wind gust
#windgust analysis
plt.figure(figsize=(12, 6))
plt.plot(Narayanganj['datetime'], Narayanganj['windgust'], marker='o', linestyle='-')
#windgust values recorded >30 d observed mainly in May with fw vlaues in April and June
#recorde >= 30 before 2022 and spread all over the year



################Comilla#############
Comilla = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/Raj_Weather_combined/Comilla_Weather_combined.csv")
Comilla.info()
#non empty record in missing values colmuns
#preciptype - 2164, snow-569, snowdepth - 569, windgust - 669
#sealevelpressure-3864, severerisk - 569
#all the columns show same behavior




#######GIS data for LST_all districts##############
LST_all = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/gis/LST_all_districts.csv")
LST_all.info() #6 columns, 1152 entries, no missing values


########GIS data for LST_BD_districts##############
LST_BD = pd.read_csv(r"D:/bangladesh project/BangladeshChapter_FloodGuard-main/bangladeshchapter_floodguard/src/data/gis/LST_BD_District.csv")
LST_BD.info() #592 rows, 117 columns

LST_BD.isnull().sum().sum() #6790 missing values

# Find missing values for each column
missing_values = LST_BD.isnull().sum()

# Print the number of missing values for each column
print(missing_values) #all the columns have missing values

LST_BD['Date'] = pd.to_datetime(LST_BD['Date'])
LST_BD.head(50)

#Let's see for few columns the pattern for missing values
plt.figure(figsize=(12, 6))
plt.plot(LST_BD['Date'], LST_BD['LST_Day_1km_Dhaka'], marker='o', linestyle='-')

# Identify the missing data points
missing_data_points = LST_BD[LST_BD['LST_Day_1km_Dhaka'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps = missing_data_points['Date']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps, [1] * len(missing_timestamps), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing LST_Day_1km_Dhaka Data')

#For LST_Night_1km_Dhaka Data
missing_data_points1 = LST_BD[LST_BD['LST_Night_1km_Dhaka'].isnull()]

# Plot the missing data points
# Extract the datetime column (replace 'timestamp' with your actual datetime column name)
missing_timestamps1 = missing_data_points1['Date']

# Create a scatter plot with missing timestamps
plt.figure(figsize=(12, 6))
plt.scatter(missing_timestamps1, [1] * len(missing_timestamps1), marker='o', color='red')
plt.xlabel('Timestamp')
plt.title('Missing LST_Night_1km_Dhaka Data')
#many missing points

#One thing can be easily observed that for all the districts, LST_night has more missing values than LST_day
#Most of the missing values for LST_day are in June, July, August with very few exceptions in September, October
#Same goes for LST_night with missing values in the month of June, July, August and September with few exceptions