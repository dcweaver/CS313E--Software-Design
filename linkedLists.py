#  File: LinkedLists.py
#  Description: Create generic linked list class to be able to manipulate any kind of linked list
#  Student's Name: David Chase Weaver
#  Student's UT EID: dcw2269
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: March 27, 2019
#  Date Last Modified: March 29, 2019


class Node:

    def __init__(self,initData):
        self.data = initData
        self.next = None
        
    #create str method to properly print node 
    def __str__(self):
        
        return self.data
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext

############################################################################
class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items[-1]

   def size (self):
      return len(self.items)
###################################################################
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.count = 0
        
    def __str__(self):
        outStr = ""
        outNum = 0
        current = self.head
        #take into account 10+ size lists
        while current != None:
            
            if outNum % 10 == 0 and outNum != 0:
                outStr += "\n"
            
            outStr += (str(current) + "  ")
            current = current.getNext()
            outNum += 1
            
        
        
        return outStr
        
    def addFirst(self, item):
        
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.count += 1


    def addLast(self, item):
        self.count += 1
        #has it start at first node
        current = self.head

        if current == None:
            self.addFirst(item)
            return
            
        while current.getNext() != None:
            current = current.getNext()

        current.setNext(Node(item))
        

    def addInOrder(self, item): #used ordered list method defined in class 

        self.count += 1
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        temp.setNext(current)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    def getLength(self):
        
        return self.count

    def findUnordered(self,item): #taken from unordered list class already created
        
        found = False
        current = self.head
        count = 0

        while current != None and not found:
            count += 1

            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def findOrdered(self, item):
        found = False
        stop = False    # we've passed the place where it should be
        current = self.head
        count = 0

        while current != None and not found and not stop:
            count += 1
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def delete(self, item):
        self.count -= 1
        previous = None
        current = self.head
        while current:
            if current.getData() == item:
                if previous:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                return True
                    
            previous = current
            current = current.getNext()
            
        return False

    def copyList(self):

        current = self.head
        newList = LinkedList()
        while current != None:

            newList.addLast(current.getData())
            current = current.getNext()
        return newList



    def reverseList(self):

        current = self.head

        newList = LinkedList()

        listStack = Stack()
        
        while current != None:

            listStack.push(current.getData())

            current = current.getNext()

        while not listStack.isEmpty():

            newList.addLast(listStack.pop())
            
        return newList

    def orderList(self):

        current = self.head

        newList = LinkedList()

        while current != None:

            newList.addInOrder(current.getData())
            current = current.getNext()
            
        return newList

    def isOrdered(self):

        sCurrent = self.head

        newList = self. orderList()

        oCurrent = newList.head

        #uses XOR logic operator to determine if one of the lists is empty
        if self.isEmpty() ^ newList.isEmpty():
            return False

        #Traverse the linked list
        while sCurrent != None or oCurrent != None:

            if sCurrent.getData() == oCurrent.getData():

                sCurrent = sCurrent.getNext()
                oCurrent = oCurrent.getNext()
            else:
                return False

        return True

    def isEmpty(self):
        #if head is empty, linked list is empty
        return self.head == None


    def mergeList(self, b):

        sCurrent = self.head
        bCurrent = b.head

        newList = LinkedList()
        #Traverse list
        while sCurrent != None or bCurrent != None:
            #if self's node isnt empty add node in order into new list
            if sCurrent != None:
                newList.addInOrder(sCurrent.getData())
                sCurrent = sCurrent.getNext()
            #if b's node isnt empty, add node in order into the new list   
            if bCurrent != None:
                newList.addInOrder(bCurrent.getData())
                bCurrent = bCurrent.getNext()
        
        return newList




    def isEqual(self, item):
        sCurrent = self.head
        bCurrent = item.head

        # Traverses both lists
        while sCurrent != None or bCurrent != None:

            # Uses XOR logic operator to determine if only one of the nodes equals none
            if (sCurrent == None) ^ (bCurrent == None):
                return False
            
            # Checks to see if equal
            if sCurrent.getData() == bCurrent.getData():
                sCurrent = sCurrent.getNext()
                bCurrent = bCurrent.getNext()

            # Otherwise return False
            else:
                return False

        return True

    def removeDuplicates(self):

        current = self.head

        # Creates new linked list
        newList = LinkedList()

        # Traverses original list
        while current != None:

            # If current node isn't in the new linked list, add it
            if not newList.findUnordered(current.getData()):
                newList.addLast(current.getData())

            # Move on to next node
            current = current.getNext()

        return newList


    
def main():

    print ("\n\n***************************************************************")
    print ("Test of addFirst:  should see 'node34...node0'")
    print ("***************************************************************")
    myList1 = LinkedList()
    for i in range(35):
      myList1.addFirst("node"+str(i))

    print (myList1)

    print ("\n\n***************************************************************")
    print ("Test of addLast:  should see 'node0...node34'")
    print ("***************************************************************")
    myList2 = LinkedList()
    for i in range(35):
      myList2.addLast("node"+str(i))

    print (myList2)

    print ("\n\n***************************************************************")
    print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
    print ("***************************************************************")
    greekList = LinkedList()
    greekList.addInOrder("gamma")
    greekList.addInOrder("delta")
    greekList.addInOrder("alpha")
    greekList.addInOrder("epsilon")
    greekList.addInOrder("omega")
    print (greekList)

    print ("\n\n***************************************************************")
    print ("Test of getLength:  should see 35, 5, 0")
    print ("***************************************************************")
    emptyList = LinkedList()
    print ("   Length of myList1:  ", myList1.getLength())
    print ("   Length of greekList:  ", greekList.getLength())
    print ("   Length of emptyList:  ", emptyList.getLength())

    print ("\n\n***************************************************************")
    print ("Test of findUnordered:  should see True, False")
    print ("***************************************************************")
    print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
    print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

    print ("\n\n***************************************************************")
    print ("Test of findOrdered:  should see True, False")
    print ("***************************************************************")
    print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
    print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

    print ("\n\n***************************************************************")
    print ("Test of delete:  should see 'node25 found', 'node34 found',")
    print ("   'node0 found', 'node40 not found'")
    print ("***************************************************************")
    print ("   Deleting 'node25' (random node) from myList1: ")
    if myList1.delete("node25"):
      print ("      node25 found")
    else:
      print ("      node25 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("   Deleting 'node34' (first node) from myList1: ")
    if myList1.delete("node34"):
      print ("      node34 found")
    else:
      print ("      node34 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("   Deleting 'node0'  (last node) from myList1: ")
    if myList1.delete("node0"):
      print ("      node0 found")
    else:
      print ("      node0 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("   Deleting 'node40' (node not in list) from myList1: ")
    if myList1.delete("node40"):
      print ("      node40 found")
    else:
      print ("   node40 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("\n\n***************************************************************")
    print ("Test of copyList:")
    print ("***************************************************************")
    greekList2 = greekList.copyList()
    print ("   These should look the same:")
    print ("      greekList before delete:")
    print (greekList)
    print ("      greekList2 before delete:")
    print (greekList2)
    greekList2.delete("alpha")
    print ("   This should only change greekList2:")
    print ("      greekList after deleting 'alpha' from second list:")
    print (greekList)
    print ("      greekList2 after deleting 'alpha' from second list:")
    print (greekList2)
    greekList.delete("omega")
    print ("   This should only change greekList1:")
    print ("      greekList after deleting 'omega' from first list:")
    print (greekList)
    print ("      greekList2 after deleting 'omega' from first list:")
    print (greekList2)

    print ("\n\n***************************************************************")
    print ("Test of reverseList:  the second one should be the reverse")
    print ("***************************************************************")
    print ("   Original list:")
    print (myList1)
    print ("   Reversed list:")
    myList1Rev = myList1.reverseList()
    print (myList1Rev) 

    print ("\n\n***************************************************************")
    print ("Test of orderList:  the second list should be the first one sorted")
    print ("***************************************************************")
    planets = LinkedList()
    planets.addFirst("Mercury")
    planets.addFirst("Venus")
    planets.addFirst("Earth")
    planets.addFirst("Mars")
    planets.addFirst("Jupiter")
    planets.addFirst("Saturn")
    planets.addFirst("Uranus")
    planets.addFirst("Neptune")
    planets.addFirst("Pluto?")

    print ("   Original list:")
    print (planets)
    print ("   Ordered list:")
    orderedPlanets = planets.orderList()
    print (orderedPlanets)

    print ("\n\n***************************************************************")
    print ("Test of isOrdered:  should see False, True")
    print ("***************************************************************")
    print ("   Original list:")
    print (planets)
    print ("   Ordered? ", planets.isOrdered())
    orderedPlanets = planets.orderList()
    print ("   After ordering:")
    print (orderedPlanets)
    print ("   ordered? ", orderedPlanets.isOrdered())

    print ("\n\n***************************************************************")
    print ("Test of isEmpty:  should see True, False")
    print ("***************************************************************")
    newList = LinkedList()
    print ("New list (currently empty):", newList.isEmpty())
    newList.addFirst("hello")
    print ("After adding one element:",newList.isEmpty())

    print ("\n\n***************************************************************")
    print ("Test of mergeList")
    print ("***************************************************************")
    list1 = LinkedList()
    list1.addLast("aardvark")
    list1.addLast("cat")
    list1.addLast("elephant")
    list1.addLast("fox")
    list1.addLast("lynx")
    print ("   first list:")
    print (list1)
    list2 = LinkedList()
    list2.addLast("bacon")
    list2.addLast("dog")
    list2.addLast("giraffe")
    list2.addLast("hippo")
    list2.addLast("wolf")
    print ("   second list:")
    print (list2)
    print ("   merged list:")
    list3 = list1.mergeList(list2)
    print (list3)

    print ("\n\n***************************************************************")
    print ("Test of isEqual:  should see True, False, True")
    print ("***************************************************************")
    print ("   First list:")
    print (planets)
    planets2 = planets.copyList()
    print ("   Second list:")
    print (planets2)
    print ("      Equal:  ",planets.isEqual(planets2))
    print (planets)
    planets2.delete("Mercury")
    print ("   Second list:")
    print (planets2)
    print ("      Equal:  ",planets.isEqual(planets2))
    print ("   Compare two empty lists:")
    emptyList1 = LinkedList()
    emptyList2 = LinkedList()
    print ("      Equal:  ",emptyList1.isEqual(emptyList2))

    print ("\n\n***************************************************************")
    print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
    print ("***************************************************************")
    dupList = LinkedList()
    print ("   removeDuplicates from an empty list shouldn't fail")
    newList = dupList.removeDuplicates()
    print ("   printing what should still be an empty list:")
    print (newList)
    dupList.addLast("giraffe")
    dupList.addLast("wolf")
    dupList.addLast("cat")
    dupList.addLast("elephant")
    dupList.addLast("bacon")
    dupList.addLast("fox")
    dupList.addLast("elephant")
    dupList.addLast("wolf")
    dupList.addLast("lynx")
    dupList.addLast("elephant")
    dupList.addLast("dog")
    dupList.addLast("hippo")
    dupList.addLast("aardvark")
    dupList.addLast("bacon")
    print ("   original list:")
    print (dupList)
    print ("   without duplicates:")
    newList = dupList.removeDuplicates()
    print (newList)

main()
    
