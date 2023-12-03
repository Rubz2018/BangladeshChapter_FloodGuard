import pandas as pd
import numpy as np
import os

SAGEMAKER_PROCESS=True # define if this file is being runned as part of sagemaker processing job or not (in local machine, for example)
FILE_NAME= "divisions daily weather.csv"

if __name__ == "__main__":

    print("==== Preprocessing started... =======")

    if SAGEMAKER_PROCESS:
        BASE_DIR = "/opt/ml/processing"
    else:    
        BASE_DIR= "../../../"


    if SAGEMAKER_PROCESS:
        # define input file
        RAW_FILE = os.path.join(BASE_DIR, f"files/input/{FILE_NAME}")

        # define output files
        BATCH_FILE= os.path.join(BASE_DIR, "files/batch/batch.csv")

    else:    
        # define input file
        RAW_FILE= os.path.join(BASE_DIR, f"data/weather/ekoue/combined/{FILE_NAME}")
        
        # define output files
        BATCH_FILE= os.path.join(BASE_DIR, "data/weather/ekoue/cleaned/sagemaker divisions daily weather -- inference.csv")


    # Read data
    df = pd.read_csv(RAW_FILE)


    # ====================== STARTED PROJECT CUSTOM PREPROCESS ======================= #
    
    # Columns to keep in the dataset (removing those that may induce target leakage )
    wanted_columns = [
        'cloudcover',
        #'conditions',
        'Date',
        #'DayType',
    #      'description',
        'dew',
        'Division',
        'feelslike',
    #      'feelslikemax',
    #      'feelslikemin',
        'humidity',
        'moonphase',
    #      'precip',
    #      'precipprob',
    #      'precipcover',
    #      'preciptype',
        'sealevelpressure',
    #      'severerisk',
        'Season',
        'snow',
    #      'snowdepth',
        'solarenergy',
        'solarradiation',
    #      'stations',
        'temp',
        'sunset',
        'sunrise',
        'tempmax',
        'tempmin',
        'uvindex',
    #      'visibility',
        'winddir',
    #      'windgust',
        'windspeed',
        # 'Flood',
        'Sunrise Hour',
        'Sunrise Minute',
        'Sunset Hour',
        'Sunset Minute'
    ]
    df = df[wanted_columns]

    # Remove samples with null season (those are outside of our range of study anyway, which is Jan 2013 to Oct 2023)
    df.dropna(subset=["Season"], inplace=True)

    # Convert date columns to datetime type
    df["Date"] = pd.to_datetime(df["Date"])
    df["sunset"] = pd.to_datetime(df["sunset"])
    df["sunrise"] = pd.to_datetime(df["sunrise"])


    # Remove samples with null entries
    df.dropna(inplace=True)

    # dummify categorical data
    df = pd.get_dummies(df, columns=["Division","Season"], prefix=["Division","Season"])

    # Engineering new columns
    df["DayOfMonth"] = df["Date"].dt.day
    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year
    df["sunrise_sunrise_mindiff"] = ( df["sunset"] - df["sunrise"]).dt.total_seconds()/60 # get elapsed time between sunrise and sunset, in minutes

    # Drop irrelevant columns to the project 
    columns_to_drop = [
        "snow", # has too many null values
        "Date", # no more needed, as features were already engineered based on it
        "sunset", # no more needed, as features were already engineered based on it
        "sunrise", # no more needed, as features were already engineered based on it
    ]
    df.drop(columns_to_drop,axis=1,inplace=True)

    # # Put the label as the first column in the df
    # y = df.pop("Flood")
    # df.insert(0, "Flood", y)
    
    # # Replace True and False by 1 and 0
    # df["Flood"] = df["Flood"].apply(lambda x: 1 if x==True else 0)

    # # shuffling dataframe content
    # df = df.sample(frac = 1, random_state=51294).reset_index(drop=True)

    # # Compute split lenghts
    # train_len = int(df.shape[0] * .7)
    # val_len = int(df.shape[0] * .15)
    # test_len = df.shape[0] - (train_len + val_len)

    # # Split datasets in train, val, test
    # train_df = df.loc[:train_len-1, :]
    # test_df = df.loc[train_len: train_len+val_len-1, :]
    # val_df = df.loc[train_len+val_len:, :]



    # ====================== ENDED PROJECT CUSTOM PREPROCESS ======================= #


    # train_df.to_csv(TRAIN_FILE, index=False, header=False)
    # val_df.to_csv(VAL_FILE, index=False, header=False)
    # test_df.to_csv(TEST_FILE, index=False, header=False)
    
    df.to_csv(BATCH_FILE, index=False, header=False)

    print("==== Preprocessing completed ======= !")

