#!/usr/bin/env python3

from Block import Block
from Blockchain import Blockchain

blockchain = Blockchain(rule="0000")


def main():
    for i in range(10):
        mined_block = Block(
            number=blockchain.get_block_number(),
            prev_hash=blockchain.current_block.hash,
            data="Block " + str(i + 1)
        )
        mined_block.mine(blockchain.rule)
        blockchain.add(mined_block)

    while blockchain.head is not None:
        blockchain.head.print()
        blockchain.head = blockchain.head.next


if __name__ == "__main__":
    main()
