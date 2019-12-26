#  File: friends.py
#  Description: creating facebook type application with linked lists
#  Student's Name: David Chase Weaver
#  Student's UT EID: dcw2269
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: April 11, 2019
#  Date Last Modified: April 11, 2019


#Node class taken from class website
class Node:

    def __init__(self,initData):
        self.data = initData
        self.next = None
        
    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext

#Unordered list class taken from class website
class UnorderedList:

    def __init__(self):
        self.head = None
    
    #Str method to properly print out friends list in main program    
    def __str__(self):
        current = self.head
        outStr =  "    [ "
        while current != None:
            
            outStr += str(current.getData()) + " "
            current = current.getNext()
        outStr += "] \n"
        return outStr

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self,item):

        found = False
        current = self.head

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):

        found = False
        previous = None
        current = self.head

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    #New method to search for friend in friends list
    def searchFor(self, item):
        found = False
        current = self.head
        
        while current != None and not found:
            
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                
        if found:
            return current
        else:
            return None
        

class User:
    
    def __init__(self, name, userList):
        
        self.name = name
        self.friends = UnorderedList()
        userList.add(self)
        print("    " + name + " now has an account.\n")
        
    def __str__(self):
        return self.name
    
    def __eq__(self,other):
        
        return self.name == other
    
    
def main():
    
    #Open file containing the data on the friends
    inFile = open("FriendData.txt", "r")
    
    userList = UnorderedList()
    
    line = inFile.readline()
    
    
    while line != "":
        
        line = line.split()
        
        #Checks to see if adding an account for a person
        if line[0] == "Person":
            print("--> Person " + line[1])
        
            if userList.search(line[1]):
                print("    A person with name " + line[1] + " already exists. \n")
    
    
            else:
                User(line[1], userList)
        
        #Checks to see if adding a friend
        elif line[0] == "Friend":
            
            print("--> Friend " + line[1] + " " + line[2])
            
            
            #Creates variables that refer to users' nodes
            user1 = userList.searchFor(line[1])
            user2 = userList.searchFor(line[2])
            
            #Checks to see if user exists
            if user1 == None or user2 == None:
                
                if user1 == None:
                    print("    A person with the name " + line[1] + " does not currently exist. \n")
                if user2 == None:
                    print("    A person with the name " + line[2] + " does not currently exist. \n")
                
                line = inFile.readline()
                continue
            
            #Checks to see if person is trying to add themselves
            if line[1] == line[2]:
                print("    A person cannot friend him/herself \n")
                line = inFile.readline()
                continue
            
            #Checks to see if person is already in friends list
            if user1.getData().friends.search(user2):
                print("    " + line[1] + " and " + line[2] + " are already friends. \n")
                line = inFile.readline()
                continue
            
            #Add each other to both users' friends list
            user1.getData().friends.add(user2)
            user2.getData().friends.add(user1)
            
            print("    " + line[1] + " and " + line[2] + " are now friends. \n")
            
            
            
        elif line[0] == "Unfriend":
            
            print("--> Unfriend " + line[1] + " " + line[2])
            
            
            #Creates variables that refer to users' nodes
            user1 = userList.searchFor(line[1])
            user2 = userList.searchFor(line[2])
            
            #Checks to see if user exists
            if user1 == None or user2 == None:
                
                if user1 == None:
                    print("    A person with the name " + line[1] + " does not currently exist. \n")
                if user2 == None:
                    print("    A person with the name" + line[2] + " does not currently exist. \n")
                
                line = inFile.readline()
                continue
            
            #Checks to see if person is trying to add themselves
            if line[1] == line[2]:
                print("    " + line[1] + " cannot unfriend him/herself. \n")
                line = inFile.readline()
                continue
            
            #Checks to see if person is already in friends list
            if not user1.getData().friends.search(user2):
                print("    " + line[1] + " and " + line[2] + " aren't friends, so you can't unfriend them. \n")
                line = inFile.readline()
                continue
            
            #removes each other from friend lists 
            user1.getData().friends.remove(user2)
            user2.getData().friends.remove(user1)
            
            print("    " + line[1] + " and " + line[2] + " are no longer friends. \n")
            
            
        elif line[0] == "List":
            
            print("--> List " + line[1])
            
            #cretes variables that can refer to users node
            user1 = userList.searchFor(line[1])
            
            if user1 == None:
                print("    " + line[1] + " doesn't have an account.\n")
                
            elif user1.getData().friends.isEmpty():
                print("    " + line[1] + " has no friends.\n")
                
            else:
                print(user1.getData().friends)
                
                
        elif line[0] == "Query":
            
            print("--> Query " + line[1] + " " + line[2])
            
            
            #Creates variables that refer to users' nodes
            user1 = userList.searchFor(line[1])
            user2 = userList.searchFor(line[2])
            
            #Checks to see if user exists
            if user1 == None or user2 == None:

                
                if user1 == None and line[1] == line[2]:
                    print("    A person cannot query with him/herself. \n")
                elif user1 == None:
                    
                    print("    A person with the name " + line[1] + " does not currently exist. \n")
                    
                if user2 == None and line[1] != line[2]:
                    print("    A person with the name " + line[2] + " does not currently exist. \n")
                
                #continue loop
                line = inFile.readline()
                continue
    
    
            #checks to see if user is querying self
        
            # If the users are friends
            if user1.getData().friends.search(user2):
                print("    " + line[1] + " and " + line[2] + " are friends.\n")

            # If the users are not friends
            else:
                print("    " + line[1] + " and " + line[2] + " are not friends.\n")
                
                
        # Checks if exiting
        elif line[0] == "Exit":

            print("--> Exit \n    Exiting...")
            break
            
        line = inFile.readline()


        try:
            user1 = userList.searchFor("Ross")
            print(type(user1.friends))
        except:
            pass
        
        
        
        
        
main()



    
        
