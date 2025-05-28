from generators.order_generator import OrderGenerator
from utils.file_writer import write_to_csv, write_to_excel

if __name__ == "__main__":
    schema_file = "data_schemas/orders_schema.json"
    order_gen = OrderGenerator(schema_file)

    df = order_gen.generate_orders(count=1000000)

    write_to_csv(df, "orders_sample")
    write_to_excel(df, "orders_sample")
    print("Test data generated successfully!")