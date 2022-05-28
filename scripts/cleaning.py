import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce
from xxlimited import Str
import os,sys
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from scripts.logger import logger

# read and process data
class ReadData():

    # read the data
    def read_data(self, path):
        data = pd.read_csv(path, sep = ';')
        logger.info("Successfully read the data")
        return data

class Clean():

    def __init__(self, df):
        """initialize the cleaning class"""
        self.df = df
        logger.info("Successfully initialized clean class")

    ##missing values###

    def has_missing_values(self):
        """
        expects:
            -   nothing
        returns:
            -   boolean
        """
        has_missing_values = False
        if True in self.df.isnull().any().to_list():
            has_missing_values = True
        counts = None
        counts = self.df.isnull().sum()
        logger.info("Successfully checked for missing values")
        return counts,has_missing_values

    def drop_missing_values(self)->pd.DataFrame:
        """
        remove rows that has column names.  
        """
        self.df.dropna(inplace=True)
        logger.info("Successfully dropped the columns with missing values")


    def remove_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns in the list are removed
        Parameters
        ----------
        columns:
            Type: list
        Returns
        -------
        pd.DataFrame
        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df


    def store_features(self,type_,value):
        """
        purpose:
            - stores features for the data set
        input:
            - string,int,dataframe
        returns:
            - dataframe
        """
        features = [None]
        if type_ == "numeric":
            features = self.df.select_dtypes(include=value).columns.tolist()
        elif type_ == "categorical":
            features = self.df.select_dtypes(exclude=value).columns.tolist()
        logger.info("Successfully stored the features")
        return features

    def drop_duplicate(self, df:pd.DataFrame,column)->pd.DataFrame:
        """
        - this function drop duplicate rows
        """
        self.df = self.df.drop_duplicates(subset=[column])
        logger.info("Successfully dropped rows with duplicate values")
        return self.df
    
    def convert_to_datetime(self, column)->pd.DataFrame:
        """
        convert column to datetime
        """
        self.df[column] = pd.to_datetime(self.df[column])
        logger.info("Successfully converted the column to datetime")
        return self.df

    def treat_null(self, data):
        global categorical, discrete, continous, cols
        categorical = []
        discrete = []
        continous = []
        for col in data.columns:
            if data[col].dtype == object:
                categorical.append(col)
            elif data[col].dtype in ['int16', 'int32', 'int64']:
                discrete.append(col)
            elif data[col].dtype in ['float16', 'float32', 'float64']:
                continous.append(col)

        cols = discrete + categorical + continous
        data = data[cols]

        # null values
        # data = preprocess_data(data)
        indices = []
        for col in cols:
            k = data.columns.get_loc(col)
            indices.append(k)

        for col in indices:
            if data.columns[col] in discrete:
                x = data.iloc[:, col].values
                x = x.reshape(-1,1)
                imputer = SimpleImputer(missing_values=np.nan, strategy='median')
                imputer = imputer.fit(x)
                x = imputer.transform(x)
                data.iloc[:, col] = x

            if data.columns[col] in continous:
                x = data.iloc[:, col].values
                x = x.reshape(-1,1)
                imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
                imputer = imputer.fit(x)
                x = imputer.transform(x)
                data.iloc[:, col] = x

            elif data.columns[col] in categorical:
                x = data.iloc[:, col].values
                x = x.reshape(-1,1)
                imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
                imputer = imputer.fit(x)
                x = imputer.transform(x)
                data.iloc[:, col] = x     
        logger.info("Successfully handled missing values")
        return data

     # outlier detection + treatment
    def outlier_correcter(self, data):
        # data = treat_null(data)
        for col in discrete + continous:
            data[col] = data[col].clip(lower=data[col].quantile(0.25), upper=data[col].quantile(0.75))
        return data

        # encoding categorical
    def encoder(self, data):
        # data = scaler(data)
        cols = categorical.copy()
        cols.remove('y')
        data = pd.get_dummies(data, columns = cols)
        return data

    def change_column_to_date_type(self, col_name: str) -> None:
        try:
            self.df[col_name] = pd.to_datetime(self.df[col_name])
        except:
            print('failed to change column to Date Type')
        self.logger.info(
            f"Successfully changed column {col_name} to Date Type")
    
    def change_columns_type_to(self, cols: list, data_type: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns data types are changed to the specified data type
        Parameters
        ----------
        cols:
            Type: list
        data_type:
            Type: str
        Returns
        -------
        pd.DataFrame
        """
        try:
            for col in cols:
                self.df[col] = self.df[col].astype(data_type)
        except:
            print('Failed to change columns type')
        self.logger.info(f"Successfully changed columns type to {data_type}")
        return self.df
    
    def replace_outlier_with_median(self, dataFrame: pd.DataFrame, feature: Str) -> pd.DataFrame:

        Q1 = dataFrame[feature].quantile(0.25)
        Q3 = dataFrame[feature].quantile(0.75)
        median = dataFrame[feature].quantile(0.50)

        IQR = Q3 - Q1

        upper_whisker = Q3 + (1.5 * IQR)
        lower_whisker = Q1 - (1.5 * IQR)

        dataFrame[feature] = np.where(
            dataFrame[feature] > upper_whisker, median, dataFrame[feature])
        dataFrame[feature] = np.where(
            dataFrame[feature] < lower_whisker, median, dataFrame[feature])
        self.logger.info(f"Outlier for {feature} is fixed")

        return dataFrame

    def label_encoding(self,train,test=None):
        """
        - label encode the data
        """
        categorical_features=self.store_features("categorical","number")
        train[categorical_features] = train[categorical_features].apply(lambda x: pd.factorize(x)[0])
        logger.info("Successfully encoded your categorical data")


    def transfrom_time_series(self,date_column):
        """
        - transform the data into a 
        time series dataset
        """
        self.df[date_column] = pd.to_datetime(self.df[date_column],errors='coerce')
        self.df['Day'] = self.df[date_column].dt.day
        self.df['Month'] = self.df[date_column].dt.month
        self.df['Year'] = self.df[date_column].dt.year
        self.df['DayOfYear'] = self.df[date_column].dt.dayofyear
        self.df['WeekOfYear'] = self.df[date_column].dt.weekofyear
        self.df.set_index(date_column, inplace=True)
        logger.info("Successfully transformed data to time series data")

    def aggregations(self,df,column=None,second_column=None,
                    third_column=None,according_to="sum"):
        """
        - this is for adding features based on aggregations
        """
        if according_to=="sum":
            grouped_x =  df.groupby([df[column]])[second_column].sum()
        elif according_to=="mean":
            grouped_x =  df.groupby([df[column]])[second_column].mean()
        grouped_y = df.groupby([df[column]])[third_column].count()
        per_x = grouped_x / grouped_y
        logger.info("successful aggregation")
        return dict(per_x)

    def save(self,name):
        """
        - returns the dataframes
        """
        self.df.to_csv(name,index=False)
        logger.info("Successfully saved the dataframe")

    def get_df(self):
        """
        - returns the dataframe
        """
        return self.df

    def transfrom_time_series(self,date_column):
        """
        - transform the data into a 
        time series dataset
        """
        self.df[date_column] = pd.to_datetime(self.df[date_column],errors='coerce')
        self.df['Day'] = self.df[date_column].dt.day
        self.df['Month'] = self.df[date_column].dt.month
        self.df['Year'] = self.df[date_column].dt.year
        self.df['DayOfYear'] = self.df[date_column].dt.dayofyear
        self.df['WeekOfYear'] = self.df[date_column].dt.weekofyear
        self.df.set_index(date_column, inplace=True)
        logger.info("Successfully transformed data to time series data")

    def save_clean_data(self, name: str):
        """
        The objects dataframe gets saved with the specified name 
        Parameters
        ----------
        name:
            Type: str
        Returns
        -------
        None
        """
        try:
            self.df.to_csv(name, index=False)
            self.logger.info(f"DataFrame saved")
        except:
            print("Failed to save data")


