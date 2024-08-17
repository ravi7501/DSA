# linklist  algorithum 
# reversing a linklist


from linklistfirst import  node,single_linklist

def linklist_reverse(head):
    curr = head 
    prev = None
    while curr is not None:
        next_node=curr.next 
        curr.next = prev
        prev = curr
        curr = next_node
    return prev




    print(head)



if __name__=="__main__":
    li=single_linklist()
    li.insert_from_front(90)
    li.insert_from_front(89)
    li.insert_from_back(34)
    li.insert_from_back(12)
    li.display_linklist()
    li.head=linklist_reverse(li.head)
    li.display_linklist()
