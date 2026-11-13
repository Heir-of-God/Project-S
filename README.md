# Project S ✨ Competitive Programming Solutions

Hello👋 and welcome to "Project S" - my personal archive of solutions to competitive programming and algorithm problems from **LeetCode**, **HackerRank** and **Codeforces**, written mostly in **Python**.

## About

I'm a Software Engineering student, and this repository is where I practise algorithms and data structures and keep track of what I've solved. My solutions may be ineffective, complex or confusing, since I, like many others, am constantly learning💫. Most of them use type hints and are meant to be readable first.

The latest activity here is from December 2024. If you find the repo interesting or useful, a "⭐" is very much appreciated🍀.

**Owner😇: [Heir-of-God](https://github.com/Heir-of-God)**  
**License📃: BSD 3-Clause - see the [LICENSE](LICENSE) file for details**

## Overview

Counts below are the number of solution files currently in the repository (one file = one problem; a file may contain several approaches).

| Platform | Folder | Solutions | What is inside |
| --- | --- | ---: | --- |
| LeetCode 🎩 | [`Leetcode`](Leetcode) | 478 | Daily challenges (222), contests (25), study plans (66), other problems (166) |
| Codeforces 🏆 | [`Codeforces`](Codeforces) | 274 | Contest problems (30), other problemset tasks (244), a beginner problem list (link only) |
| HackerRank 🔋 | [`HackerRank`](HackerRank) | 104 | "3 Months Preparation Kit" (13 weeks) |
| **Total** | | **856** | |

**Languages:** all solutions are Python 3 (`.py`).  
**Topics touched:** arrays and strings, sorting, binary search, heaps, stacks and queues, linked lists, trees and BSTs, dynamic programming, graphs, greedy, math and number theory, and custom data-structure design.

My accounts: [LeetCode](https://leetcode.com/heir-of-god/) · [Codeforces](https://codeforces.com/profile/Heir-of-God)

## Notable solutions

A few files I think show more than a simple loop:

- [`Leetcode/Dailys/29.09.2024.py`](Leetcode/Dailys/29.09.2024.py) - a data structure built from scratch: nodes plus a hand-written doubly linked list (the `AllOne` class).
- [`Leetcode/Dailys/16.07.2024.py`](Leetcode/Dailys/16.07.2024.py) - binary tree path directions (the longest solution in the repo).
- [`HackerRank/PreparationKits/3months/Week11/8 tree_huffman_decoding.py`](<HackerRank/PreparationKits/3months/Week11/8 tree_huffman_decoding.py>) - decoding a Huffman-encoded string by walking the tree.
- [`HackerRank/PreparationKits/3months/Week12/2 binary_search_tree_lowest_common_ancestor.py`](<HackerRank/PreparationKits/3months/Week12/2 binary_search_tree_lowest_common_ancestor.py>) - lowest common ancestor in a BST.

## How to navigate and run

Each file is a standalone solution; there is nothing to install.

- **LeetCode** files contain a `class Solution` (the format LeetCode expects). Copy the class into the LeetCode editor, or import it in your own script. Some files rely on LeetCode's own helpers (e.g. `TreeNode`, `Optional`), which are shown in comments at the top.
- **HackerRank** and **Codeforces** files are plain scripts that read from standard input:

```
python "HackerRank/PreparationKits/3months/Week1/1 plus_minus.py"
```

Problem names are not translated into titles for LeetCode files, so use the problem number (or the date for Dailys) to look the task up on the site.

## Repository layout

```
Project-S
├── Leetcode
│   ├── Dailys          <DD.MM.YYYY>.py          (01.05.2024 - 08.12.2024)
│   ├── Contests        <Weekly|Biweekly N>/<problem #>.py
│   ├── Study plans     <plan name>/<problem #>.py   (TopInterview150)
│   └── Others          <problem #>.py
├── HackerRank
│   └── PreparationKits <kit name>/Week<N>/<#> <problem_name>.py   (3months)
└── Codeforces
    ├── Contests        <contest name>/<problem letter>.py
    ├── Problemsets     <list name>/link.txt   (link to the source of the problem list)
    └── Others          <contest id + letter> <problem_name>.py   (e.g. 1790A polycarp_and_the_day_of_pi.py)
```

P.S. A file for one LeetCode solution may contain several "Solution" classes (several approaches found) or a re-solution if, for example, the daily task had already appeared before📆.

## License

Released under the [BSD 3-Clause License](LICENSE). Feel free to read, learn from and reuse the code under its terms - but please try solving the problem yourself first😉. Happy coding💻!
