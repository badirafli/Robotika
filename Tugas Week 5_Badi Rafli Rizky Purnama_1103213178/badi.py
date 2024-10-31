import heapq

def dijkstra(graph, start, end):
    # Menyimpan jarak terpendek dari start ke setiap node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Menyimpan jalur terpendek
    previous_nodes = {node: None for node in graph}

    # Priority queue untuk menyimpan node yang akan dieksplorasi
    priority_queue = [(0, start)]  # (jarak, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika kita sudah mencapai node tujuan
        if current_node == end:
            break

        # Jika jarak saat ini lebih besar dari jarak terpendek yang sudah diketahui
        if current_distance > distances[current_node]:
            continue

        # Menelusuri tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Hanya pertimbangkan node yang lebih baik
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Membangun jalur terpendek dari start ke end
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1]  # Membalikkan jalur

    return path, distances[end]

# Contoh penggunaan
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    end_node = 'D'
    shortest_path, total_cost = dijkstra(graph, start_node, end_node)

    print(f"Jalur terpendek dari {start_node} ke {end_node}: {shortest_path}")
    print(f"Biaya total: {total_cost}")
