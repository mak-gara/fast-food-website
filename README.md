# Fast Food Restaurant Website
The fast food chain's web application provides customers with an easy and convenient way to view and place orders. The main page presents various selections of products, as well as a slider designed to display important information. Information about the institution, contacts, delivery and payment can be found by users on the corresponding pages, which are accessed by clicking on the corresponding item in the navigation menu. The app also includes pages for displaying category and product listings.

The shopping cart supports standard functionality, which includes:
- adding products to the cart;
- removing from the basket;
- increase in number;
- decrease in number;
- automatic calculation of the total amount.

The shopping cart is available to both authorized users and guests.

The web application also has an administration panel that allows the establishment to easily manage content.

The application was developed using HTML, CSS and JS, the Swiper.js library was used to create sliders. The backend logic was developed using Django.

### Running this project
1. Сopy this repository
2. Install the virtual environment
```python -m venv venv```
3. Install the libraries from the requirements.txt file
```pip install -r requirements.txt```
4. Run the project with this command
```python manage.py runserver```