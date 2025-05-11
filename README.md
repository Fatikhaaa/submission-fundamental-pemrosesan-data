# Submission Belajar Fundamental Pemrosesan Data : Proyek Akhir Membangun ETL Pipelines

## Project Description
Proyek ini merupakan submission akhir dari modul Belajar Fundamental Pemrosesan Data yang mengimplementasikan alur ETL (Extract, Transform, Load) untuk mengolah data produk dari website e-commerce. Proyek ini dibangun dengan Python dan menggunakan berbagai library seperti Pandas, BeautifulSoup, dan SQLAlchemy.

## Key Features
### Extraction
- Web scraping produk dari website e-commerce
- Support pagination (50 halaman)
- Error handling untuk failed requests

### Transformation
- Pembersihan dan normalisasi data
- Konversi format harga
- Transformasi rating produk
- Penambahan kolom baru (harga dalam Rupiah)

### Loading Data
- CSV file export
- Google Sheets API integration
- PostgreSQL database storage

## Installation Guide

### Prasyarat
- Python 3.10 or later
- PostgreSQL database
- Google Cloud Platform account (for Sheets API)

### Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/yourusername/project-etl.git
cd project-etl
```
2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Configure environment:
Create .env file with:
```ini
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=product
GSHEETS_CREDENTIALS=credentials.json
GSHEETS_SHEET_ID=your_sheet_id
```

### Usage
1. Running the Pipeline
```bash
python main.py
```
3. Testing
```bash
# Run tests
python -m unittest discover tests

# With coverage
coverage run -m unittest discover tests
coverage report
```
