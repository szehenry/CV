#. Input/store/update/retrieve the income(s), spendings and other allocations
# the first column is time,2 is amount, 3 is type
def main():
    fp = open('amount.csv','r')
    content = fp.readlines()
    print(content,len(content))
    fp.close
    update()
    #input_income()

def retrieve():
    '''
    This function is for finding the data set while given the key word.
    It will return the data set and the index of the string.
    '''
    stat = input('What related data you have?\n Please enter 2 if you have the date.\n Please enter 3 if you have the amount\n Please enter 4 if you have the type\n')
    fp = open('amount.csv','r')
    content = fp.readlines()
    len_fp = len(content)
    j = 0
    temp_str = [0,0,0,0,0,0]
    temp_index = [0,0,0,0,0,0]
    #print(stat)
    if stat == '2':
        #print('hello')
        temp_date = input("please input the date:   ")
        for i in range(len_fp):
            index = content[i].find(temp_date)
            if index != -1:
                temp_str[j] = content[i]
                temp_index[j] = i
                j += 1

    elif stat == '3':
        #print('hello')
        temp_amo = str(input("please input the amount:  "))
        for i in range(len_fp):
            index = content[i].find(temp_amo)
            if index != -1:
                temp_str[j] = content[i]
                temp_index[j] = i
                j += 1

    elif stat == '4':
        #print('hello')
        temp_type = input("please input the type:   ")
        for i in range(len_fp):
            index = content[i].find(temp_type)
            if index != -1:
                temp_str[j] = content[i]
                temp_index[j] = i
                j += 1
    #print(j,'aaaaa',temp_str)
    fp.close
    a = 0
    if j>1:
        print('Please enter the number that you want the set:   ')
        for a in range(j) :
            print(a+1,')',temp_str[a])
        temp_num = int(input())
        return temp_str[temp_num-1],temp_index[temp_num-1]
    else:
        print("This is the data:",temp_str[0])
        return temp_str[0],temp_index[0]
        #temp_num = input()
    
def update():
    '''
    It is for update the data set while using retrieve to find the data set
    '''
    str , index = retrieve()
    #print(str,index)
    change_str = input("Please type the whole set that you need to update(split with ','):")
    fp = open('amount.csv','r')
    content = fp.readlines()
    #print(content)
    fp.close
    fp = open('amount.csv','w')
    len_fp = len(content)
    content[index]= change_str
    for i in range(len_fp):
        fp.write(content[i])
    fp.close
    print('Updated')
        

def input_income():
    '''
    It is for input the data to data set.
    
    
    '''

    fp = open('amount.csv','a')
    date  = input('Please input in the data of the amount : date:')
    cost = input('Amount(if it is a spending, please add "-" in the input.)')
    type_c = input('Type:')
    fp.write(date)
    fp.write(',')
    fp.write(cost)
    fp.write(',')
    fp.write(type_c)
    fp.write('\n')
    fp.close
    

update()