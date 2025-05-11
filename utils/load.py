import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from sqlalchemy import create_engine

def save_to_csv(df, filename="products.csv"):
    """
    Save data to CSV file.
    """
    df.to_csv(filename, index=False)

def save_to_google_sheets(df, spreadsheet_id, range_name):
    """
    Save data to Google Sheets.
    """
    # Menggunakan kredensial dari file service account
    creds = Credentials.from_service_account_file('project-etl-459518-eac077deb7c9.json')
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Konversi DataFrame ke lists
    values = df.values.tolist()
    body = {
        'values': values
    }

    # Update data di Google Sheets
    sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

def load_to_postgresql(df, table_name='products'):
    """
    Save data to PostgreSQL database.
    """
    try:
        # Setting koneksi ke PostgreSQL
        username = 'postgres'
        password = 'root'
        host = 'localhost'
        port = '5432'
        database = 'product'

        # Membuat engine SQLAlchemy untuk koneksi ke PostgreSQL
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

        # Simpan DataFrame ke tabel PostgreSQL (replace apabila tabel sudah ada)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data has been successfully saved to the PostgreSQL table '{table_name}'.")

    except Exception as e:
        print(f"Failed save to PostgreSQL: {e}")
