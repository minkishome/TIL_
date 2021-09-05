import heapq

def solution(operations):
    answer = []

    heap = []

    for operation in operations:
        string, num = operation.split(' ')
        if string == 'I':
            heapq.heappush(heap, int(num))
        else:
            if heap:
                if num == '1':
                    max_value = heapq.nlargest(1, heap)[0]
                    heap.remove(max_value)
                else:
                    heapq.heappop(heap)
            else:
                pass
    if heap:
        answer = [heap[-1], heap[0]]
    else:
        answer = [0, 0]

    return answer


solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])