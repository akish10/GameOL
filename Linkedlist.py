
"""def Linkedlist(head,previousNode):
    #this function inserts at the beginning ot the linked list.

    if (head is None ):

        Data = None

        Pointer = None 

        previousNode = None 

        newNode = None 

        currentHead = None 

        print("Empty linked list.")

    

    else:
        
        #if (previousNode is not None ):

        currentHead = previousNode.next

        newNode = currentHead.next

        head = newNode


Output = Linkedlist(5,10)

print(Output) 

"""

def endLinkedList(lastNode,head):
    #inserts data at the end of a linked list.

     #first node in the linked list. is head 

     #pointer to previous node. is previousNode

    currentNode = None 


    if (lastNode is None ):

        currentNode = head

        return currentNode

    
    




