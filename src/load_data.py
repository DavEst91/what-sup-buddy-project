import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split_data(X,y):
    X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8)
    X_train=np.stack(np.asarray(X_train))
    y_train=np.stack(np.asarray(y_train))
    X_test=np.stack(np.asarray(X_test))
    y_test=np.stack(np.asarray(y_test))
    return X_train,X_test,y_train,y_test