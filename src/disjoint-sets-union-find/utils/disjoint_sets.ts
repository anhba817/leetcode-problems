export default class DisjointSets {
  private parent: number[];
  private size: number[];
  constructor(n: number) {
    this.parent = Array.from({ length: n + 1 }, (_, i) => i);
    this.size = Array(n + 1).fill(0);
  }

  public findRoot(a: number): number {
    if (this.parent[a] === a) {
      return a;
    }
    this.parent[a] = this.findRoot(this.parent[a]);
    return this.parent[a];
  }

  public unionSets(a: number, b: number): void {
    const rootA = this.findRoot(a);
    const rootB = this.findRoot(b);
    if (rootA !== rootB) {
      if (this.size[rootA] < this.size[rootB]) {
        this.parent[rootA] = rootB;
        this.size[rootB] += this.size[rootA];
      } else {
        this.parent[rootB] = rootA;
        this.size[rootA] += this.size[rootB];
      }
    }
  }

  public isConnected(a: number, b: number): boolean {
    return this.findRoot(a) === this.findRoot(b);
  }
}
