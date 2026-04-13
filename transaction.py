class Transaction:
    def __init__(self, sender, recipient, amount ) :
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def validate(self, blockchain):
        balance= 0
        for block in blockchain.chain:
            for transaction in block["transactions"]:
                if transaction[sender]==self.sender:
                    balance-=transaction[amount]
                elif transaction[recipient]==self.sender:
                    balance+=transaction[amount]

        return balance>=self.amount
