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

    def load(self):
        if self.data is None:
            print( "Data Empty ")
        else:
            return  self.data.to_csv('cleaned_data.csv', index=False)

file = CSVTransformer('dirty_data.csv')
file.read()
file.transform()
file.load()
