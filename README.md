# Portfolio
# Flask E-commerce Website

This is a Flask E-commerce website that allows users to browse through products, add them to cart and purchase them. The website has a cart and payment system that accepts Stripe payments.

![home_page](https://user-images.githubusercontent.com/54271054/127762413-9e5ebf6b-fd6d-4f5c-851b-5b5a5f4e33d4.PNG)

![product_detail_page](https://user-images.githubusercontent.com/54271054/127762461-904d734f-fdb8-4cd9-bc91-0f15fde6895a.PNG)

![cart_page](https://user-images.githubusercontent.com/54271054/127762491-4d68faa5-0b0a-4e47-bb16-141d19059f2c.PNG)

![checkout_page](https://user-images.githubusercontent.com/54271054/127762504-fc57e00d-891c-4653-9b9f-2cf80b7cda24.PNG)

![success_page](https://user-images.githubusercontent.com/54271054/127762524-9f06e704-af38-46d3-8b7e-008f369d7faa.PNG)

## Features

- User authentication system that allows users to register, login and logout.
- Products browsing system that allows users to browse through products and view their details.
- Cart system that allows users to add and remove products from their cart.
- Payment system that accepts Stripe payments.
- Purchase history system that allows users to view their past purchases.

## Technologies Used

- Python 3.9.1
- Flask 2.0.1
- SQLite
- SQLAlchemy 1.4.25
- Flask-WTF 0.15.1
- WTForms 2.3.3
- Flask-Login 0.5.0
- Flask-Migrate 3.1.0
- Stripe API

## Installation and Setup

1. Clone the repository:
Here's the raw readme file for the ecommerce site Flask repository on GitHub:

markdown
Copy code
# Flask E-commerce Website

This is a Flask E-commerce website that allows users to browse through products, add them to cart and purchase them. The website has a cart and payment system that accepts Stripe payments.

![home_page](https://user-images.githubusercontent.com/54271054/127762413-9e5ebf6b-fd6d-4f5c-851b-5b5a5f4e33d4.PNG)

![product_detail_page](https://user-images.githubusercontent.com/54271054/127762461-904d734f-fdb8-4cd9-bc91-0f15fde6895a.PNG)

![cart_page](https://user-images.githubusercontent.com/54271054/127762491-4d68faa5-0b0a-4e47-bb16-141d19059f2c.PNG)

![checkout_page](https://user-images.githubusercontent.com/54271054/127762504-fc57e00d-891c-4653-9b9f-2cf80b7cda24.PNG)

![success_page](https://user-images.githubusercontent.com/54271054/127762524-9f06e704-af38-46d3-8b7e-008f369d7faa.PNG)

## Features

- User authentication system that allows users to register, login and logout.
- Products browsing system that allows users to browse through products and view their details.
- Cart system that allows users to add and remove products from their cart.
- Payment system that accepts Stripe payments.
- Purchase history system that allows users to view their past purchases.

## Technologies Used

- Python 3.9.1
- Flask 2.0.1
- SQLite
- SQLAlchemy 1.4.25
- Flask-WTF 0.15.1
- WTForms 2.3.3
- Flask-Login 0.5.0
- Flask-Migrate 3.1.0
- Stripe API

## Installation and Setup

1. Clone the repository:

git clone https://github.com/Edwinngera/Portfolio.git

2. Create and activate a virtual environment:

python -m venv env
source env/bin/activate

3. Install the required dependencies:

pip install -r requirements.txt

4. Set up the database by running:

flask db init
flask db migrate
flask db upgrade



5. Create a `.env` file and add your Stripe API keys:

STRIPE_PUBLIC_KEY=<your_public_key>
STRIPE_SECRET_KEY=<your_secret_key>

6. Start the server:

flask run

## Usage

Browse products by clicking on the "Shop" link in the navigation menu
Add products to cart by clicking the "Add to Cart" button on a product page
View cart and checkout by clicking the "Cart" link in the navigation menu
Login or create an account to access the admin dashboard at /admin
Add or edit products and view orders in the admin dashboard


## Future Improvements

- Adding the ability to filter products based on category, price and other attributes.
- Adding a search bar for users to search for specific products.
- Adding the ability to rate and review products.
- Adding a wishlist system that allows users to save products for later.
- Improving the UI/UX of the website.

## Author

- [Edwin Ng'era](https://www.github.com/Edwinngera)










