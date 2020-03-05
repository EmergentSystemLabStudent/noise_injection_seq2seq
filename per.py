from jiwer import wer
import sys
if __name__ == '__main__':
    f = open("GPSRsentence_phoneme_list", "r")
    dir = sys.argv[1]
    g = open(dir+"google_phonemeresultdata.csv")
    s = open(dir+"sphinx_phonemeresultdata.csv")
    sumg = 0
    sums = 0

    for i in range(100):
        print(i)
        s1 = f.readline()
        s2 = g.readline()
        s3 = s.readline()
        wg = wer(s1, s2)
        ws = wer(s1, s3)
        print(i, wg, ws)
        sumg += wg
        sums += ws
    print("avg", sumg/100.0, sums/100.0)
