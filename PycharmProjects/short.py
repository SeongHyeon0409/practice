from queue import PriorityQueue  # 파이썬 내장 모듈


def dijkstra(road, N):
    queue = PriorityQueue()  # 우선순위 큐
    queue.put([1, 0])  # 1번 마을부터 시작

    dist = [float('inf')] * (N + 1)  # 계산하기 편하게 N+1 길이만큼 리스트 생성
    dist[1] = 0  # 1번 마을은 무조건 거리가 0

    while not queue.empty():
        current, current_cost = queue.get()  # 현재 선택된 노드와 비용
        for src, dest, cost in road:  # 출발지, 목적지, 비용
            next_cost = cost + current_cost  # 비용
            if src == current and next_cost < dist[dest]:
                # src가 현재 선택된 노드면서 목적지까지 더 저렴할 경우
                dist[dest] = next_cost  # 최소 비용을 갱신
                queue.put([dest, next_cost])  # Priority Queue에 추가
            elif dest == current and next_cost < dist[src]:
                # dest가 현재 선택된 노드면서 출발지까지 더 저렴할 경우
                dist[src] = next_cost  # 최소 비용을 갱신
                queue.put([src, next_cost])  # Priority Queue에 추가
    return dist


def solution(N, road, K):
    dist = dijkstra(road, N)
    return len([x for x in dist if x <= K])  # list comprehension

