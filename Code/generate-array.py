import json
import math
import random

def lengthArray(num_samples):
    A = 100
    B = 1000 ** (1 / (num_samples - 1))
    return [round(A * (B ** i)) for i in range(num_samples)]

def randomArray(length, _range: tuple[int, int]):
    return [random.randint(*_range) for _ in range(length)]

def linspace(start, stop, num):
    step = (stop - start) / (num - 1)
    return [start + step * i for i in range(num)]

def generateTestCases(num_samples, k_samples):
    lengths = lengthArray(num_samples)
    ranges = [(0, 500000),(500000, 1000000),(1000000, 1500000)]
    test_cases = []
    i = 1

    for length in lengths:
        print(length)
        for k in linspace(1, length - 1, k_samples):
            array_1 = randomArray(length, ranges[0])
            array_2 = randomArray(length, ranges[1])
            array_3 = randomArray(length, ranges[2])
            print({'length': length, 'k': int(k)})
            test_cases.append({'array': [array_1, array_2, array_3], 'length': length, 'k': int(k)})
    
    return test_cases

if __name__ == "__main__":
    num_samples = int(input("Quanti sample? "))
    k_samples = int(input("Quanti sample di K per ogni lunghezza di array? "))
    test_cases = generateTestCases(num_samples, k_samples)
    
    with open('test_cases.json', 'w') as f:
        json.dump(test_cases, f)
    
    print("Test cases saved to 'test_cases.json'")
