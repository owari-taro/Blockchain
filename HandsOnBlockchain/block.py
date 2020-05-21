import hashlib
import json


class Block:
    def __init__(self, block_id, history, parent: Block = None, parent_hash=None):
        self.block_id = block_id
        self.history = history
        self.parent = parent
        self.parent_id = parent.id
        self.parent_hash = parent_hash

    def create_hash(self):
        return hashlib.sha256(json.dumps(
            self.__dict__).encode("utf-8")).hexdigest()

    def recalculate(self):
        current = self.parent.create_hash()
        return current == self.parent_hash


if __name__ == "__main__":
    block_A = Block(1, "nelson likes cat")
    #print(block_A.create_hash())
    #block_B = Block(2, "marie likes dog", block_A.block_id,
    #                block_A.create_hash())
    #block_C = Block(3, "marie likes dog", block_B.block_id,
     #               block_B.create_hash())
