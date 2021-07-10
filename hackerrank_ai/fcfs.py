'''
FCFS: First Come First Serve
The task is to find the Average Waiting Time and Average Turnaround Time of the given processes with their Burst Time using FCFS Scheduling Algorithm.
FCFS is the simplest Scheduling Algorithm. It simply serves a process in order that they arrive in the Ready Queue.
FCFS is a Non Pre-emptive Algorithm, hence the process which comes first will be executed first and the next process will be served only after the previous process is executed completely.
Start Time: Time at which the execution of the process starts
Completion Time: Time at which the process completes its execution
Turnaround Time: Completion Time - Arrival Time
Waiting Time: Turnaround Time - Burst Time
'''


class FCFS:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Enter Process ID: "))

            arrival_time = int(input("Enter Arrival Time: "))

            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))

            temporary.extend([process_id, arrival_time, burst_time])
            process_data.append(temporary)
        FCFS.schedulingProcess(self, process_data)

    def process_data(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            a = input().split(' ')
            temporary.extend([a[0], int(a[1]), int(a[2])])
            process_data.append(temporary)
        FCFS.schedulingProcess(self, process_data)

    '''
    Sort according to Arrival Time
    '''
   
    def schedulingProcess(self, process_data):
        process_data.sort(key=lambda x: x[1])
        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(process_data)):
            if s_time < process_data[i][1]:
                s_time = process_data[i][1]
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            e_time = s_time
            exit_time.append(e_time)
            process_data[i].append(e_time)
        t_time = FCFS.calculateTurnaroundTime(self, process_data)
        w_time = FCFS.calculateWaitingTime(self, process_data)
        FCFS.printData(self, process_data, t_time, w_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][3] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][4] - process_data[i][2]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time):

        print("Process_ID \t\tArrival_Time \t\tBurst_Time \t Completion_Time \t Turnaround_Time \t Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t\t\t")
            print()
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')


if __name__ == "__main__":

    no_of_processes = int(input())

    fcfs = FCFS()
    fcfs.process_data(no_of_processes)
