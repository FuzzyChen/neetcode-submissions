class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[] for _ in range(n)]

        for s, d, cost in flights:
            adj[s].append((d, cost))

        # cost, city, flights_taken
        minH = [(0, src, 0)]

        # best[city][number of flights] = minimum cost
        best = [[float('inf')] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while minH:
            cost, city, flights_taken = heapq.heappop(minH)

            if city == dst:
                return cost

            if flights_taken == k + 1:
                continue

            # Skip outdated heap entries
            if cost > best[city][flights_taken]:
                continue

            for next_city, next_cost in adj[city]:
                new_cost = cost + next_cost
                new_flights = flights_taken + 1

                if new_cost < best[next_city][new_flights]:
                    best[next_city][new_flights] = new_cost
                    heapq.heappush(
                        minH,
                        (new_cost, next_city, new_flights)
                    )

        return -1