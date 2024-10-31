import numpy as np
import matplotlib.pyplot as plt

class CellDecomposition:
    def __init__(self, grid):
        self.grid = grid
        self.rows = grid.shape[0]
        self.cols = grid.shape[1]
        self.path = []

    def is_safe(self, x, y):
        return (0 <= x < self.rows) and (0 <= y < self.cols) and (self.grid[x][y] == 1)

    def find_path(self, start, end):
        self.path = []
        if self._find_path_recursive(start, end):
            return self.path
        return None

    def _find_path_recursive(self, current, end):
        x, y = current
        # Jika mencapai tujuan
        if current == end:
            self.path.append(current)
            return True
        
        # Jika posisi saat ini tidak aman
        if not self.is_safe(x, y):
            return False

        # Tandai posisi saat ini sebagai bagian dari jalur
        self.path.append(current)

        # Cek setiap arah (atas, bawah, kiri, kanan)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_cell = (x + dx, y + dy)
            if self._find_path_recursive(next_cell, end):
                return True

        # Jika jalur tidak ditemukan, hapus posisi saat ini dari jalur
        self.path.pop()
        return False

    def plot_path(self):
        plt.imshow(self.grid, cmap='gray_r')
        if self.path:
            x, y = zip(*self.path)
            plt.plot(y, x, marker='o', color='blue', markersize=5, linewidth=2)
        plt.title("Jalur Robot")
        plt.xlabel("Kolom")
        plt.ylabel("Baris")
        plt.xticks(np.arange(-0.5, self.cols, 1), [])
        plt.yticks(np.arange(-0.5, self.rows, 1), [])
        plt.grid()
        plt.show()

# Contoh penggunaan
if __name__ == "__main__":
    # 1 adalah sel bebas rintangan, 0 adalah sel dengan rintangan
    grid = np.array([
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1]
    ])

    start_position = (0, 0)  # Titik awal
    end_position = (4, 4)    # Titik tujuan

    cell_decomp = CellDecomposition(grid)
    path = cell_decomp.find_path(start_position, end_position)

    if path:
        print("Jalur ditemukan:", path)
        cell_decomp.plot_path()
    else:
        print("Jalur tidak ditemukan.")
