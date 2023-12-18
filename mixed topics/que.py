
def enqueue(queue,item):
    queue.append(item)
    print(f"enqueued : {item}")
def dequeue(queue):
    if (queue!=0):
        dequed=queue.pop(0)
        print("dequeued : {dequed}")
        return dequed
    else:
        print("queue is empty")


    

my_queue = []

enqueue(my_queue, 1)
enqueue(my_queue, 2)
enqueue(my_queue, 3)


dequeue(my_queue)
dequeue(my_queue)

print("Queue size after dequeues:", my_queue)