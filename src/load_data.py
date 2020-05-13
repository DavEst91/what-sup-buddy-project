import pandas as pd
import numpy as np

def load_dataframe(train_test):
    df=pd.read_csv("input/fer2013.csv")
    if train_test=="train":
        return df[df.Usage=="Training"].drop(columns=["Usage"],inplace=True)
    elif train_test=="test":
        return df[df.Usage=="PrivateTest"].drop(columns=["Usage"],inplace=True)