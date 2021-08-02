import csv
with open('D:/python/class104/height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    #csv.reader()reads the current row and moves to the next.
    file_data=list(reader)
    #list(reader) add data to the list 

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))
    #create a empty list name new_data
    #use forloop on file_data to get the element 
    #append the height column to new_data list 

n=len(new_data)
new_data.sort()

if n%2==0:
    median1=float(new_data[n//2])
    #using floor division to get nearest whole number 
    # floor division is shown by //
    median2=float(new_data[n//2 -1])
    median=(median1+median2)/2

else:
    median=new_data[n//2]

print("median is : "+str(median))    
#output median is : 67.9957
#example
#2,5,7,3,9,4
#2,3,4,5,7,9
#n=6
#n//2=3....median1=5
#median=4
#median=(4+5)/2

