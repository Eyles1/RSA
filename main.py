try:
    import RSA.functions as functions
except ModuleNotFoundError:
    import functions
import base64
import bz2

class RSA:
    def __init__(self, size=1024, seed=None):
        if seed:
            functions.setseed(seed)
        self.v = {}
        self.v["p"], self.v["q"], self.v["n"], self.v["e"], self.v["d"] = functions.createkeys(size)
        self.private = (self.v["d"], self.v["n"])
        self.public =  (self.v["e"], self.v["n"])
    
    def encode(self, m: str, reciever):
        nums = []
        for i in m:
            nums.append(str(functions.encode(*reciever, ord(i))))
        return base64.b85encode(",".join(nums).encode()).decode()
    
    def decode(self, c: str):
        nums = []
        for i in base64.b85decode(c.encode()).decode().split(","):
            nums.append(functions.decode(*self.private, int(i)))
        return "".join(chr(i) for i in nums)
