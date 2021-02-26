#!/usr/bin/env python3

from Block import Block

blockchain = []
blockNum = 0

def getBlockNumber():
  global blockNum
  blockNum += 1
  return blockNum

def mine(number, prev_hash, data):
  nonce = 0
  while True:
    block = Block(number, nonce, prev_hash, data)
    if block.hash.startswith("0"):
      return block
    else:
      nonce += 1

genesis_block = mine(getBlockNumber(), "This is a test str", ["hello"])

print(genesis_block.hash)

