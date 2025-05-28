# 🧪 Test Data Generator (DataGen) — Step-by-Step Local Setup

---
## 📦 Tech Stack
**Language:** Python 3.x

**Libraries:** Faker, Pandas, SQLAlchemy, PyYAML

**Optional DB:** SQLite or PostgreSQL (for ODS simulation)

**Output Formats:** CSV / Excel

**Schema Format:** JSON

---

## 🛠️ Setup Instructions

### 1. Create the Project Folder Structure
```bash
    mkdir test_data_generator && cd test_data_generator
    
    mkdir -p data_schemas generators utils output
    touch main.py
```

### 2. Create a Virtual Environment and Install Dependencies
```bash
    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirments.txt
```

### 3. Define Your JSON Schema (for Orders)
Create a file:
📄 data_schemas/orders_schema.json

Example:

json
Copy
Edit
{
  "table_name": "orders",
  "fields": [
    {"name": "order_id", "type": "uuid"},
    {"name": "order_date", "type": "date"},
    {"name": "customer_name", "type": "name"},
    {"name": "location", "type": "city"},
    {"name": "sku", "type": "custom", "format": "SKU-####"},
    {"name": "quantity", "type": "int", "min": 1, "max": 100},
    {"name": "priority_level", "type": "int", "min": 1, "max": 5},
    {"name": "status", "type": "enum", "values": ["PENDING", "SHIPPED", "DELIVERED", "CANCELLED"]}
  ]
}
### 4. Base Generator Class
**Create:**
📄 generators/base_generator.py

Implements common setup and Faker instance.

### 5. Order Generator Using Schema
**Create:**
📄 generators/order_generator.py

Reads schema and generates data based on each field type.

### 6. File Writer Utility
**Create:**
📄 utils/file_writer.py

Writes generated data to CSV or Excel.

### 7. Main Script to Run Everything
**Create:**
📄 main.py

Controls the overall flow — loads schema, calls generator, writes to file.

### 8. Run the Python DataGen
```bash
    python main.py
```
