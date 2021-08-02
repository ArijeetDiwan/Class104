import csv
with open('D:/python/class104/height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    #csv.reader()reads the current row and moves to the next.
    file_data=list(reader)
    #list(reader) add data to the list 

file_data.pop(0)
#to remove the title from the data 
#print(file_data)


new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))
    #create a empty list name new_data
    #use forloop on file_data to get the element 
    #append the height column to new_data list 

n=len(new_data)
total=0
for x in new_data:
    total+=x

mean= total/n
print('mean/average is : '+str(mean))
#output mean/average is : 67.99311359679979