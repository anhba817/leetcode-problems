/**
 * Binary min-heap storing tuple entries `[priority, value]`.
 * Maintains the smallest priority at the root by bubbling nodes up/down.
 *
 * Example tree representation for the array `[1, 3, 5, 7, 9, 8, 6, 10, 12, 15, 17]`:
 *
 *                    1
 *                 /     \
 *               3         5
 *             /   \     /   \
 *           7       9  8     6
 *          / \     / \
 *        10  12  15  17
 *
 * Array indices: 0:1, 1:3, 2:5, 3:7, 4:9, 5:8, 6:6, 7:10, 8:12, 9:15, 10:17.
 * Children of `i` are at `2i + 1` (left) and `2i + 2` (right).
 */
export default class MinHeap {
  private heap: [number, number][] = [];
  constructor() {}

  /** Insert a tuple and bubble it up until the min-heap invariant holds. */
  push(val: [number, number]) {
    this.heap.push(val);
    this._heapifyUp(this.heap.length - 1);
  }

  /**
   * Remove and return the tuple with the smallest priority.
   * Returns null when the heap is empty.
   */
  pop() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const min = this.heap[0];
    this.heap[0] = this.heap.pop() as [number, number];
    this._heapifyDown(0);
    return min;
  }

  size() {
    return this.heap.length;
  }

  // Restore heap order by swapping a node with its parent while it is smaller.
  _heapifyUp(index: number) {
    while (index > 0) {
      const parent = Math.floor((index - 1) / 2);
      if (this.heap[parent][0] <= this.heap[index][0]) break;
      [this.heap[parent], this.heap[index]] = [
        this.heap[index],
        this.heap[parent],
      ];
      index = parent;
    }
  }

  // Restore heap order by pushing a node down to the smallest child when needed.
  _heapifyDown(index: number) {
    const n = this.heap.length;
    while (true) {
      let smallest = index;
      const left = 2 * index + 1;
      const right = 2 * index + 2;

      if (left < n && this.heap[left][0] < this.heap[smallest][0]) {
        smallest = left;
      }

      if (right < n && this.heap[right][0] < this.heap[smallest][0]) {
        smallest = right;
      }

      if (smallest === index) break;
      [this.heap[smallest], this.heap[index]] = [
        this.heap[index],
        this.heap[smallest],
      ];
      index = smallest;
    }
  }
}
