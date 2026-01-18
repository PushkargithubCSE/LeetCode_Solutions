# LeetCode_Solutions

A personal collection of my solved LeetCode problems. This repo stores solutions I write while practicing algorithm and data-structure problems on LeetCode. Each solution includes a link to the original problem, the code, complexity notes, and a short explanation.

---

## Goals
- Keep a searchable, well-organized archive of solved problems.
- Track progress across difficulties and topics.
- Provide clear solutions with complexity analysis and short explanations.

---

## Repository structure
- / (root)
  - README.md — this file
  - /problems
    - /<problem-id>-<slug>/
      - solution.<ext> (e.g., solution.py, solution.cpp)
      - README.md (optional: explanation, examples)
  - /notes (optional) — topic or pattern notes (two-pointer, DP, graph)
  - /tests (optional) — example input/output or small run scripts

Example folder:
```
problems/
├── 1-two-sum/
│   ├── solution.py
│   └── README.md
├── 2-add-two-numbers/
│   └── solution.cpp
```

---

## Naming convention
- Folder: `<leetcode-id>-<kebab-case-title>` (e.g., `3-longest-substring-without-repeating-characters`)
- Solution files: `solution.<ext>` (language extension: `.py`, `.cpp`, `.java`, `.js`, etc.)
- If multiple solutions for same problem (different approaches), name them: `solution_approach1.py`, `solution_fast.py`, etc.

---

## Solution file header template
Include a short header comment at top of each solution file:
```text
/*
LeetCode <ID>: <Title>
Author: PushkargithubCSE
Language: <Python3 / C++ / Java / JS>
Date: YYYY-MM-DD
Complexity: Time O(...), Space O(...)
Approach: Short description of the approach
*/
```

Example (Python):
```python
"""
LeetCode 1: Two Sum
Author: PushkargithubCSE
Language: Python3
Date: 2026-01-18
Complexity: Time O(n), Space O(n)
Approach: Use a hash map to store complement indices while iterating once.
"""
```

---

## How to add a solution
1. Create a new branch: `git checkout -b feat/leetcode-<id>-<short-title>`
2. Add a directory under `problems/` using the naming convention.
3. Add your `solution.<ext>` file with the header template and optional `README.md` with explanation.
4. Update the top-level README "Problems table" if you maintain it manually.
5. Commit with message: `feat: add solution for LeetCode <id> - <Title>`
6. Open a PR (optional) and merge.

---

## Problems table (optional)
You can keep an index in README or a separate file. Example table format:
| # | Problem | Difficulty | Language | File | Notes |
|---:|---|---:|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Python3 | problems/1-two-sum/solution.py | Hashmap, O(n) |

---

## Running / Testing
- Python: `python3 solution.py` (add a main with sample cases)
- C++: compile and run, e.g. `g++ solution.cpp -std=c++17 -O2 -o sol && ./sol`
- JavaScript (Node): `node solution.js`
Include a small `if __name__ == "__main__":` block or equivalent to run examples locally.

---

## Conventions & Best practices
- Add time/space complexity and brief approach at top of each solution.
- Prefer readable, idiomatic code over micro-optimizations.
- Keep explanation short in file header; expand in `README.md` inside the problem folder if needed.
- Tag problems by topic in their problem-folder README (e.g., #dynamic-programming, #two-pointers).

---

## Contribution
This repo is primarily personal, but contributions are welcome:
- Open an issue if you find errors or want to propose alternate solutions.
- Submit PRs for improvements or additional languages/solutions.

---

## License
MIT — see LICENSE file (or add one if you want to open-source your solutions).

---

## Contact
GitHub: [PushkargithubCSE](https://github.com/PushkargithubCSE)

Good luck and happy coding!
