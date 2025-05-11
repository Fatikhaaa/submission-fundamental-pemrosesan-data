import pandas as pd
import numpy as np
from datetime import datetime
import warnings

# Mengabaikan warning terkait perubahan di masa depan
warnings.simplefilter(action='ignore', category=FutureWarning)

# Setting pandas untuk memperlihatkan peringatan downcasting
pd.set_option('future.no_silent_downcasting', True)

def transform_data(products):
    # Mengubah data produk menjadi DataFrame
    df = pd.DataFrame(products)
    
    # Menghapus baris dengan title 'unknown product'
    df = df[df['title'].str.lower() != 'unknown product']
    
    # Membersihkan harga dan mengonversinya ke format float dan ke satuan rupiah
    df['price'] = df['price'].replace(r'[^\d.]', '', regex=True)
    df['price'] = df['price'].replace('', np.nan)
    df.dropna(subset=['price'], inplace=True)
    
    # Mengonversi harga ke float dan mengalikannya dengan nilai tukar
    df['price'] = df['price'].astype(float) * 16000
    
    # Membersihkan dan mengonversi rating
    df['rating'] = df['rating'].replace(r'[^0-9.]', '', regex=True)
    df['rating'] = df['rating'].replace('', np.nan)
    df.dropna(subset=['rating'], inplace=True)
    
    # Mengonversi rating menjadi tipe data float
    df['rating'] = df['rating'].astype(float)
    
    # Membersihkan kolom colors dan hanya menyisakan angka saja
    df['colors'] = df['colors'].replace(r'\D', '', regex=True)
    df['colors'] = df['colors'].replace('', np.nan)
    df.dropna(subset=['colors'], inplace=True)
    
    # Mengonversi colors menjadi tipe data integer
    df['colors'] = df['colors'].astype(int)
    
    # Membersihkan kolom size dan gender
    df['size'] = df['size'].replace(r'Size:\s*', '', regex=True)
    df['gender'] = df['gender'].replace(r'Gender:\s*', '', regex=True)
    
    # Menghapus baris yang memiliki duplikasi dan nilai null
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    # Tambahkan kolom timestamp dengan format tanggal dan waktu saat ini
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return df
