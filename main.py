#!/usr/bin/env python3

from Block import Block
from Blockchain import Blockchain

blockchain = Blockchain("0000")

for i in range(10):
    mined_block = Block(blockchain.get_block_number(), blockchain.current_block.hash, ["Hello"])
    mined_block.mine(blockchain.rule)
    blockchain.add(mined_block)


while blockchain.head is not None:
    blockchain.head.print()
    blockchain.head = blockchain.head.next