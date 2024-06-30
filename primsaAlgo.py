# graph=[
#     [0,7,-1,-1,-1,-1,-1,2,-1,-1],
#     [7,0,4,1,-1,-1,5,-1,-1,-1,-1],
#     [-1,4,0,-1,-1,-1,-1,8,-1,-1],
#     [-1,1,-1,0,6,8,3,3,-1,-1],
#     [-1,-1,-1,6,0,-1,-1,6,8,-1],
#     [-1,5,-1,8,-1,0,-1,-1,-1,-1],
#     [-1,-1,-1,3,-1,-1,0,-1,9,2],
#     [2,-1,88,3,6,-1,-1,0,-1,-1],
#     [-1,-1,-1,-1,8,-1,9,-1,0,-1],
#     [-1,-1,-1,-1,-1,-1,2,-1,-1,0],
# ]

graph = [
    [0, 7, -1, -1, -1, -1, -1, 2, -1, -1],
    [7, 0, 4, 1, -1, -1, 5, -1, -1, -1],
    [-1, 4, 0, -1, -1, -1, -1, 8, -1, -1],
    [-1, 1, -1, 0, 6, 8, 3, 3, -1, -1],
    [-1, -1, -1, 6, 0, -1, -1, 6, 8, -1],
    [5, -1, -1, 8, -1, 0, -1, -1, -1, -1],
    [-1, -1, -1, 3, -1, -1, 0, -1, 9, 2],
    [2, -1, 8, 3, 6, -1, -1, 0, -1, -1],
    [-1, -1, -1, -1, 8, -1, 9, -1, 0, -1],
    [-1, -1, -1, -1, -1, -1, 2, -1, -1, 0],
]
visited =[False]*len(graph)
min=float('inf')
x=y=-1
print(min)
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]==0 or graph[i][j]==-1:
            continue
        elif min>graph[i][j]:
            min=graph[i][j]
            x=i
            y=j
print(x+1,y+1,min)

visited[x]=True
visited[y]=True
mst=[]
mst.append(tuple((x+1,y+1,min)))
print(mst)

while False in visited:
    min=float('inf')
    for i in range(len(visited)):
        # if visited[i]==True:
        for j in range(len(graph[i])):
            if graph[i][j]==0 or graph[i][j]==-1 or visited[j]==True:
                continue
            elif min>graph[i][j]:
                min=graph[i][j]
                x=i
                y=j
    visited[y]=True
    mst.append(tuple((x+1,y+1,min)))
for i in mst:
    print(i)


# def dijkstra(graph, start):
#     n = len(graph)
#     dist = [float('inf')] * n
#     dist[start] = 0
#     visited = [False] * n
    
#     for _ in range(n):
#         # Find the unvisited node with the smallest distance
#         min_dist = float('inf')
#         u = -1
#         for i in range(n):
#             if not visited[i] and dist[i] < min_dist:
#                 min_dist = dist[i]
#                 u = i
        
#         if u == -1:
#             break

#         # Mark the node as visited
#         visited[u] = True
        
#         # Update the distances of the neighboring nodes
#         for v in range(n):
#             if graph[u][v] != -1 and not visited[v]:
#                 new_dist = dist[u] + graph[u][v]
#                 if new_dist < dist[v]:
#                     dist[v] = new_dist
    
#     return dist

# # Define the graph
# graph = [
#     [0, 7, -1, -1, -1, -1, -1, 2, -1, -1],
#     [7, 0, 4, 1, -1, -1, 5, -1, -1, -1],
#     [-1, 4, 0, -1, -1, -1, -1, 8, -1, -1],
#     [-1, 1, -1, 0, 6, 8, 3, 3, -1, -1],
#     [-1, -1, -1, 6, 0, -1, -1, 6, 8, -1],
#     [5, -1, -1, 8, -1, 0, -1, -1, -1, -1],
#     [-1, -1, -1, 3, -1, -1, 0, -1, 9, 2],
#     [2, -1, 8, 3, 6, -1, -1, 0, -1, -1],
#     [-1, -1, -1, -1, 8, -1, 9, -1, 0, -1],
#     [-1, -1, -1, -1, -1, -1, 2, -1, -1, 0],
# ]

# # Starting node (0-indexed)
# start_node = 0

# # Apply Dijkstra's algorithm
# distances = dijkstra(graph, start_node)

# # Print the shortest distances from the start node to all other nodes
# for i, d in enumerate(distances):
#     print(f"Shortest distance from node {start_node + 1} to node {i + 1} is {d}")