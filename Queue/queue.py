from collections import deque

q = deque()

def isEmpty():
    return len(q) == 0

# add new data
def qEnqueue(data):
    q.append(data)
# remove first el
def qDequeue():
    if isEmpty():
        return
    q.popleft()
# return fisrt el
def getFront():
    if isEmpty():
        return -1
    return q[0]
# return last element
def getRear():
    if isEmpty():
        return -1
    return q[-1]

if __name__ == '__main__':
    qEnqueue(1)
    qEnqueue(8)
    qEnqueue(3)
    qEnqueue(6)
    qEnqueue(2)

    if not isEmpty():
        print("Queue after enqueue operation: ", list(q))

    print("Front: ", getFront())
    print("Rear: ", getRear())

    print("Queue size: ", len(q))

    qDequeue()

    print("Is queue empty? ", "Yes" if isEmpty() else "No")