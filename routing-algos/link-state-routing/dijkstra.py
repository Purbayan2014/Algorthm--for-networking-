import sys

class graph():

    def __init__(self, vertices):
        self.vert = vertices
        # construct the graph with the vertices
        self.grph = [[0 for vert in range(vertices)] for col in range(vertices)]

    def min_dist(self, dist, adj_mat):
        """
        Method used to determine the vertex with the least cost ,
        from the set of vertices that are not yet included in the adjacent matrxi

        Args:
            dist (list) : Contains the costs or the so called edges of the 
                          graph
            adj_mat (list) : List containing the status for the vertices to be 
                             included in the shortest path tree
        Return
            min_idx (int) : The index of the vertex with the least cost path
        """
        min =  sys.maxsize
        
        # min_idx = 0
        for vertex in range(self.vert):
            #  check if the vertex is not included in the matrix and also check
            #  if the cost of the vertex path is min 
            if dist[vertex] < min and adj_mat[vertex] == False:
                # update the min dist and the min index
                min = dist[vertex]
                min_idx = vertex
        return min_idx

    def display_cout(self, dist_matrix):
        for vertices in range(self.vert):
            print(f"The least cost of vertex {vertices} from the source is {dist_matrix[vertices]}")

    def dijkstra(self, source):
        """
        Method used to implement dijkstra's algorithm for an undirected graph
        with weights

        Args :
            source (integer) : source vertex of the graph

        Returns:
            Prints out the min cost for all the vertices from the source
        """
        # set the dist_matrix for all the included vertices to infinite at the start 
        #  we can update it as we iterate through the vertices
        dist_matrix = [sys.maxsize] * self.vert
        # set the source vertex as 0
        dist_matrix[source] = 0

        adj_matrix = [False] * self.vert

        for vertx in range(self.vert):
            # check for the min dist vertex from the set of the vertices which are not yet
            # included in the adj_matrix 
            temp = self.min_dist(dist_matrix, adj_matrix)

            # update the value of the visted vertex in the graph as true
            adj_matrix[temp] =  True

            # update the value of the adjacent vertex of the picked vertex only 
            # if the currect edge cost is greater than the new edge dist and the
            # vertex is not included in the shortest path tree
            for y in range(self.vert):
                if self.grph[temp][y] > 0 and adj_matrix[y] == False \
                    and dist_matrix[y] > dist_matrix[temp] + self.grph[temp][y]:
                    dist_matrix[y] =  dist_matrix[temp] + self.grph[temp][y]

        self.display_cout(dist_matrix=dist_matrix)


if __name__ == '__main__':
    gr = graph(9)
    gr.grph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    gr.dijkstra(0)