print 5
Time=0
print "enter the no of processes:"
No_ofprocesses=int(input())
processes=[]
BurstTime=[]
RemainingBurstTime=[]
AvgWaitingTime=[]
WaitingTime=[]
AvgTurnAroundTime=0
print "enter the Time slice"
TimeSlice=int(input())
print "Enter the burt time of each process: (space separated)"
BurstTime=list(map(int,raw_input().split()))

for i in range(0,No_ofprocesses):
    processes.insert(i,i+1)
RemainingBurstTime=BurstTime
while(1):
    end=True
    for i in range(0,No_ofprocesses):
        if(RemainingBurstTime[i]>TimeSlice):
            Time=Time+TimeSlice
            RemainingBurstTime[i]=RemainingBurstTime[i]-TimeSlice
        else:
            Time=Time+RemainingBurstTime[i]
            WaitingTime[i]=Time-BurstTime[i]
            RemainingBurstTime[i]=0
    if(end==True):
        break



for i in range(0,No_ofprocesses-1):
    print str(WaitingTime[i])




