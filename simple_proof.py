import hashlib
import json


class Block:
    """[summary]
    block for blockchain
    """

    id = None
    history = None
    parent_id = None
    parent_hash = None


if __name__ == "__main__":
    block_A = Block()
    block_A.id = 1
    block_A.history = 'Nelson likes cat'

    block_B = Block()
    block_B.id = 2
    block_B.history = 'Marie likes dog'
    block_B.parent_id = block_A.id
    block_B.parent_hash = hashlib.sha256(json.dumps(
        block_A.__dict__).encode('utf-8')).hexdigest()

    block_C = Block()
    block_C.id = 3
    block_C.history = 'Marie likes dog'
    block_C.parent_id = block_B.id
    block_C.parent_hash = hashlib.sha256(json.dumps(
        block_B.__dict__).encode('utf-8')).hexdigest()

    block_d = Block()
    block_d.id = 4
    block_d.history = "sky love"
    block_d.parent_id = block_C.id

    import json
    block_serialized = json.dumps(block_d.__dict__).encode("utf-8")
    print(block_serialized)
    # mini mining
    import hashlib
    payload_string = '{"history": "Sky loves turtle", "parent_id": 3, "id": 4}'
    payload_bytes = bytes(payload_string, 'utf-8')
    for i in range(1000000):
        nonce = str(i).encode('utf-8')
        result = hashlib.sha256(payload_bytes + nonce).hexdigest()
        if result[0:5] == '00000':
            print("The answer to puzzle: " + str(i))
            print("Input to hash is: " + payload_string + str(i))
            print("Output hash which has 5 leading zeros: " + result)
            break
