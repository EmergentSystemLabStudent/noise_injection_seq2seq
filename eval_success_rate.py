import pandas as pd
import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    list = pd.read_csv("GPSRsentence_list.csv")
    label = list["label"]
    results = open(filename, "r")
    result = results.readlines()
    success = 0
    for i in range(100):
        # print(i)
        # print(result[i])
        # print(label[i])
        if result[i] == label[i] + "\n":
            # print("1")
            success = success + 1
        # else:
        # print("0")
        # print("\n")
    results.close()
    print(filename, success)
    # for label in :
    #    print(label)
