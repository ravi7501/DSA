class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class single_linklist:
    def __init__(self):
        self.head = None

    def insert_from_front(self,data):
        n=node(data)
        if self.head==None:
            self.head=n
            return
        n.next=self.head
        self.head=n
        return
    
    def insert_from_back(self,data):
        n=node(data)
        if self.head==None:
            self.head=n
            return
        t=self.head
        while t.next:
            t=t.next
        t.next=n
        return


    def display_linklist(self):
        t=self.head
        print("link list ")
        while t is not None:
            print(t.data)
            t=t.next
       

    def length_link_list(self):
        #print('length of linklist: ')
        count=0
        t=self.head
        while t is not None:
            count+=1
            t=t.next
        return  count
    
    def after_specfic_pos(self,pos,data):
        count=0
        t=self.head
        n=node(data)
        length=self.length_link_list()
        if pos>length:
            return "postion is greater then length of link  list"
        if pos==0:
            self.insert_from_front(data)
            return
        while t is not None and count<pos-1:
            count+=1
            t=t.next
        n.next=t.next
        t.next=n
        return 
            
                




if __name__=="__main__":
    li=single_linklist()
    li.insert_from_front(90)
    li.insert_from_front(89)
    li.display_linklist()
    li.insert_from_back(34)
    li.display_linklist()
    print(li.length_link_list())
    li.after_specfic_pos(2,65)
    li.display_linklist()






        
        
