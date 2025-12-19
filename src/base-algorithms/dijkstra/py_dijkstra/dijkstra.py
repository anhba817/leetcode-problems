import heapq
import sys


# Function to construct adjacency
def constructAdj(edges, n):

    # adj[u] = list of [v, wt]
    adj = [[] for _ in range(n)]

    for edge in edges:
        u, v, wt = edge
        adj[u].append([v, wt])
        adj[v].append([u, wt])

    return adj


# Returns shortest distances from src to all other vertices
def dijkstra(n, edges, src):
    # Create adjacency list
    adj = constructAdj(edges, n)

    # Create a priority queue to store vertices that
    # are being preprocessed.
    pq = []

    # Create a list for distances and initialize all
    # distances as infinite
    dist = [sys.maxsize] * n

    # Insert source itself in priority queue and initialize
    # its distance as 0.
    heapq.heappush(pq, [0, src])
    dist[src] = 0

    # Looping till priority queue becomes empty (or all
    # distances are not finalized)
    while pq:
        # The first vertex in pair is the minimum distance
        # vertex, extract it from priority queue.
        u = heapq.heappop(pq)[1]

        # Get all adjacent of u.
        for x in adj[u]:
            # Get vertex label and weight of current
            # adjacent of u.
            v, weight = x[0], x[1]

            # If there is shorter path to v through u.
            if dist[v] > dist[u] + weight:
                # Updating distance of v
                dist[v] = dist[u] + weight
                heapq.heappush(pq, [dist[v], v])

    # Return the shortest distance array
    return dist
