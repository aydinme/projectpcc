#!/usr/local/bin/python3

# This is the runner program for the correlation Checker tool.
# The goal of this tool is to examine the correlation (if any) between
# severity of a disease case and expression levels of a gene based on
# each pcr experiment input.

import math
import numpy as np
import matplotlib as mpl
import re

import matplotlib.pyplot as plt

#Define a gene array for input for each severity score
target_severity1 = []
target_severity2 = []
target_severity3 = []
target_severity4 = []
#Define a control array for input
control_severity1 = []
control_severity2 = []
control_severity3 = []
control_severity4 = []
# Arrays to store normalized values after simpleNormalizer funtion..
normalized_severity1 = []
normalized_severity2 = []
normalized_severity3 = []
normalized_severity4 = []


my_input = input("This Program displays RP11-248E9.5 correlation with \
pneumonia patients based on Real-Time PCR Experiment Data. \
Please enter the location of your exported PCR experiment file. \n" )

my_file = open(my_input)

def organizeArrays():
    for line in my_file:
        my_column = line.split('\t')
        if re.search(r'1',my_column[2]):
            target_severity1.append(my_column[0])
            control_severity1.append(my_column[1])
        if re.search(r'2',my_column[2]):
            target_severity2.append(my_column[0])
            control_severity2.append(my_column[1])
        if re.search(r'3',my_column[2]):
            target_severity3.append(my_column[0])
            control_severity3.append(my_column[1])
        if re.search(r'4',my_column[2]):
            target_severity4.append(my_column[0])
            control_severity4.append(my_column[1])


# a simpler normalizer that neglects control group...
# It would take a value from gene input as target,
# internal control input as control
# and add this value to the expression array..
# This is a basic delta ct normalization method for PCR based on ct values..

def simpleNormalizer(target,control,my_expression_array):
    mydelta = int(target)-int(control)
    my_expression = math.pow(2,-mydelta)
    my_expression_array.append(my_expression)

# a simple boxplot function
# It would take the values from normalized gene arrays and show a boxplot
# based on the severityScores...

def plotData(sample1,sample2,sample3,sample4):
    data_to_plot = [sample1,sample2,sample3,sample4]
    # Create a figure instance
    plt.boxplot(data_to_plot,patch_artist=True,
    labels=['severity1','severity2','severity3','severity4'])
    plt.title('Correlation results of Gene Based on Severity Score:')
    plt.ylabel('Expression')
    plt.show()

# Mean Expression method.. This method calculates the mean value of each
# normalized expression array..
def meanExpression(sample):
    my_sum = 0
    for i in range(1,len(sample)):
        my_sum = my_sum + sample[i]
    my_mean_expression = my_sum/len(sample)
    return my_mean_expression

#MAIN function
#It normalizes all of the arrays...
def normalizeAll():
    for i in range(1,len(target_severity1)):
        simpleNormalizer(target_severity1[i],control_severity1[i],
        normalized_severity1)
    for i in range(1,len(target_severity2)):
        simpleNormalizer(target_severity2[i],control_severity2[i],
        normalized_severity2)
    for i in range(1,len(target_severity3)):
        simpleNormalizer(target_severity3[i],control_severity3[i],
        normalized_severity3)
    for i in range(1,len(target_severity4)):
        simpleNormalizer(target_severity4[i],control_severity4[i],
        normalized_severity4)

# Now the program is ready to run...

# Step 1 -> Organize arrays based on our input file...
organizeArrays()
# Step 2 -> Normalize these arrays...
normalizeAll()

# Step 3 -> Print mean values for each Severity Score as a command line output.

print("Mean R Value for Severity Score 1 is: " +
str(meanExpression(normalized_severity1)))
print("Mean R Value for Severity Score 2 is: " +
str(meanExpression(normalized_severity2)))
print("Mean R Value for Severity Score 3 is: " +
str(meanExpression(normalized_severity3)))
print("Mean R Value for Severity Score 4 is: " +
str(meanExpression(normalized_severity4)))

# Step 4 -> Boxplot output.. 
plotData(normalized_severity1,normalized_severity2,normalized_severity3,
normalized_severity4)
