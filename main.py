from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, load_to_postgresql

def main():
    base_url = 'https://fashion-studio.dicoding.dev/'
    all_products = []

    # Melakukan data scraping pada halaman utama tanpa pagination
    print(f"Mulai scraping halaman utama: {base_url}")
    try:
        products = scrape_main(base_url)
        all_products.extend(products)
    except Exception as e:
        print(f"Failed to scrape main page: {e}")

    # Melakukan scraping pada halaman 2 sampai dengan 50
    for page in range(2, 51):
        url = f"{base_url}page{page}"
        print(f"Started scraping page {page}: {url}")
        try:
            products = scrape_main(url)
            all_products.extend(products)
        except Exception as e:
            print(f"Failed to scrape page {page}: {e}")

    # Proses data yang telah diambil (transform data)
    transformed_data = transform_data(all_products)
    
    # Menyimpan data ke berbagai format
    save_to_csv(transformed_data)
    load_to_postgresql(transformed_data)

    # Simpan ke Google Sheets
    save_to_google_sheets(
        transformed_data,
        '15ZUjmgUdMshETn983S3gXEMVkX9CuJocZMXbFAzYi-Y',
        'SHEET1!A2'
    )

if __name__ == '__main__':
    main()
