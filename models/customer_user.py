class CustomerUser:
    def __init__(self, cust_id, password, customer):
        self.cust_id = cust_id
        self.password = password  # Hash in production
        self.customer = customer

    @staticmethod
    def authenticate(cust_id, password):
        # Will be used by app.py
        return True
