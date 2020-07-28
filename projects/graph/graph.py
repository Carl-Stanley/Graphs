"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_next_vr(self, vertex_id):
        """
        Get all next_vr (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        TheQueue = Queue()
        touched_vr = set()
        TheQueue.enqueue(starting_vertex)
        while TheQueue.size() > 0:
            current_node = TheQueue.dequeue()
            if current_node not in touched_vr:
                touched_vr.add(current_node)
                next_vr = self.get_next_vr(current_node)
                for neighbor in next_vr:
                    TheQueue.enqueue(neighbor)
        print("\n".join(str(num)for num in touched_vr))

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        work_stack = Stack()
        touched_vr = []
        work_stack.push(starting_vertex)
        while work_stack.size() > 0:
            current_node = work_stack.pop()
            if current_node not in touched_vr:
                touched_vr.append(current_node)
                next_vr = self.get_next_vr(current_node)
                for neighbor in next_vr:
                    work_stack.push(neighbor)

        print("\n".join(str(vertex) for vertex in touched_vr))

    def dft_recursive(self, starting_vertex, touched_vr=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        touched_vr.add(starting_vertex)
        next_vr = self.get_next_vr(starting_vertex)
        for neighbor in next_vr:
            if neighbor not in touched_vr:
                self.dft_recursive(neighbor, touched_vr)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        touched_vr = set()
        TheQueue = Queue()
        TheQueue.enqueue([starting_vertex])
        while TheQueue.size() > 0:
            current_path = TheQueue.dequeue()
            current_node = current_path[-1]

            if current_node is destination_vertex:
                return current_path
            if current_node not in touched_vr:
                touched_vr.add(current_node)

                next_vr = self.get_next_vr(current_node)
                for neighbor in next_vr:
                    TheQueue.enqueue(current_path+[neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        touched_vr = set()
        work_stack = Stack()
        work_stack.push([starting_vertex])
        while work_stack.size() > 0:
            current_path = work_stack.pop()
            current_node = current_path[-1]

            if current_node is destination_vertex:
                return current_path
            if current_node not in touched_vr:
                touched_vr.add(current_node)

                next_vr = self.get_next_vr(current_node)
                for neighbor in next_vr:
                    work_stack.push(current_path+[neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], touched_vr=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if len(path) == 0:
            path.append(starting_vertex)
        touched_vr.add(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        next_vr = self.get_next_vr(starting_vertex)
        for neighbor in next_vr:
            if neighbor not in touched_vr:
                result = self.dfs_recursive(
                    neighbor, destination_vertex, path+[neighbor], touched_vr)
                if result is not None:
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print(f'recursive')
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))