import subprocess, time

def commands(commands_list):
    start_time = time.time()

    end_output = []
    completed = []
    timing = []

    #Initiate the processes/commands
    for x in commands_list:
        sub_command = x.split(" ")
        end_output.append(subprocess.Popen(sub_command))
        completed.append(False)
        timing.append(time.time())

    # Checking to make sure all the commands ae completed
    completed_commands = 0
    index = 0
    while(completed_commands < len(commands_list)):
        #Reset the index number when it overflows.
        if(index == len(commands_list)):
            index = 0

        #Collect and count the completed commands
        if(end_output[index].poll() != None and completed[index] == False):
            timing[index] = time.time() - timing[index]
            completed_commands += 1
            completed[index] = True
        index += 1


    #User Report
    print("Average time:\t", sum(timing)/len(timing))
    print("Minimum time:\t", min(timing))
    print("Maximum time:\t", max(timing))
    print("Total time:\t", time.time() - start_time)




def main():
    commands([
    'sleep 3',
    'ls -l /',
    'find /',
    'sleep 4',
    'find /usr',
    'date',
    'sleep 5',
    'uptime'
    ])

if __name__ == '__main__':
    main()
