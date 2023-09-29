#!/usr/bin/env python3

# ** Inmport pandas as pd  and read udemy.csv file and store in value name "dataS" **
import pandas as pd 
import matplotlib.pyplot as plt
dataS = pd.read_csv('udemy.csv')
# ** clean dataS In the section name 'course level' **
dataS = dataS[dataS['course level'] != 'Current price: $16.99']
dataS = dataS[dataS['course level'] != 'Current price: $19.99']

def main():
    x = dataS['instructors'].value_counts().head(20)

    instructors = []
    num_inst = []
    for i in dataS['instructors']:
        if i in instructors:
            continue
        else:
            instructors.append(i)
    for i in instructors:
        nub = 0
        for j in dataS['instructors']:
            if i == j:
                nub += 1
        num_inst.append(nub)

    list_data = []
    for i in x:
        inD = num_inst.index(i)
        name = instructors[inD]
        sum_rate = 0
        data = dataS[dataS['instructors'] == name]
        rate = data['Ratings'].apply(lambda x : x[8:11])

        for j in rate:
            if j != 'ws':
                fj = float(j)
                sum_rate += fj
        list_data.append([name,round(sum_rate/i,2),i])
    # print(list_data)
    make_graph(list_data)

def make_graph(list_d):
    left = [] 
    height = []
    name_instr = []
    for i in range(len(list_d)):
        left.append(i+1)
        height.append(list_d[i][1])
        name_instr.append(list_d[i][0])
    
    plt.bar(left,height,name_instr = name_instr,width=0.8,color = ['blue','pink'])
    # plt.plot(name_instr,height)
    plt.xlabel('instructors')
    plt.ylabel('Average Ratings')
    plt.title('test1')
    plt.show()
    # print(name_instr)




if __name__ == '__main__':
    main()