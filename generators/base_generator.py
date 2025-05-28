from faker import Faker

class BaseGenerator:
    def __init__(self):
        self.fake = Faker()