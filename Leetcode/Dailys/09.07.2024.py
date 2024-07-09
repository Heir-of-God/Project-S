class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        n: int = len(customers)
        time_waiting: int = customers[0][1]
        finished_prev = customers[0][0] + customers[0][1]

        for customer_ind in range(1, n, 1):
            times: list[int] = customers[customer_ind]
            arrive: int = times[0]

            # chef starts cook this as soon as he finished last dish or customer arrived
            start_cook: int = max(arrive, finished_prev)
            end_time: int = start_cook + times[1]
            finished_prev: int = end_time
            time_waiting += end_time - arrive

        return time_waiting / n
