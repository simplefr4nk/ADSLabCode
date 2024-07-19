package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"time"
)

const E = 0.001

type TestCase struct {
	Array  []int `json:"array"`
	K      int   `json:"k"`
	Length int   `json:"length"`
}

func resolution() float64 {
	start := time.Now()
	for time.Since(start).Seconds() == 0 {
	}
	stop := time.Now()
	return stop.Sub(start).Seconds()
}

func measure(A []int, length, K int, Tmin float64) float64 {
	count := 0
	startTime := time.Now()
	for {
		Select(A, 0, length-1, K)
		count++
		endTime := time.Now()
		if endTime.Sub(startTime).Seconds() >= Tmin {
			break
		}
	}
	return time.Since(startTime).Seconds() / float64(count)
}

func main() {
	file, err := os.Open("Code/test_cases.json")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	byteValue, _ := io.ReadAll(file)

	var testCases []TestCase
	json.Unmarshal(byteValue, &testCases)

	Tmin := resolution() * (1/E + 1)

	csvFile, err := os.Create("go.csv")
	if err != nil {
		fmt.Println("Error creating CSV file:", err)
		return
	}
	defer csvFile.Close()

	csvWriter := csv.NewWriter(csvFile)
	defer csvWriter.Flush()

	err = csvWriter.Write([]string{"length array", "time"})
	if err != nil {
		fmt.Println("Error writing record to CSV file:", err)
		return
	}

	for i, testCase := range testCases {
		record := []string{fmt.Sprintf("%d", testCase.Length), fmt.Sprintf("%g", measure(testCase.Array, testCase.Length, testCase.K, Tmin))}
		if i%10 == 0 {
			fmt.Println(i)
		}
		err := csvWriter.Write(record)
		if err != nil {
			fmt.Println("Error writing record to CSV file:", err)
			return
		}
	}
}

func Select(A []int, start, end, index int) int {
	for (end-start+1)%5 != 0 {
		for j := start + 1; j <= end; j++ {
			if A[start] > A[j] {
				A[start], A[j] = A[j], A[start]
			}
		}
		if index == 0 {
			return A[start]
		}
		start++
		index--
	}

	numberSubArray := (end - start + 1) / 5
	for j := 0; j < numberSubArray; j++ {
		insertionSort(A, start+j*5, start+j*5+4, 1)
	}

	medians := make([]int, numberSubArray)
	for i := 0; i < numberSubArray; i++ {
		medians[i] = A[start+i*5+2]
	}

	medianOfMedians := Select(medians, 0, numberSubArray-1, numberSubArray/2)
	pivotIndex := partitionAround(A, start, end, medianOfMedians)
	pivotPosition := pivotIndex - start

	if index == pivotPosition {
		return A[pivotIndex]
	} else if index < pivotPosition {
		return Select(A, start, pivotIndex-1, index)
	} else {
		return Select(A, pivotIndex+1, end, index-pivotPosition-1)
	}
}

func partitionAround(A []int, p, r, x int) int {
	for i := p; i <= r; i++ {
		if A[i] == x {
			A[i], A[r] = A[r], A[i]
			break
		}
	}

	i := p - 1
	for j := p; j < r; j++ {
		if A[j] <= x {
			i++
			A[i], A[j] = A[j], A[i]
		}
	}
	A[i+1], A[r] = A[r], A[i+1]
	return i + 1
}

func insertionSort(A []int, p, q, x int) {
	for i := p + x; i <= q; i += x {
		key := A[i]
		j := i - x
		for j >= p && A[j] > key {
			A[j+x] = A[j]
			j -= x
		}
		A[j+x] = key
	}
}
