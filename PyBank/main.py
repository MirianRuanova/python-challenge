import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    months = 0
    profit_losses_list = []
    dates_list =[]
    for row in csvreader:
        months += 1 #months=months+1
        dates_list.append(row[0])
        profit_losses_list.append(int(row[1]))
        print(row)

    print("Total number of months:", months)
    #print(dates_list)
    #print(profit_losses_list)

    #Calculate the net total amount in "Profit/Losses" over the entire period.
    revenue = 0 
    for i in profit_losses_list:
        revenue = revenue + i
    print("Total revenue:   ", revenue)
    
    print("Total revenue B: "+str(sum(profit_losses_list)))

    #Calculate the changes in "Profit/Losses" over the entire period.
    #Create a list to store all the changes.
    sum_change_list=[]
    sum_change= 0 
    for i in (range(len(profit_losses_list)-1)):
        sum_change= profit_losses_list[i+1] - profit_losses_list[i]
        print(sum_change)
        sum_change_list.append(sum_change)
    print("This is sum_change_list:   ", sum_change_list)

    average_change= 0
    for i in sum_change_list:
        average_change= average_change + i
    average_change=average_change/len(sum_change_list)
    print("This is the average change:   ", average_change)
 
    average_change2=sum(sum_change_list)/len(sum_change_list)
    print("This is the average (B) "+str(average_change2))

   

    del dates_list[0]
    print("This is the new Dates List:  ", dates_list)

    dates_profit_losses_list = list(zip(dates_list,sum_change_list))
   

    for i in dates_profit_losses_list:
        print(i)

    max_profits=0
    max_month=''
    
    min_profits=0
    min_month=''

    for x in dates_profit_losses_list:
        if x[1]>max_profits:
            max_profits=x[1]
            max_month=x[0]

        if x[1]<min_profits:
            min_profits=x[1]
            min_month=x[0]
    
    #greatest_increase=max(dates_profit_losses_list)
    #greatest_decrease=min(dates_profit_losses_list)

    print("Greatest Increase in Profits: ", max_profits, " in month ", max_month)
    print("Greatest Decrease in Profits: ", min_profits, " and month ", min_month)

output_file=os.path.join("analysis","output.txt")
with open(output_file,"w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("____________________________________________\n")
    datafile.write("Total Months: " + str(months) + "\n")
    datafile.write("Average Change: " + str(average_change) + "\n")
    datafile.write("Greatest Increase in Profits: " + str(max_month) + " "+ "($"+str(max_profits) +")" "\n")
    datafile.write("Greatest Decrease in Profits: " +  str(min_month) + " "+ "($"+ str(min_profits) +")" "\n")
 






    


   
    

    
  
    


  



  



