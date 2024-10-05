from LinkedList import LinkedList

# create a linked list instance 
list = LinkedList()

# add first node into the linked list
list.insert_at_front(32)
print(f"Added following note into the linked list : {list.get_head_value()}")

# add second node into the linked list
list.insert_at_front(65)
print(f"Added following note into the linked list : {list.get_head_value()}")
