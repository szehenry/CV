
'''open csv. file, user first input the date of today, classify the data, put them into different list, sum up users income in a year, print out users income within a year'''


date = input("please enter date of today(split day, month and year with ','): ").split(',')

def sum_income():  
    # sum of income in a year
    fp = open('amount.csv','r')
    content = fp.readlines()
        
        
       
    
    # date = input("please enter date of today(split day, month and year with ','): ").split(',')
    # print(date)

    date_list = []
    amo_list = []
    type_list = []

    for i in range(len(content)):
        temp = content[i][:-1].split(",")
        date_list.append(temp[0])
        amo_list.append(int(temp[1]))
        type_list.append(temp[2])
    # print(date_list,"\n", amo_list,"\n", type_list )
    # print(type(date_list))


    temp_date_list = []
    for k in range(0,len(date_list)):
        temp_date_list.append(date_list[k].split("/"))
    # print(temp_date_list)

    sum_list = []

    for j in range(len(temp_date_list)):
        # print(temp_date_list[j][2],'\n',date[2])
        
        # print( int(temp_date_list[j][2])==(int(date[2]) -1) and int(temp_date_list[j][1])>int(date[1]) and type_list=="income")
        # print(int(temp_date_list[j][1]), '\n',int(date[1]))

        # print(int(temp_date_list[j][0]), '\n',int(date[0]))
        
        if int(temp_date_list[j][2])==int(date[2]) and int(temp_date_list[j][1])<int(date[1]) and type_list[j]=="income":
            # print('hello',amo_list[j])
            sum_list.append(amo_list[j])
        elif int(temp_date_list[j][2])==int(date[2]) and int(temp_date_list[j][1])==int(date[1]) and int(temp_date_list[j][0]) <= int(date[0]) and type_list[j]=="income":
            sum_list.append(amo_list[j])

        elif int(temp_date_list[j][1])==int(date[1]) and int(temp_date_list[j][2])==(int(date[2]) -1) and int(temp_date_list[j][0]) >= int(date[0]) and type_list[j]=="income":
            sum_list.append(amo_list[j])
        elif int(temp_date_list[j][2])==(int(date[2]) -1) and int(temp_date_list[j][1])>int(date[1]) and type_list[j]=="income":
            

            sum_list.append(amo_list[j])
    Sum = sum(sum_list)
    # print(temp_date_list[0][0])
    print("Your total income last year is ", Sum)

    return temp_date_list,amo_list,type_list

   


temp_date_list,amo_list,type_list = sum_income()            




def myMax(list):
    '''
    Take the list which we want to find the maximum number.
    Compare the number in the list one by one.
    When finding a larger number in the comparison, use the larger number to compare next time.
    looping these processes until all the numbers in the list are compared.
    return the maximum number, the length of the list, and the position of the maximum stared at 0.
    '''
    i = 0
    
    max = list[0]
    list_len = len(list)
    while (i < list_len):
        if (list[i] > max):
            max = list[i]
            
        i += 1
    return max



'''user first type in date of today, the function will find spendings from the last 30 days, and list out the type and amount of the top three spendings in the last 30 days'''



def top_three_spend(temp_date_list,amo_list,type_list):
    
    date = input("please enter date of today(split day, month and year with ','): ").split(',')
    # print(date[0], date[1], date[2])
    new_type_list = []
    new_amo_list = []
    # print("hello0")
    
    for i in range(len(type_list)):
        
        # print(type_list[i] != "income" and ((temp_date_list[i][2]==date[2] and temp_date_list[i][1]==date[1] and int(temp_date_list[i][0])<=int(date[0])) or (temp_date_list[i][2]==date[2] and int(temp_date_list[i][1])==(int(date[1])-1) and int(temp_date_list[i][0])>=int(date[0]))))
        # print("hello1")

        if type_list[i] != "income" and ((temp_date_list[i][2]==date[2] and temp_date_list[i][1]==date[1] and int(temp_date_list[i][0])<=int(date[0])) or (temp_date_list[i][2]==date[2] and int(temp_date_list[i][1])==(int(date[1])-1) and int(temp_date_list[i][0])>=int(date[0]))):
            
            
            # print("hello2")
            new_type_list.append(type_list[i])
            new_amo_list.append(amo_list[i])
        
        
        
        elif date[1]=="1":
            # print("Hello")
            if type_list[i] != "income" and int(temp_date_list[i][2])==(int(date[2])-1) and int(temp_date_list[i][1])==int(12) and int(temp_date_list[i][0])>=int(date[0]):
                
                # print("hello3")
                # print("Helllo")
                new_type_list.append(type_list[i])
                new_amo_list.append(amo_list[i])
    
    # print(new_type_list, '\n', new_amo_list)

    real_type_list = list(set(new_type_list))

    real_amo_list = []
    X = []
    temp1 = 0
    

    for j in range(len(real_type_list)):
        for n in range(len(new_type_list)):
            if new_type_list[n] == real_type_list[j]:
                real_amo_list.append(new_amo_list[n])
        temp1 = sum(real_amo_list)
        X.append(temp1)
        real_amo_list = []
        temp1 = 0
    # print(real_type_list)
    # print(X)
    # print("hi")


    N = len(X)
    I = 1
    for j in range(0,3):
        for k in range(0, len(X)):
        
            if X[k] == myMax(X):
                print("The ", I, "spending is ", real_type_list[k], "$", X[k])
                # print(X[k])
                X[k] = 0
                I += 1
                break
            
        


        


    
# find top three spendings
#     top_spend = []
#     temp_type = list(set(temp_type))




# & int(temp_date_list[j][1])<=int(date[1])

top_three_spend(temp_date_list,amo_list,type_list)



