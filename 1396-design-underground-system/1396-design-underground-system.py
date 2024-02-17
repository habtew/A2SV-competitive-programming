class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.checkouts = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins[id]
        out_time = t - start_time
        key = (start_station, stationName)
        
        if key in self.checkouts:
            total_time, count = self.checkouts[key]
            self.checkouts[key] = (total_time + out_time, count + 1)
        else:
            self.checkouts[key] = (out_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        total_time, count = self.checkouts.get(key, (0, 0))
        return total_time / count if count > 0 else 0.0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)