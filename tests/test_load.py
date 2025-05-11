import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_to_csv, save_to_google_sheets, load_to_postgresql

class TestLoad(unittest.TestCase):

    @patch('utils.load.pd.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        # Menyiapkan data frame untuk diuji
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Menyimpan data ke CSV
        save_to_csv(df, 'test.csv')
        
        # Menguji apakah fungsi to_csv dipanggil dengan argumen yang benar
        mock_to_csv.assert_called_once_with('test.csv', index=False)
    
    @patch('utils.load.build')
    @patch('utils.load.Credentials.from_service_account_file')
    def test_save_to_google_sheets(self, mock_creds, mock_build):
        # Menyiapkan data frame untuk diuji
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Menyiapkan mock untuk kredensial dan service Google Sheets
        mock_creds.return_value = MagicMock()
        mock_service = MagicMock()
        mock_build.return_value = mock_service
        
        # Memanggil fungsi untuk menyimpan data ke Google Sheets
        save_to_google_sheets(df, 'spreadsheet_id', 'Sheet1!A2')
        
        # Menguji apakah fungsi update dipanggil untuk memperbarui data
        mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()
    
    @patch('utils.load.create_engine')
    def test_load_to_postgresql_success(self, mock_create_engine):
        # Menyiapkan data frame untuk diuji
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Menyiapkan mock untuk engine SQLAlchemy
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        
        # Memanggil fungsi untuk menyimpan data ke PostgreSQL
        with patch('pandas.DataFrame.to_sql') as mock_to_sql:
            load_to_postgresql(df)
        
        # Menguji apakah fungsi to_sql dipanggil untuk menyimpan data
        mock_to_sql.assert_called_once()
    
    @patch('utils.load.create_engine')
    def test_load_to_postgresql_failure(self, mock_create_engine):
        # Menyiapkan data frame untuk diuji
        df = pd.DataFrame({
            'title': ['Product 1', 'Product 2'],
            'price': [10000, 20000],
            'rating': [4.5, 5.0]
        })
        
        # Menyiapkan mock untuk error koneksi database
        mock_create_engine.side_effect = Exception("Database connection error")
        
        # Menguji apakah pesan error tercetak saat terjadi kegagalan
        with patch('builtins.print') as mock_print:
            load_to_postgresql(df)
            self.assertIn("Failed save to PostgreSQL", mock_print.call_args_list[0][0][0])
    
    def test_main_block(self):
        # Menguji blok utama untuk memastikan '__main__' berjalan
        with patch.object(unittest, 'main'):
            import tests.test_load

if __name__ == '__main__':
    unittest.main()
