class UndergroundSystem:

    def __init__(self):
        self.ciDict = {}
        self.coDict = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.ciDict:
            self.ciDict[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ciTuple = self.ciDict.pop(id)
        coTuple = (ciTuple[0], stationName)
        newTime = t - ciTuple[1]
        if coTuple not in self.coDict:
            self.coDict[coTuple] = [newTime]
        else:
            self.coDict[coTuple].append(newTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tKey = (startStation, endStation)
        return sum(self.coDict[tKey]) / len(self.coDict[tKey])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)