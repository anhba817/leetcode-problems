import DisjointSets from "@/disjoint-sets-union-find/utils/disjoint_sets";

export class ConnectedComponentsInLCMGraph {
  private union: DisjointSets; // Union for numbers less than or equal threshold
  private nums: number[];
  private belowThresholdNums: number[] = [];
  private threshold: number;
  private singleComponents: number[] = [];
  constructor(nums: number[], threshold: number) {
    this.nums = nums;
    this.threshold = threshold;
    this.union = new DisjointSets(threshold);
    this.setup();
  }

  private setup(): void {
    for (const num of this.nums) {
      if (num > this.threshold) {
        this.singleComponents.push(num);
        continue;
      }
      this.belowThresholdNums.push(num);
      let m = 1;
      while (num * m <= this.threshold) {
        this.union.unionSets(num, num * m);
        m += 1;
      }
    }
  }
  public countComponents(): number {
    const results = new Set(
      this.belowThresholdNums.map((num) => this.union.findRoot(num)),
    );
    return results.size + this.singleComponents.length;
  }
}
