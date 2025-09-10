import pandas as pd
import os
# def get_csv(file):
#     df = pd.read_csv(file)
#     return df

# df = "E:/CEDMAP python/Code Sarvarth/Project1/data/raw.csv"

# # get_csv(df)
# print(get_csv(df))

def data_load(path):
    """
    Load Student performance data from CSV file
    
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Data File not found as: {path}")
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")
    
df = "E:/CEDMAP python/Code Sarvarth/Project1/data/raw.csv"
print(data_load(df))