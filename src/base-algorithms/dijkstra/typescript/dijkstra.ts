import MinHeap from "@/base-algorithms/utils/min_heap";

/**
 * Build an adjacency list for an undirected weighted graph.
 * Each `edges[i] = [ui, vi, wt]` adds a bidirectional edge of weight `wt`.
 */
function constructAdj(edges: number[][], n: number) {
  // adj[u] = list of [v, wt]
  const adj: [number, number][][] = Array.from({ length: n }, () => []);

  for (const edge of edges) {
    const [u, v, wt] = edge;
    adj[u].push([v, wt]);
    adj[v].push([u, wt]);
  }

  return adj;
}

/**
 * Compute shortest-path distances from `src` to every node using Dijkstra's algorithm.
 * @returns array where index `i` yields the minimum cost from `src` to `i`.
 */
export function dijkstra(n: number, edges: number[][], src: number) {
  // Create adjacency list
  const adj = constructAdj(edges, n);

  // Create a min heap to store <distance, node>
  const minHeap = new MinHeap();

  // Create an array for distances and initialize all distances as infinity
  const dist = Array(n).fill(Number.MAX_SAFE_INTEGER);

  // Push the source node with distance 0
  minHeap.push([0, src]);
  dist[src] = 0;

  // Pop the closest node from the PQ and relax its edges
  while (minHeap.size() > 0) {
    const item = minHeap.pop() as [number, number];

    // Traverse all adjacent of the node
    // item[1] is node label
    for (const [v, weight] of adj[item[1]]) {
      if (dist[v] > dist[item[1]] + weight) {
        dist[v] = dist[item[1]] + weight;
        minHeap.push([dist[v], v]);
      }
    }
  }

  return dist;
}
