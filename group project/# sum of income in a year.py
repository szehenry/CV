# sum of income in a year
    
    
    
    
    date = input("please enter date of today(split day, month and year with ','): ")

    
    
    
    
    
    sum = []

    for j in temp_date:
        if temp_date[2] == date[2]:
            sum.append(temp_amo[j])
        elif temp_date[1] == date[1] & temp_date[2] == (date[2] -1) & temp_date[0] >= date[0]:
            sum.append(temp.amo[j])
        
        



#find top three spendings
    top_spend = []
    temp_type = list(set(temp_type))

