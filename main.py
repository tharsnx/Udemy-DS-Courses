#!/usr/bin/env python3

# ** Inmport pandas as pd  and read udemy.csv file and store in value name "dataS" **
import pandas as pd 
dataS = pd.read_csv('udemy.csv')
# ** clean dataS In the section name 'course level' **
dataS = dataS[dataS['course level'] != 'Current price: $16.99']
dataS = dataS[dataS['course level'] != 'Current price: $19.99']

def main():
    print(dataS['reviews'])
    way = int(input('''/////////////////////////////////////////////////////
Please enter the search material you are looking for ?? 
1. Course
2. Course level	
3. Duration
4. Instructors
Enter: '''))



if __name__ == '__main__':
    main()