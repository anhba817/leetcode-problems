# leetcode-problems
A repo where I learn from Leetcode

## TypeScript workflow
1. Install dependencies once with `npm install` (Node 18+ recommended).
2. Run all Jest suites via `npm test`. Helpful variants:
   - `npm run test:watch` keeps Jest running and reruns affected suites automatically.
   - `npm run test:coverage` produces a coverage report under `coverage/`.

## C++ workflow
1. Configure a build directory: `cmake -S . -B build` (requires CMake ≥3.28 and a C++20 compiler).
2. Build all targets with `cmake --build build`.
3. Execute the tests managed by CTest with `ctest --test-dir build --output-on-failure`.
   - Re-run the configure/build steps after adding new problems so they are picked up by CMake.

## Python workflow
1. Install [uv](https://docs.astral.sh/uv/) (already included in most dev environments) and sync dependencies with `uv sync --dev` to create `.venv`.
2. Run the LeetCode Python tests via `uv run pytest` (configuration lives in `pyproject.toml`).
3. Python source files live under `src/leetcode_problems`, and tests live under `tests/` (e.g., problem 2528 is under `src/leetcode_problems/problem_2528`).
