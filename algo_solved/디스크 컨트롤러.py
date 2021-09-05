import heapq

def solution(jobs):
    answer, now, index = 0, 0, 0
    heap = []
    start = -1
    while index < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            new_job = heapq.heappop(heap)
            start = now
            now += new_job[0]
            answer += (now - new_job[1])
            index += 1
        else:
            now += 1

    return int(answer // len(jobs))



solution([[0, 3], [1, 9], [2, 6]])