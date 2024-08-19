import heapq


class Solution:
    def topStudents(
        self,
        positive_feedback: list[str],
        negative_feedback: list[str],
        report: list[str],
        student_id: list[int],
        k: int,
    ) -> list[int]:
        n: int = len(student_id)
        pos: set[int] = set(positive_feedback)
        neg: set[int] = set(negative_feedback)
        res: list[tuple[int, int]] = []  # tuple(score, id)

        for ind in range(n):
            feedback: list[str] = report[ind].split()
            score = 0
            for word in feedback:
                if word in pos:
                    score += 3
                elif word in neg:
                    score -= 1
            res.append((score, student_id[ind]))

        topk: list[tuple[int, int]] = heapq.nsmallest(k, res, key=lambda obj: (-obj[0], obj[1]))
        return [obj[1] for obj in topk]
