import sys
import os

# Aggiungi la directory principale al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from SORT.SortingAlgorithms import QuickSelect, Select, HeapSelect
from UTILS.Measure import minMeasureTime, Measure
import json
import csv

def main():
    Tmin = minMeasureTime()

    # Legge i test case dal file JSON
    with open('../test_cases.json', 'r') as f:
        allTests = json.load(f)

    # Misura il tempo di esecuzione di Select
    with open('../Golang/createGraphs/csv/select.csv', 'w+') as f:
        print("Select")
        csvWriter = csv.writer(f)
        for test in allTests:
            #               range,         length,         k, misura
            for idx, arr in enumerate(test['array']):
                csvWriter.writerow([idx+1, test['length'], test['k'], Measure(arr, test['k'], Tmin, Select)])

    # Misura il tempo di esecuzione di Quick Select
    with open('../Golang/createGraphs/csv/quickselect.csv', 'w+') as f:
        print("QuickSelect")
        csvWriter = csv.writer(f)
        for test in allTests:
            #               range,         length,         k, misura
            for idx, arr in enumerate(test['array']):
                csvWriter.writerow([idx+1, test['length'], test['k'], Measure(arr, test['k'], Tmin, QuickSelect)])

    # Misura il tempo di esecuzione di Heap Select
    with open('../Golang/createGraphs/csv/heapselect.csv', 'w+') as f:
        print("HeapSelect")
        csvWriter = csv.writer(f)
        for test in allTests:
            #               range,         length,         k, misura
            for idx, arr in enumerate(test['array']):
                csvWriter.writerow([idx+1, test['length'], test['k'], Measure(arr, test['k'], Tmin, HeapSelect)])


if __name__ == "__main__":
    main()
