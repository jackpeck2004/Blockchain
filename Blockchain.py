import random
from Block import Block


class Blockchain:
    # basic blockchain variables
    blockNum = 0

    # create genesis block
    # genesis = Block(0, random.randint(0, 100), hex(random.randint(0, 17012004)), "The genesis block")
    genesis = Block(0, "", "The genesis Block")

    def __init__(self, rule):
        self.rule = rule
        self.genesis.calculate_hash()

        # assign by value head to genesis
        _dummy = self.head = self.genesis

        # point block to head
        self.current_block = self.head

    def get_block_number(self) -> int:
        self.blockNum += 1
        return self.blockNum

    def add(self, block):
        self.current_block.next = block
        self.current_block = self.current_block.next
