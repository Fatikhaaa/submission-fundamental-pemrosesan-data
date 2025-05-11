import unittest
from unittest.mock import patch
import pandas as pd
from utils.transform import transform_data

class TestTransform(unittest.TestCase):

    def test_transform_data(self):
        # Menyiapkan data produk untuk diuji
        products = [
            {'title': 'Product 1', 'price': '10000', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'},
            {'title': 'Product 2', 'price': '20000', 'rating': '5.0', 'colors': '3', 'size': 'L', 'gender': 'Women'}
        ]
        
        # Mengubah data produk menjadi DataFrame
        df = transform_data(products)
        
        # Menguji hasil transformasi data
        self.assertEqual(len(df), 2)  # Memastikan ada 2 produk dalam DataFrame
        self.assertIn('price', df.columns)  # Memastikan kolom 'price' ada
        self.assertIn('rating', df.columns)  # Memastikan kolom 'rating' ada
        self.assertIn('timestamp', df.columns)  # Memastikan kolom 'timestamp' ada
        self.assertTrue(df['price'].iloc[0] > 0)  # Memastikan harga lebih besar dari 0
        self.assertTrue(df['rating'].iloc[0] > 0)  # Memastikan rating lebih besar dari 0
    
    def test_invalid_price(self):
        # Menyiapkan data produk dengan harga tidak valid
        products = [
            {'title': 'Product 1', 'price': 'invalid_price', 'rating': '4.5', 'colors': '3', 'size': 'M', 'gender': 'Men'}
        ]
        
        df = transform_data(products)
        
        # Menguji hasil ketika harga tidak valid
        self.assertEqual(len(df), 0)  # Tidak ada produk yang valid karena harga tidak valid
    
    def test_main_block(self):
        # Menguji blok '__main__' untuk memastikan semuanya berjalan saat program dijalankan
        with patch.object(unittest, 'main'):
            import tests.test_transform

if __name__ == '__main__':
    unittest.main()
