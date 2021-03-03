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

    def get_block_number(self):
        """
        Calculates the current block number and returns it

        :return: current block number
        :rtype: int
        """
        self.blockNum += 1
        return self.blockNum

    def __block_can_be_added__(self, block):
        """
        Checks if a block respects the blockchain rule

        :param block: the block to be checked
        :return: if the block respects the blockchain rule or not
        :rtype: bool
        """
        if block.hash.startswith(self.rule):
            return True
        return False

    def add(self, block):
        """
        Checks if the block should be added to the blockchain and adds it to the blockchain

        :param block: the block to be added
        """
        if self.__block_can_be_added__(block):
            self.current_block.next = block
            self.current_block = self.current_block.next
        else:
            print("ERROR: Block", block.hash, "cannot be added.")
            return
