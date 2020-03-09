import pandas as pd

if __name__ == '__main__':
    scores = pd.read_csv("data.csv", index_col = "Participant Code")
    scores.head(26)