#!/usr/bin/env python3

from Block import Block
from Blockchain import Blockchain

blockchain = Blockchain()

for i in range(10):
    blockchain.mine("Block " + str(i + 1))

while blockchain.head is not None:
    blockchain.head.print()
    blockchain.head = blockchain.head.next