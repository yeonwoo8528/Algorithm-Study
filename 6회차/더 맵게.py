import heapq
def solution(scoville, K):
    heap = []
    cnt = 0
    for i in scoville:
        heapq.heappush(heap, i)
    while(heap[0] < K):
        if(len(heap) == 1): return -1
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1
    return cnt
