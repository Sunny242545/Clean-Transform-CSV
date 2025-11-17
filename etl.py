import pandas as pd # type: ignore
import numpy as np  # type: ignore
import os

class CSVTransformer:
    def __init__(self, path = None):
        self.data = None
        self.path = path

    def read(self):
        if self.path is None or not os.path.exists(self.path):
            raise FileNotFoundError("File not Found")
        else:
            self.data = pd.read_csv(self.path)
                      
    def transform(self):
        if self.data is None:
            print( "Data Empty ")
        else:
            self.data = self.data.replace({"ERROR": pd.NA, "UNKNOWN": pd.NA})

    def columntypes(self):
        print(self.data.dtypes)
        # for col in self.data:
        #     print(f'column : {col}')
            # print(self.data[col].unique())

    def changetype(self):
        col = 'Transaction Date'
        if col in self.data.columns:
            print(f'Changing type of column: {col} along with other numeric columns')
            for c in self.data.columns:
                if c != col:
                    self.data[c] = self.data[c].apply(pd.to_numeric, errors = 'ignore')
                else:
                    self.data[c] = pd.to_datetime(self.data[c], errors='coerce')
        else:
            print(f'Column {col} not found in data')
        # print(self.data['Transaction Date'].dtype)
        # print(self.data['Transaction Date'].head())

    def load(self):
        if self.data is None:
            print( "Data Empty ")
        else:
            return  self.data.to_csv('cleaned_data.csv', index=False)

file = CSVTransformer('dirty_data.csv')
file.read()
file.transform()
file.columntypes()
file.changetype()
file.load()

file2 = CSVTransformer('cleaned_data.csv')
file2.read()
file2.changetype()
file2.columntypes()
