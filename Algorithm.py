import csv
import numpy as np
import random

def main():
    with open('D:\\软件工程.csv','r') as f:
        reader=csv.reader(f)
        header=next(reader)

        # for row in reader:
        #     print("{}{}: {}={}, {}={}, {}={}  {}={}".format(header[0], row[0],
        #                                              header[1], row[1],
        #                                              header[2], row[2],
        #                                              header[3], row[3],
        #                                              header[4], row[4]
        #                                              )
        #           )

        list1=[]    #是否班委
        list2=[]    #绩点是否大于0

        for row in reader:
            if row[2]=="是":
                list1.append(1)
            else:
                list1.append(0)

            if row[3]>"3.0":
                list2.append(1)
            else:
                list2.append(0)

        length = 90
        fenmu = 0.000
        fenzi = 0.000
        # for i in range(length):
        #     print(list1[i],list2[i])

        list3=[0 for i in range(90)]
        list4=[0 for i in range(90)]
        list5=[0.000000 for i in range(90)]

        a=float(input())
        b=float(input())
        c=float(input())
        d=float(input())

        e=int(input())
        f=int(input())

        list7=[0.0 for i in range(90)]

        print(list1)
        print(list2)


        for i in range(e):
            for j in range(length-8):
                random.seed()
                num=random.random()
                list7[j]=num

                #print(num)
                if list1[j]==1:
                    if list2[j]==1:
                        if num<a:
                            list3[j]=0
                        else:
                            list3[j]=1
                    else:
                        if num<b:
                            list3[j]=0
                        else:
                            list3[j]=1
                else:
                    if list2[j]==1:
                        if num<c:
                            list3[j]=0
                        else:
                            list3[j]=1
                    else:
                        if num <d:
                            list3[j] = 0
                        else:
                            list3[j] = 1


                list4[j]=list4[j]+list3[j]

                if list3[j] == 0:
                    fenzi+=1

                list5[j]=list4[j]/(i+1)


            for j in range(82,90):
                random.seed()
                num=random.random()
                list7[j] = num
                if num<0.8:
                    list3[j]=0
                else:
                    list3[j]=1

                list4[j]=list4[j]+list3[j]

                if list3[j] == 0:
                    fenzi+=1

                list5[j]=list4[j]/(i+1)

            print(list7)
            print(list4)

        fenmu=e*60

        #print(list5)

        list6=np.argsort(list5)
        print(list6)
        list6=list6[:8]
        print(list6)

        for i in range(e,100):
            fenmu+=8
            random.seed()
            for j in range(length - 8):
                num = random.random()
                # print(num)
                if list1[j] == 1:
                    if list2[j] == 1:
                        if num < a:
                            list3[j] = 0
                        else:
                            list3[j] = 1
                    else:
                        if num < b:
                            list3[j] = 0
                        else:
                            list3[j] = 1
                else:
                    if list2[j] == 1:
                        if num < c:
                            list3[j] = 1
                        else:
                            list3[j] = 0
                    else:
                        if num < d:
                            list3[j] = 1
                        else:
                            list3[j] = 0

                list4[j] = list4[j] + list3[j]

                list5[j] = list4[j] / (i + 1)
                # print(list5[j])

            for j in range(82, 90):
                num = random.random()
                if num < 0.8:
                    list3[j] = 0
                else:
                    list3[j] = 1

                list4[j] = list4[j] + list3[j]

                list5[j] = list4[j] / (i + 1)

            for j in range(8):
                if list3[list6[j]]==0:
                    fenzi+=1

            fenmu+=f
            for j in range(f):
                num = random.randint(0,80)
                if list3[num]==0:
                    fenzi+=1

        print(list5)
        rating=fenzi/fenmu
        #print(list5)
        print(rating)

main()
