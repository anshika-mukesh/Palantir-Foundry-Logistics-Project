# Palantir Foundry: Logistics & Inventory Pipeline

An end-to-end data engineering project that transforms raw supermarket sales data into a "Digital Twin" of inventory.

## 🏗️ Architecture
- **Bronze**: Raw data ingestion from supermarket sales CSVs.
- **Silver**: Data cleaning and transformation using **PySpark**.
- **Gold**: Configured Object Action Types with Organization-level permissions to enable collaborative data management.

## 🛠️ Key Transformations
- **Column Standardization**: Renamed "Invoice ID" and "Product line" for consistency.
- **Inventory Logic**: Calculated real-time `stock_level` using a baseline of 100 units minus quantity sold.

## 🚀 Technical Stack
- **Platform**: Palantir Foundry.
- **Language**: PySpark (Python).
- **DevOps**: Managed via Foundry Code Repositories with integrated version control.
