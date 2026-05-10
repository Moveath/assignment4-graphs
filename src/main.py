from vertex import Vertex
from graph import Graph
from experiment import Experiment
def main():
    print("=" * 55)
    print("   Assignment 4: Graph Traversal")
    print("=" * 55)
    print("\n--- Small Graph (10 vertices) ---")
    small = Graph()
    for i in range(10):
        small.add_vertex(Vertex(i))
    edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(3,7),(4,8),(5,9)]
    for u, v in edges:
        small.add_edge(u, v)
    small.print_graph()
    print("\nBFS from vertex 0:", small.bfs(0))
    print("DFS from vertex 0:", small.dfs(0))
    print("\n--- Performance Experiments ---")
    exp = Experiment()
    exp.run_multiple_tests(sizes=[10, 30, 100])
    exp.print_results()
if __name__ == "__main__":
    main()