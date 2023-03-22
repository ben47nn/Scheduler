####TO DO:
    #--Done--time_printconvert
    #--DONE--sort day !!!! 
    #--starting--write to specific day
    #List Comprehension
    #Clean up the very mesy code
import numpy
import calendar
from datetime import date
def data_sorter():
    f=open("day.txt","r")
    unsort=(f.readlines())
    f.close()
    i=0
    while i < len(unsort):
        unsort[i]=unsort[i].rstrip("\n")
        i+=1
    times=unsort
    tasks=[]
    tasks=unsort
    i=0
    mark1=0
    while i <len(times):
        g=0
        while i <len(times[i]):
            mark1=times[i]
            if mark1[g]==",":
                times[i]=mark1[g+1:]
                break
            g+=1
        i+=1
    i=0
    mark1=0
    while i <len(times):
        g=0
        while i <len(times[i]):
            mark1=times[i]
            if mark1[g]==",":
                times[i]=mark1[:g]
                break
            g+=1
        i+=1
    i=0
    while i < len(times):
        times[i]=times[i].translate({ord(':'): None})
        i+=1
    f=open("day.txt","r")
    tasks=(f.readlines())
    
    def bubble_sort(array,list1):#sort tasks based on filtered times
        n=len(array)
        for i in range(n-1):
            already_sorted=True
            for j in range(0, n-i-1):
                if int(array[j]) > int(array[j+1]):
                    array[j], array[j+1]=array[j+1], array[j]
                    list1[j],list1[j+1]=list1[j+1], list1[j]
                    already_sorted=False

            if already_sorted:
                break
        return(tasks)
    for count, task in enumerate(tasks):##setup list comprehension
        if task[-1:] != '\n':
            tasks[count]+='\n'
    if tasks[-1:][-1:]=='\n':
        bubble_sort(times,tasks)
    g = open("day.txt","w") 
    g.writelines(tasks)  #write sorted tasks to day.txt
    g.close()
    
def day_write(str1):#open txt file to store task data
    
    g=open("day.txt","a")
    f=open('day.txt','r')
    if f.read()=='':#if first line is empty dont write a new line
        g.write(str1)
        g.close()
    else:
        #g.write("\n")
        g.write(str1)
        g.close()

def time_dataconvert(str1):#converts to military time
    hour=str1[:-5]
    if str1[-2:]=="am":
      str1=str1[:-2]
    elif str1[-2:]=="pm":
        if hour=="12":
            str1=str1[:-2]
        elif str1[1:2]==":":
            str1=str(int(str1[:1])+12)+str1[1:4]
        else:
            str1=str(int(str1[:2])+12)+str1[2:5]
    else:
        print("Error Incorrect Time Given")
    return(str1)

def time_convert(str1):#converts to civ time
   str1=str1[:-1]
   str1=str1.split(",")
   start_time=str1[1].split(":")
   end_time=str1[2].split(":")

   if int(start_time[0])>11:#check if starting time is greater than 12pm
       if int(end_time[0])>11:
            if start_time[0]=="12":#check if start time is 12
               str1[1]=start_time[0]+":"+start_time[1]+"pm"
               if end_time[0]=="12":#check if end time is 12
                  str1[2]=end_time[0]+":"+end_time[1]+"pm"
               else:
                  str1[2]=str(int(end_time[0])-12)+":"+end_time[1]+"pm"
            else:
               str1[1]=str(int(start_time[0])-12)+":"+start_time[1]+"pm"
               if end_time[0]=="12":
                  str1[2]=end_time[0]+":"+end_time[1]+"pm"
               else:
                  str1[2]=str(int(end_time[0])-12)+":"+end_time[1]+"pm"
               
            str1=(str1[0]+" "+str1[1]+"-"+str1[2])
       else:
            if start_time[0]=="12":#check if start time is 12
               str1[1]=start_time[0]+":"+start_time[1]+"pm"
            else:
               str1[1]=str(int(start_time[0])-12)+":"+start_time[1]+"pm"
            str1=(str1[0]+" "+str1[1]+"-"+str1[2]+"am")

   elif int(end_time[0])>11 and int(start_time[0])<12:#check if end time is greater than 12pm
      if end_time[0]=="12":#check if end tim is 12
            str1[2]=end_time[0]+":"+end_time[1]+"pm"
      else:
            str1[2]=str(int(end_time[0])-12)+":"+end_time[1]+"pm"
      str1=(str1[0]+" "+str1[1]+"am-"+str1[2])
     
   else:    
       str1=(str1[0]+" "+str1[1]+"am"+"-"+str1[2]+"am")
   print(str1)

def get_date(date):#give a date and it will find where that date is located
    return

def add_today(): #adds task to the txt file
    #write day before adding tasks
    #find date before adding task
    today = date.today()
    task=str(input("Task: "))#get data input
    time1=str(input("Time Start[EX: 8:45am]: "))
    time2=str(input("Time End[EX: 8:45pm]: "))
    tt=[]
    tt.append(task+ "," + time_dataconvert(time1) +","+ time_dataconvert(time2))
    day_write(tt[0])#add data to txt file
    global Sorted
    Sorted=False
    
def task_print():
    data_sorter()#Very very slow to run evey time
    e=open("day.txt","r")
    milTime=(e.readlines())
    for i in milTime:#prints out all tasks in civ time
        time_convert(i)

def task_close():
   with open('day.txt', 'w'):
       pass
      
clause=True
while clause:
    print("################################")
    print("0:Leave task menu")
    print("1:Add Task today")
    print("2:Add Task on specific date")
    print("3:Print all tasks")
    print("4:Clear all data")
    choice=int(input(f"Pick an option: "))
    print("################################")
    if choice==1:
        add_today()
    elif choice==0:
        clause=False
    elif choice==3:
        task_print()
    elif choice==4:
        task_close()


