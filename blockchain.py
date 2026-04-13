import json
import hashlib
from datetime import datetime

class Blockchain:
    def __init__(self):
        self.chain= []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = self.create_block(previous_hash=0, proof=1)
        return genesis 

    def create_block(self, previous_hash, proof):
        block = {
            "index" : len(self.chain)+1,
            "timestamp" : str(datetime.now()),
            "transactions" : self.pending_transactions,
            "previous_hash" : previous_hash,
            "proof": proof
        }
        self.pending_transactions = []
        block["hash"] = self.hash_block(block)
        self.chain.append(block)
        return block

    def hash_block(self, block):
        encoded = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def add_transactions(self, transaction):
        self.pending_transactions.append(transaction)

