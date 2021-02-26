import hashlib


class Block:
    next = None
    nonce = 0
    hash = ""

    def __init__(self, number, prev_hash, data):
        # assign parameters to class variables
        self.data = data
        self.number = number
        self.prev_hash = prev_hash

    def mine(self, rule):
        while True:
            self.calculate_hash()
            if self.hash.startswith(rule):
                break
            else:
                self.nonce += 1

    def calculate_hash(self):
        # create string to be hashed
        str_to_hash = str(self.number) + "".join(self.data) + self.prev_hash + str(self.nonce)

        # calculate hash
        self.hash = hashlib.sha256(str_to_hash.encode()).hexdigest()

    def print(self):
        print("Number: ", self.number)
        print("Nonce: ", self.nonce)
        print("Hash: ", self.hash)
        print("Prev Hash: ", self.prev_hash)
        print("Data: ", self.data)
        print("-------------------")

