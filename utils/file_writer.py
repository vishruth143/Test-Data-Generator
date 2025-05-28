import os

def write_to_csv(df, filename, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(f"{output_dir}/{filename}.csv", index=False)

def write_to_excel(df, filename, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    df.to_excel(f"{output_dir}/{filename}.xlsx", index=False)