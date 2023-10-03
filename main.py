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
    print(x)
    instructors = []
    num_inst = []
    # list_x =[]
    for i in dataS['instructors']:
        # if i in instructors:
        #     print('aom!!!!!')
        #     continue
        # else:
        if len(instructors) == 0:
            instructors.append(i)
        else:
            k = 0
            for j in instructors:
                if i == j:
                    k += 1
                    break
            if k == 0:
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
        # print(inD)
        name = instructors[inD]
        sum_rate = 0
        data = dataS[dataS['instructors'] == name]
        rate = data['Ratings'].apply(lambda x : x[8:11])
        max_rate = 0
        for j in rate:
            if j != 'ws':
                fj = float(j)
                sum_rate += fj
                if fj > max_rate:
                    max_rate = fj
        list_data.append([name,round(sum_rate/i,2),max_rate,i])
        num_inst[inD] = 0
    # print(list_data)
    make_graph(list_data)

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
        # print(list_d[i][0])

    
    plt.figure(figsize=(15,5))

    t = {'Average': average_rate,'Max' : max_rate}
    tf = pd.DataFrame(t,columns=['Average','Max'],index=name_instr)
    tf.plot.bar()

    # plt.bar(left,average_rate,tick_label = name_instr,width=0.8,color = ['red', 'green'])
    # plt.xlabel('instructors')
    # plt.ylabel('Average Ratings')
    # plt.title('test1')
    plt.savefig('hello world.png')
    # plt.show()
    # print(list_d)




if __name__ == '__main__':
    main()