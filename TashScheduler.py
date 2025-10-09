class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many times each task appears
        count = Counter(tasks)

        # Use a max heap (simulated with negative counts, since Python has a min-heap by default)
        # Higher frequency tasks should be processed first
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0  # Total units of time (result)
        
        # Queue to keep track of tasks that are in the cooldown period
        # Each element = [remaining_count, time_when_task_can_be_reused]
        q = deque()

        # Continue until all tasks are executed (both heap and cooldown queue are empty)
        while maxHeap or q:
            time += 1  # Move time forward by 1 unit each iteration

            if not maxHeap:
                # If no available task to execute, fast-forward time to the next available cooldown completion
                time = q[0][1]
            else:
                # Pop the most frequent remaining task
                cnt = 1 + heapq.heappop(maxHeap)  # add 1 because heap stores negative counts
                
                # If there are still remaining instances of this task
                if cnt:
                    # Add it to cooldown queue; it can be used again after 'n' units
                    q.append([cnt, time + n])

            # If any task's cooldown is over at the current time, push it back into the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
