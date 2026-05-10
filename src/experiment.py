import time
import random
from graph import Graph
from vertex import Vertex
class Experiment:
    def __init__(self):
        self.__results = []
    def run_traversals(self, graph, start_id, label, show_order=False):
        t_start = time.perf_counter_ns()
        bfs_order = graph.bfs(start_id)
        t_end = time.perf_counter_ns()
        bfs_time = t_end - t_start
        t_start = time.perf_counter_ns()
        dfs_order = graph.dfs(start_id)
        t_end = time.perf_counter_ns()
        dfs_time = t_end - t_start
        if show_order:
            print(f"[{label}] BFS order: {bfs_order}")
            print(f"[{label}] DFS order: {dfs_order}")
        return {"label": label, "bfs_time_ns": bfs_time, "dfs_time_ns": dfs_time}
    def run_multiple_tests(self, sizes):
        random.seed(42)
        for n in sizes:
            g = Graph()
            for i in range(n):
                g.add_vertex(Vertex(i))
            for i in range(n):
                for _ in range(2):
                    j = random.randint(0, n - 1)
                    if j != i:
                        g.add_edge(i, j)
            show = (n == sizes[0])
            result = self.run_traversals(g, 0, f"{n} vertices", show_order=show)
            self.__results.append(result)
    def print_results(self):
        print(f"\n{'Graph Size':<15} {'BFS Time (ns)':>18} {'DFS Time (ns)':>18}\n")
        for r in self.__results:
            print(f"\n{r['label']:<15} {r['bfs_time_ns']:>18,} {r['dfs_time_ns']:>18,}\n")