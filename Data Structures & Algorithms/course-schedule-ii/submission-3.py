from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
           adj_list[src].append(dest)
           in_degree[dest] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []


        while queue:
           node = queue.popleft()
           order.append(node)
        
        # Reduce the in-degree of all neighboring courses
           for neighbor in adj_list[node]:
               in_degree[neighbor] -= 1
            # If a neighbor has no more prerequisites, add it to the queue
               if in_degree[neighbor] == 0:
                   queue.append(neighbor)
                
    # Step 4: Check for a cycle (if we couldn't take all courses)
        if len(order) == numCourses:
          return order
        else:
         return []



        