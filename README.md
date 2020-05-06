# projectpcc

* ABOUT *

Gene expression/Disease Severity Correlation Checker based on Real-Time PCR Experiment Data.

Source code can be obtained here:
https://github.com/aydinme/projectpcc/blob/master/runner.py

Demo with pre-uploaded files:
https://github.com/aydinme/projectpcc
	--> Can be found under 'Exemplaryi demo I/O files'


Summary of the Program:
	This program is an external tool to check for gene expression/severity
correlations based on Real-Time PCR experiments. In a Real-Time Experiment, readings
are acquired from different filters. This program assumes that there are two readings;
1 for target gene which is from the FAM Channel, the other for control gene which is from the HEX Channel..
	There are many Real-Time PCR Softwares out there that exports different outputs. However, all of them has these following titles;

Label	Target Channel	Ct Value 	Control Channel 	Ct Value	Extra Info

	Based on the Real-Time PCR Instrument we are using, the program should be modified since outputs would be different. This version 1 of the program	assumes that the Real-Time PCR export data is within the following format;

Channel1	Channel2	Severity Score
ct value1	ct value1	severity value 1
ct value2	ct value2	severity value 2
ct value3	ct value3	severity value 3
...		...		...
...		...		...
...		...		...

Then the program calculates the expression correlation based on severity scores 
and displays them within a boxplot.. The correlation equation is R = 2^-deltact
A deltadeltact method is better for better quantitation but since there is no control group,
the second delta is neglected. 

Step by step Instructions for the use of program:

1) Open terminal
2) make sure the program is in your working directory
3) enter command -> python3 runner.py
4) The program will execute and ask you to enter the location of your experiment file.
	enter this location..
5) The program will output a boxplot for this correlation relation and show mean expression values on the command line.
