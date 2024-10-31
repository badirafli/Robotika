import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # (x, y) tuple
        self.parent = parent
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost to the end node
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

def heuristic(a, b):
    # Menghitung jarak Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, end, grid):
    open_list = []
    closed_list = []

    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        current_node = heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        # Jika mencapai node tujuan
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Membalikkan jalur

        # Mendapatkan posisi node saat ini
        (x, y) = current_node.position

        # Menghasilkan anak-anak node
        neighbors = [
            (x - 1, y), (x + 1, y),  # Kiri, Kanan
            (x, y - 1), (x, y + 1)   # Atas, Bawah
        ]

        for next_position in neighbors:
            if (0 <= next_position[0] < len(grid)) and (0 <= next_position[1] < len(grid[0])):
                if grid[next_position[0]][next_position[1]] != 0:  # 0 berarti rintangan
                    continue

                neighbor_node = Node(next_position, current_node)

                if neighbor_node in closed_list:
                    continue

                # Menghitung biaya g, h, dan f
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_node.position, end_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if add_to_open(open_list, neighbor_node):
                    heapq.heappush(open_list, (neighbor_node.f, neighbor_node))

    return None  # Jalur tidak ditemukan

def add_to_open(open_list, neighbor_node):
    for node in open_list:
        if neighbor_node == node[1] and neighbor_node.g > node[1].g:
            return False
    return True

# Contoh penggunaan
if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1]
    ]

    start_position = (0, 0)  # Titik awal
    end_position = (4, 4)    # Titik tujuan

    path = a_star(start_position, end_position, grid)

    if path:
        print("Jalur ditemukan:", path)
    else:
        print("Jalur tidak ditemukan.")
