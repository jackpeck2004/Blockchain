import hashlib


class Block:
    next = None

    def __init__(self, number, nonce, prev_hash, data):
        # assign parameters to class variables
        self.data = data
        self.nonce = nonce
        self.number = number
        self.prev_hash = prev_hash

        # create string to be hashed
        str_to_hash = str(number) + "".join(data) + prev_hash + str(nonce)

        # calculate hash
        self.hash = hashlib.sha256(str_to_hash.encode()).hexdigest()

    def print(self):
        print("Number: ", self.number)
        print("Nonce: ", self.nonce)
        print("Hash: ", self.hash)
        print("Prev Hash: ", self.prev_hash)
        print("Data: ", self.data)
        print("-------------------")
