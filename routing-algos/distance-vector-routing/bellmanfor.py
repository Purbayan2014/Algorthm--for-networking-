import sys

def bellmanford(graph, vertices, edges, source):
    """
    Method used to detect the bellman ford algorithm for detecting the
    negative weight cycle 

    Args:
        graph [list] 
        vertex [integer]
        edges  [integer]
        source [integer]

    Returns:
        Shortest routes for the edges from the source
        and if a negative path is detected the shortest path 
        is not calculated    
    """
    #  initialize the distances for all the vertices as infinite
    dist_matrix = [sys.maxsize] * vertices
    # set the source vertex as 0
    dist_matrix[source] = 0

    # The outer loop goes for vertices-1 because a simple shortest path
    #  tree can have (vertices-1) edges

    for x in range(vertices-1):
        for y in range(edges):
            if dist_matrix[graph[y][0]] + graph[y][2] < dist_matrix[graph[y][1]]:
                dist_matrix[graph[y][1]] = dist_matrix[graph[y][0]] + graph[y][2]

            
    # now for the negative weights 
    #  if there exists a shorter path then we get 
    #  a cycle

    for x in range(edges):
        source_pt = graph[x][0]
        dest_pt = graph[x][1]
        wt =  graph[x][2]
        if  dist_matrix[source_pt] != sys.maxsize and dist_matrix[source_pt] + wt < dist_matrix[dest_pt]:
             print("Graph contains a negative weight cycle !! ")
    
    print("The shortest routes are as follows : ")
    for index in range(vertices):
        print(f"\nThe shortest distance for {index} from the source is ::  {dist_matrix[index]} ")

if __name__ == '__main__':
    vertex = 5
    edges = 8

    graph = [[0, 1, -1], [0, 2, 4], [1, 2, 3],
             [1, 3, 2], [1, 4, 2], [3, 2, 5],
             [3, 1, 1], [4, 3, -3]]
    
    bellmanford(graph=graph, vertices=vertex, edges=edges, source=0)
