class Transaction:
    def __init__(self, sender, recipient, amount ) :
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def validate(self, blockchain):
        sum = 0
        for block in blockchain.chain:
            for transaction in block["transaction"]:
                if transaction.sender==self.sender:
                    sum-=transaction.amount
                elif transaction.recipient==self.recipient:
                    sum+=transaction.amount
