class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        busToStop = defaultdict(set)
        q = collections.deque([(source, 0)])

        for bus, stops in enumerate(routes):
            for s in stops:
                busToStop[s].add(bus)

        busStops = set()
        busses = set()

        while q:
            stop, busC = q.popleft()

            if stop == target:
                return busC

            for b in busToStop[stop]:
                if b not in busses:
                    busses.add(b)
                    
                    for stops in routes[b]:
                        if stops not in busStops:
                            busStops.add(stops)
                            q.append((stops, busC + 1))
        return -1
