class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count=count+1
            itr=itr.next
        print("count of linked list is : "+str(count))

    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        ll_str=''
        while itr:
            ll_str=ll_str+str(itr.data)+'-->' if itr.next else ll_str+str(itr.data)
            itr=itr.next
        print(ll_str)    
    
    def insert_at_begining(self,data):
        first_node = Node(data,self.head)
        self.head=first_node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        last_node=Node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=last_node    

    def insert_values(self,list_of_values):
        self.head=None
        for data in list_of_values:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr=self.head       
        while itr:
            if itr.data==data_after:
                node_to_insert = Node(data_to_insert,itr.next)
                itr.next=node_to_insert
                return
            itr=itr.next    

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        itr=self.head
        if itr.data==data: #only one node case
            itr.next=itr.next.next
            return

        while itr:
            if itr.data==data:
                prev_elem.next=itr.next
                return
            prev_elem=itr
            itr=itr.next
            
    def remove_at(self,index):
        pass

if __name__=='__main__':
    ll=LinkedList()
    ll.insert_values([1,2,3])
    ll.insert_at_begining(8)
    ll.print_ll()
    ll.insert_after_value(1,4)
    ll.print_ll()
    ll.remove_by_value(8)
    ll.print_ll()
    ll.get_length()