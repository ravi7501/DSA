# linklist  algorithum 
# reversing a linklist


from linklistfirst import  node,single_linklist



def linklist_reverse(head):  # reversing a linklist 
    curr = head 
    prev = None
    while curr is not None:
        next_node=curr.next 
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def reverse_linklist(head): #reversing a linklist using recurssion
    if head is None or head.next is None:
        return head
    
    rest=reverse_linklist(head.next)
    head.next.next=head
    head.next=None
    return rest

def rotate_linklist(head,k): # using loop rotatating link list 
    last=head
    temp=head
    if head==None or k==0:
        return head
    while last.next!=None:
        last=last.next 
    #print("this is last element ",last.data)
    #print("this is last element ",temp.data)
    while k!=0:
            
            head=head.next
            temp.next=None
            last.next=temp
            last=temp
            temp=head
            #display_linklist(head)
            #print(k,"head ",head.data,"last ",last.data,"temp",temp.data)
            k-=1
  #  print("last element ",temp.data)
    return head

       


# rotating linklist without using loop
def rotate_linklist_w_lp(head,k):
    if k==0:
        return
    current=head
    count=1
    while(count <k and current is not None):
        current = current.next 
        count+=1
    if current is None:
        return 
    kthnode=current 
    while(current.next is not None):
        current=current.next 
    current.next=head
    head=kthnode.next 
    kthnode.next=None
    return head



if __name__=="__main__":
    li=single_linklist()
    li.insert_from_front(90)
    li.insert_from_front(89)
    li.insert_from_back(34)
    li.insert_from_back(12)
    li.display_linklist()
    li.head=linklist_reverse(li.head)
    li.display_linklist()
    li.head=reverse_linklist(li.head)
    li.display_linklist()

    li.head=rotate_linklist(li.head,3)
    #print(li.head.data)
    li.display_linklist()

    li.head=rotate_linklist_w_lp(li.head,2)
    li.display_linklist()



