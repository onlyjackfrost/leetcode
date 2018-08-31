class Node :
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None

class linked_list :
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None :
            self.head = node
        else :
            node.next = self.head
            node.next.pre = node
            self.head = node
    
    def remove(self, node_p):
        tmp = node_p.pre
        node_p.pre.next = node_p.next
        node_p.next.pre = tmp

    def search(self, data_k):
        h = self.head
        if h != None :
            while h.next != None :
                if h.data == data_k :
                    return h
                h = h.next
                
        return None
l = linked_list()
l.add(1)
l.add(2)
l.add(3)
print(l)
l.remove(l.search(2))
print(l)

    
                
    
    