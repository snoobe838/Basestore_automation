import pandas as pd


def read_test_data(file_name, sheet_name):

    df = pd.read_excel(file_name, sheet_name=sheet_name)
    for column in df.columns:
        if df[column].dtype in ['int64', 'float64']:
            df[column] = df[column].astype(str)
    return df.values.tolist()