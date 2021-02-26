import random
from Block import Block


class Blockchain:
    # basic blockchain variables
    blockNum = 0
    rule = "0000"

    # create genesis block
    genesis = Block(0, random.randint(0, 100), hex(random.randint(0, 17012004)), "The genesis block")

    # assign by value head to genesis
    _dummy = head = genesis

    # point block to head
    block = head

    def __get_block_number__(self) -> int:
        self.blockNum += 1
        return self.blockNum

    def add(self, block):
        self.block.next = block
        self.block = self.block.next

    def mine(self, data):
        nonce = 0
        number = self.__get_block_number__()
        while True:
            block = Block(number, nonce, self.block.hash, data)
            if block.hash.startswith(self.rule):
                self.add(block)
                break
            else:
                nonce += 1


