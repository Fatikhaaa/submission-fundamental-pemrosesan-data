import requests
from bs4 import BeautifulSoup

def scrape_main(url):
    try:
        # Mengirimkan request ke URL dan menangani timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Mengecek apabila status code bukan 200, maka raise exception
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to access URL: {url}. Detail: {e}")
    
    try:
        # Gunakan BeautifulSoup untuk parsing HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        
        # Validasi untuk mengecek struktur HTML parsing sesuai apa tidak
        if not soup.find_all('div', class_='collection-card'):
            raise Exception("Failed to parse HTML: Invalid or missing HTML structure.")
        
        # Loop untuk mengekstrak data produk dari setiap card
        for card in soup.find_all('div', class_='collection-card'):
            title_tag = card.find('h3', class_='product-title')
            title = title_tag.text.strip() if title_tag else 'Unknown Title'
            
            price_tag = card.find('div', class_='price-container')
            price = price_tag.text.strip() if price_tag else 'Price Unavailable'
            
            rating_tag = card.find('p', string=lambda text: text and 'Rating' in text)
            rating = rating_tag.text.strip() if rating_tag else 'No Rating Info'
            
            colors_tag = card.find('p', string=lambda text: text and 'Colors' in text)
            colors = colors_tag.text.strip() if colors_tag else 'No Color Info'
            
            size_tag = card.find('p', string=lambda text: text and 'Size' in text)
            size = size_tag.text.strip() if size_tag else 'No Size Info'
            
            gender_tag = card.find('p', string=lambda text: text and 'Gender' in text)
            gender = gender_tag.text.strip() if gender_tag else 'No Gender Info'
            
            # Menambahkan produk ke dalam list
            products.append({
                'title': title,
                'price': price,
                'rating': rating,
                'colors': colors,
                'size': size,
                'gender': gender
            })
        
        # Mengecek apakah ada produk yang ditemukan
        if not products:
            raise Exception("No products found")
            
        return products
    
    except Exception as e:
        raise Exception(f"Failed to parse: {str(e)}")
