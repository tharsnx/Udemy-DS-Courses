#!/usr/bin/env python3

# ** Inmport pandas as pd  and read udemy.csv file and store in value name "dataS" **
import pandas as pd 
import matplotlib.pyplot as plt
dataS = pd.read_csv('udemy.csv')
# ** clean dataS In the section name 'course level' **
dataS = dataS[dataS['course level'] != 'Current price: $16.99']
dataS = dataS[dataS['course level'] != 'Current price: $19.99']
dataS = dataS[dataS['reviews'] != '0 reviews']

def main():
    n = int(input())
    list_data = make_Data(n)
    make_graph(list_data)
    #################################################################
    #ตัวอย่าง#
    # y = dataS[dataS['instructors'] == 'Spotle Learn']
    # print(y)


def make_Data(n):
    x = dataS['instructors'].value_counts().head(n)
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
    result = []
    for i in x:
        inD = num_inst.index(i)
        name = instructors[inD]
        sum_rate = 0
        data = dataS[dataS['instructors'] == name]
        rate = data['Ratings'].apply(lambda x : x[8:11])
        max_rate = 0
        for j in rate:
            if j != 'ws' :
                fj = float(j)
                sum_rate += fj
                if fj > max_rate:
                    max_rate = fj
        result.append([name,round(sum_rate/i,2),max_rate,i])
        num_inst[inD] = 0
    return result


def make_graph(list_d):
    left = [] 
    average_rate = []
    name_instr = []
    max_rate = []
    for i in range(len(list_d)):
        left.append(i+1)
        average_rate.append(list_d[i][1])
        name_instr.append(list_d[i][0])
        max_rate.append(list_d[i][2])

    t = {'Average': average_rate,'Max' : max_rate}
    tf = pd.DataFrame(t,columns=['Average','Max'],index=name_instr)
    plt.figure(figsize=(15,40))
    tf.plot.bar()
    plt.savefig('have 0 reviews.png')
    plt.show()


if __name__ == '__main__':
    main()