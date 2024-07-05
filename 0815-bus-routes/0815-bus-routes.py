class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        sets_of_routes = [set(route) for route in routes]
      
        stop_to_buses_dict = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses_dict[stop].append(i)
      
        bus_graph = defaultdict(list)
        for buses in stop_to_buses_dict.values():
            num_buses = len(buses)
            for i in range(num_buses):
                for j in range(i + 1, num_buses):
                    first, second = buses[i], buses[j]
                    bus_graph[first].append(second)
                    bus_graph[second].append(first)
      
        queue = deque(stop_to_buses_dict[source])
        number_of_buses = 1
        visited_buses = set(stop_to_buses_dict[source])
      
        while queue:
            for _ in range(len(queue)):
                current_bus = queue.popleft()
              
                if target in sets_of_routes[current_bus]:
                    return number_of_buses
              
                for adjacent_bus in bus_graph[current_bus]:
                    if adjacent_bus not in visited_buses:
                        visited_buses.add(adjacent_bus)
                        queue.append(adjacent_bus)
          
            number_of_buses += 1
      
        return -1
