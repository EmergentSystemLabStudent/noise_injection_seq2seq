from jiwer import wer
import pandas as pd
import sys

if __name__ == "__main__":
    dir = sys.argv[1]
    google_file = open(dir + "google")
    google = google_file.read().split("\n")
    sphinx_file = open(dir + "sphinx")
    sphinx = sphinx_file.read().split("\n")
    df = pd.read_csv("GPSRsentence_list.csv")
    sumg = 0
    sums = 0
    for index, row in df.iterrows():
        label = row.label
        wg = wer(label, google[index])
        ws = wer(label, sphinx[index])
        print(index, wg, ws)
        sumg += wg
        sums += ws
    print("avg", sumg / 100.0, sums / 100.0)
