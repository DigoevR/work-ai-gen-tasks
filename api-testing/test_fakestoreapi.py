import requests

API_URL = 'https://fakestoreapi.com/products'

def main():
    response = requests.get(API_URL)
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    products = response.json()
    defects = []

    for product in products:
        product_defects = []
        # Check title
        if not product.get('title'):
            product_defects.append('Missing or empty title')
        # Check price
        if product.get('price', 0) < 0:
            product_defects.append('Negative price')
        # Check rating.rate
        rating = product.get('rating', {})
        if rating.get('rate', 0) > 5:
            product_defects.append('Rating.rate exceeds 5')
        if product_defects:
            defects.append({
                'id': product.get('id'),
                'title': product.get('title'),
                'defects': product_defects
            })

    if defects:
        print("\nProducts with defects:")
        for d in defects:
            print(f"ID: {d['id']}, Title: {d['title']}, Defects: {', '.join(d['defects'])}")
    else:
        print("\nNo defects found.")

if __name__ == '__main__':
    for _ in range(10):
        main() 