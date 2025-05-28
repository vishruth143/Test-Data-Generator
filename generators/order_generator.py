import json
import pandas as pd
import random
import time
from generators.base_generator import BaseGenerator

class OrderGenerator(BaseGenerator):
    def __init__(self, schema_file):
        super().__init__()
        with open(schema_file) as f:
            self.schema = json.load(f)

    def generate_orders(self, count=10):
        print(f"Starting data generation for {count} records...")
        start_time = time.time()

        rows = []
        fields = self.schema['fields']

        for _ in range(count):
            row = {}
            for field in fields:
                name = field['name']
                dtype = field['type']

                # Fine-grained generation using both name and type
                if name == 'order_id' and dtype == 'uuid':
                    row[name] = self.fake.uuid4()

                elif name == 'order_date' and dtype == 'date':
                    row[name] = self.fake.date_between(start_date='-1y', end_date='today')

                elif name == 'customer_name' and dtype == 'name':
                    row[name] = self.fake.name()

                elif name == 'location' and dtype == 'city':
                    row[name] = self.fake.city()

                elif name == 'sku' and dtype == 'custom':
                    row[name] = self.fake.bothify(field.get('format', 'SKU-####'))

                elif name == 'quantity' and dtype == 'int':
                    row[name] = random.randint(field.get('min', 1), field.get('max', 100))

                elif name == 'priority_level' and dtype == 'int':
                    row[name] = random.randint(field.get('min', 1), field.get('max', 5))

                elif name == 'status' and dtype == 'enum':
                    row[name] = random.choice(field.get('values', []))

                else:
                    row[name] = None  # fallback for unsupported/unknown fields

            rows.append(row)

        df = pd.DataFrame(rows)

        end_time = time.time()
        elapsed = end_time - start_time
        print(f"✅ Data generation completed in {elapsed:.2f} seconds.")

        return df
