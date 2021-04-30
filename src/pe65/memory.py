class Memory:
    def __init__(self, size, base):
        self.size = size
        self.base = base
        self.data = bytearray(size)

    def read(self, addr):
        addr -= self.base
        if addr < 0:
            raise IndexError("invalid address", addr)
        return self.data[addr]

    def write(self, addr, newvalue):
        addr -= self.base
        if addr < 0:
            raise IndexError("invalid address", addr)
        self.data[addr] = newvalue
