import pandas as pd # type: ignore
import numpy as np  # type: ignore
import os
import yaml #type: ignore


# -----------------------------
# Config reader function
# -----------------------------

def load_config(path = "config.yml"):
        with open(path, "r") as f:
            return yaml.safe_load(f)
        
            
# -----------------------------
# CSV Transformer class
# -----------------------------

class CSVTransformer:
    def __init__(self, config_file = "config.yml"):
        print("Loading the config properties....")
        self.props = load_config(config_file) #load the config file to props variable
        self.data = None
        self.path = self.props["input_file"] #get the input file path from config(input_path)

    def read(self):
        if self.path is None or not os.path.exists(self.path):
            raise FileNotFoundError("File not Found")
        else:
            print("Reading the input file data....")
            self.data = pd.read_csv(self.path)
                      
    def transform(self):
        if self.data is None:
            print( "Data Empty ")
        else:
            print("replacing the Invalid values in the data....")
            replacements = {val: pd.NA for val in self.props["invalid_replacements"]}
            self.data = self.data.replace(replacements)
        self.missfill()
        self.changetype()
        self.dropduplicates()

    def uniqueness(self):
        # print(self.data.dtypes)
        for col in self.data:
            print(f'column : {col}')
            print(self.data[col].unique())

    def changetype(self):
        col = self.props["date_column"]
        print(f'Changing type of columns....')
        for c in self.data.columns:
            if c != col:
                self.data[c] = self.data[c].apply(pd.to_numeric, errors = 'ignore')
            else:
                self.data[c] = pd.to_datetime(self.data[c], errors='coerce')


    def missfill(self):
        print("Filling the missing values....")
        fill_rules = self.props["missing_values"]
        self.data = self.data.fillna(fill_rules)
    
    def dropduplicates(self):
        if self.data is None:
            print("Data Empty")
        else:
            print("Dropping Duplicates if any")
            print(self.data[self.data.duplicated()])
            self.data = self.data.drop_duplicates()
        # return self.data[self.data.duplicated()]

    def load(self):
        output_file = self.props.get("output_file")
        if self.data is None:
            print( "Data Empty ")
        else:
            print("Loading the cleaned data into output file....")
            return  self.data.to_csv(output_file, index=False)

file = CSVTransformer("config.yml")
file.read()
file.transform()
file.load()
