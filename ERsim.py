#  File: ERsim.py
#  Description: Use Queues to sort and treat patients in an emergency room in order from most to least severe
#  Student's Name: David Chase Weaver
#  Student's UT EID: dcw2269
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: March 14, 2019
#  Date Last Modified: March 15, 2019

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    #define str method to properly print out queues
    def __str__(self):
        return str(self.items)  

#function to add patient to queue
def addPatient(command):
    #split text file into separate words
    splitStr = command.split()
    
    #if statements to treat each condition separately 
    if splitStr[2] == "Critical":
        critical.enqueue(splitStr[1])
        print("Add patient " + splitStr[1] + " to critical queue")
        
    elif splitStr[2] == "Serious":
        serious.enqueue(splitStr[1])
        print("Add patient " + splitStr[1] + " to serious queue")
        
    elif splitStr[2] == "Fair":
        fair.enqueue(splitStr[1])
        print("Add patient " + splitStr[1] + " to fair queue")
        
    print("Queues are:")
    print("Fair: " + str(fair))
    print("Serious: " + str(serious))
    print("Critical: "+ str(critical) + "\n")
    
    
def treatNext():
    
    if not critical.isEmpty(): 
        patient = critical.dequeue()
        print("Treating " + patient + " from Critical queue")
        print("Queues are:")
        print("Fair: " + str(fair))
        print("Serious: " + str(serious))
        print("Critical: " + str(critical) + "\n")
        
    elif not serious.isEmpty():
        patient = serious.dequeue()
        print("Treating " + patient + " from Serious queue")
        print("Queues are:")
        print("Fair: " + str(fair))
        print("Serious: " + str(serious))
        print("Critical: " + str(critical) + "\n")
        
    elif not fair.isEmpty():
        patient = fair.dequeue()
        print("Treating " + patient + " from Fair queue")
        print("Queues are:")
        print("Fair: " + str(fair))
        print("Serious: " + str(serious))
        print("Critical: " + str(critical) + "\n")
        
    # all queues are empty    
    else:  
        print("No patients in queues \n")
        
def treatAll():
    while True:
        
        # if there is still patient in any queue, treat next patient
        if not (critical.isEmpty() and serious.isEmpty() and fair.isEmpty()):
            treatNext()
        # if not, end the loop
        
        else:
            print("No patients in queues \n")
            break       
        




def main():
    
#tell program to read text file containing patient data
    file = open("ERsim.txt", "r")
    lines = file.readlines()

    #make the 3 conditions global variables so that they can be accessed in other functions
    global critical
    global fair
    global serious
    
    #Create 3 empty queues
    fair = Queue()
    critical = Queue()
    serious = Queue()
    
    for command in lines: # process each line
        command = command.strip() # get rid of trailing whitespaces
        
        # the add process
        if (command[0:3] == "add"):
            addPatient(command)

        # the treat next process
        elif (command == "treat next"):
            print("Treat next patient\n")
            treatNext()

        # the treat all process
        elif (command == "treat all"):
            print("Treat all patients\n")
            treatAll()

        # the exit process
        elif (command == "exit"):
            print("Exit")
            
            
main()
