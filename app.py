import pandas as pd
import numpy as np
import math
import scipy
from scipy import stats as s
import csv
import statistics

dataset = 'datasets/L-L1.csv'

def readColumn(columnNumber):
    column=[]
    with open(dataset) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            column.append(row[columnNumber-1])
            lineCount += 1
    return column

def convertToFolat(column):
    floatData = []
    for i in column:
        floatData.append(float(i))
    return floatData

def getVariance(column):
    variance = np.var(column)
    return variance

def getMean(column):
    mean = statistics.mean(column)
    return mean

def getMedian(column):
    median = statistics.median(column)
    return median

def getMode(column):
    mode = s.mode(column)[0][0]
    return mode

def getStandardDeviation(column):
    standardDeviation = statistics.stdev(column)
    return standardDeviation

def printValues(mean, median, mode, variance, standardDeviation):
    print('Mean : ', mean)
    print('Median : ', median)
    print('Mode : ', mode)
    print('Variance : ', variance)
    print('Standard Deviation : ', standardDeviation)

def main():

    column1 = readColumn(1)
    column1 = convertToFolat(column1)
    mean = getMean(column1)
    median = getMedian(column1)
    mode = getMode(column1)
    variance = getVariance(column1)
    standardDeviation = getStandardDeviation(column1)
    printValues(mean, median, mode, variance, standardDeviation)

    column2 = readColumn(2)
    column2 = convertToFolat(column2)
    mean = getMean(column2)
    median = getMedian(column2)
    mode = getMode(column2)
    variance = getVariance(column2)
    standardDeviation = getStandardDeviation(column2)
    printValues(mean, median, mode, variance, standardDeviation)

main()