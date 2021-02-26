import hashlib

class Block:
  def __init__(self, number, nonce, prev_hash, data):
    self.data = data
    self.nonce = nonce
    self.number = number
    self.prev_hash = prev_hash

    str_to_hash = str(number) + "".join(data) + prev_hash + str(nonce)

    # self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
    self.hash = hashlib.sha256(str_to_hash.encode()).hexdigest()

