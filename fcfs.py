BurstTime=[]  
WaitingTime=[]    
AvgWaitingTime=0  
TurnAroundTime=[]    
AvgTurnAroundTime=0     
print("Enter the number of process: ")
n=int(input())
processes=[]
for i in range(0,n):
 processes.insert(i,i+1)
print("Enter the burst time of the processes: \n")
BurstTime=list(map(int, raw_input().split()))
print "\n"
print "sorted processes: "
print processes
print "Sorted burst time: "
print BurstTime

#now its simple as First come First Serve(FCFS)
WaitingTime.insert(0,0)
TurnAroundTime.insert(0,BurstTime[0])
for i in range(1,len(BurstTime)):  
 WaitingTime.insert(i,WaitingTime[i-1]+BurstTime[i-1])
 TurnAroundTime.insert(i,WaitingTime[i]+BurstTime[i])
 AvgWaitingTime+=WaitingTime[i]
 AvgTurnAroundTime+=TurnAroundTime[i]
AvgWaitingTime=float(AvgWaitingTime)/n
AvgTurnAroundTime=float(AvgTurnAroundTime)/n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
 print(str(processes[i])+"\t\t"+str(BurstTime[i])+"\t\t"+str(WaitingTime[i])+"\t\t"+str(TurnAroundTime[i]))
 print("\n")
print("Average Waiting time is: "+str(AvgWaitingTime))
print("Average Turn Arount Time is: "+str(AvgTurnAroundTime))

