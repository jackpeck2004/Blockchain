from Block import Block


class Blockchain:
    # basic blockchain variables
    blockNum = 0

    # create genesis block
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

    def __block_can_be_added__(self, block):
        if block.hash.startswith(self.rule):
            return True
        return False

    def add(self, block):
        if self.__block_can_be_added__(block):
            self.current_block.next = block
            self.current_block = self.current_block.next
        else:
            return
