class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.authentication = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.authentication[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.authentication and (self.timeToLive + self.authentication[tokenId] > currentTime):
            self.authentication[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count  = 0
        for val in self.authentication.values():
            if val + self.timeToLive > currentTime:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)