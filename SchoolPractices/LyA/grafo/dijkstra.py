import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph["nodes"]}
    previous = {node: None for node in graph["nodes"]}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph["edges"].get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Construir los caminos
    paths = {}
    for node in graph["nodes"]:
        if distances[node] < float('inf'):
            path = []
            current = node
            while current is not None:
                path.insert(0, current)
                current = previous[current]
            paths[node] = path

    return {
        "distances": distances,
        "paths": paths
    }
