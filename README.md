# MobileStore - E-Commerce Platform

A modern, fully responsive e-commerce platform for selling mobile phones built with Django and designed for all screen sizes.

## 🌟 Features

### User Features
- **Product Browsing**: Browse products with responsive grid layout (3 columns on desktop, 2 on tablet, 1 on mobile)
- **Shopping Cart**: Add products to cart, update quantities, remove items
- **Checkout System**: Complete order placement with order review
- **Order Management**: Track and view all past orders with delivery status
- **User Authentication**: Secure login, registration, and password management
- **Responsive Design**: Fully responsive layout optimized for all devices (480px - 4K)
- **Banner Slider**: Automatic carousel with navigation controls

### Admin Features
- **Dashboard**: Quick overview of sales and orders
- **Product Management**: Add, edit, and manage product inventory
- **Order Management**: View all orders with status tracking
- **User Management**: View and manage registered users
- **Sales Reports**: Detailed revenue and order analytics
- **Admin Authentication**: Secure admin-only access

## 🛠 Tech Stack

### Backend
- **Django 5.2.10**: Web framework
- **Python 3.x**: Programming language
- **SQLite**: Database (development)
- **Django ORM**: Database abstraction

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling with custom properties and media queries
- **JavaScript**: Interactive features
- **Font Awesome 6.0.0**: Icons
- **Google Fonts**: Typography (Inter, Outfit)

### Key Libraries
- **Django Auth**: User authentication and permissions
- **Django Migrations**: Database versioning
- **PIL/Pillow**: Image handling

## 📋 Project Structure

```
mobile_store/
├── main/                          # Main app (home, collections, about, contact)
│   ├── models.py                  # Product model
│   ├── views.py                   # Home, collections, pages views
│   ├── urls.py                    # Main app URL routing
│   ├── auth_views.py              # Logout functionality
│   └── migrations/
│
├── user/                          # User app (cart, orders, authentication)
│   ├── models.py                  # Order, Cart, CartItem models
│   ├── views.py                   # Cart, checkout, order views
│   ├── urls.py                    # User app URL routing
│   ├── admin.py                   # Admin panel configuration
│   └── migrations/
│
├── adminuser/                     # Admin app (dashboard, management)
│   ├── models.py                  # (inherited from auth)
│   ├── views.py                   # Dashboard, product, order management
│   ├── urls.py                    # Admin app URL routing
│   ├── admin.py                   # Admin models registration
│   └── migrations/
│
├── mobile_store/                  # Project settings
│   ├── settings.py                # Django configuration
│   ├── urls.py                    # Main URL router
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
│
├── templates/                     # HTML templates
│   ├── base.html                  # Base template
│   ├── nav.html                   # Navigation bar
│   ├── footer.html                # Footer
│   ├── main/                      # Main app templates
│   │   ├── home.html
│   │   ├── collections.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── login.html
│   │   └── register.html
│   ├── user/                      # User app templates
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── product_list.html
│   │   ├── place_order.html
│   │   └── my_orders.html
│   └── adminuser/                 # Admin templates
│       ├── login.html
│       ├── dashboard.html
│       ├── add_product.html
│       ├── users.html
│       ├── orders.html
│       └── sales_report.html
│
├── static/
│   ├── css/
│   │   └── style.css              # Main stylesheet with responsive design
│   └── js/
│       └── script.js              # JavaScript utilities
│
├── media/
│   ├── banner/                    # Hero slider images
│   │   ├── banner1.png
│   │   ├── banner2.png
│   │   └── banner3.png
│   └── products/                  # Product images
│
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django management script
└── requirements.txt               # Python dependencies
```

## 📦 Database Models

### Product (main/models.py)
```python
- brand: CharField
- name: CharField
- price: DecimalField
- description: TextField
- image: ImageField
- created_at: DateTimeField
```

### Cart & CartItem (user/models.py)
```python
Cart:
- user: OneToOneField(User)
- created_at: DateTimeField
- updated_at: DateTimeField

CartItem:
- cart: ForeignKey(Cart)
- product: ForeignKey(Product)
- quantity: PositiveIntegerField
```

### Order (user/models.py)
```python
- user: ForeignKey(User)
- product: ForeignKey(Product)
- quantity: PositiveIntegerField
- total_price: DecimalField
- order_date: DateTimeField
- status: CharField (Placed/Delivered)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Steps

1. **Clone the repository**
```bash
cd "E-Commerce Website"
cd mobile_store
```

2. **Create virtual environment (optional but recommended)**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install django pillow
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser (admin account)**
```bash
python manage.py createsuperuser
# Follow the prompts to create admin account
```

6. **Collect static files**
```bash
python manage.py collectstatic --noinput
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Website: `http://127.0.0.1:8000/`
- Django Admin: `http://127.0.0.1:8000/admin/`
- Admin Panel: `http://127.0.0.1:8000/adminuser/login/`

## 🎯 Usage Guide

### For Customers
1. **Browse Products**: Visit home or collections page
2. **Login/Register**: Create account or login
3. **Add to Cart**: Add products to shopping cart
4. **Checkout**: Review cart and complete purchase
5. **Track Orders**: View order history in "My Orders"

### For Admins
1. **Login**: Go to admin login with staff credentials
2. **Dashboard**: Access quick stats and management options
3. **Add Products**: Manage mobile phone inventory
4. **Manage Orders**: Track and update order status
5. **View Reports**: Analyze sales and revenue data

## 🎨 Responsive Design

### Breakpoints
- **Large (1025px+)**: 3-column product grid, full features
- **Medium (769px - 1024px)**: 2-column product grid
- **Small (481px - 768px)**: 1-column layout, optimized spacing
- **Extra Small (480px and below)**: Mobile-first design

### Features
- Fluid typography that scales with screen size
- Touch-friendly buttons and interactions
- Mobile-optimized navigation
- Responsive images with proper aspect ratios
- Flexible layouts using CSS Grid and Flexbox

## 🔐 Authentication & Security

- **User Registration**: Email and password validation
- **Password Storage**: Django's secure password hashing
- **Admin Access**: Staff-only authentication required
- **Session Management**: Django session framework
- **CSRF Protection**: Built-in CSRF token verification
- **Login Redirects**: Proper authentication flow with redirect support

## 🔧 Configuration

### settings.py
```python
DEBUG = True                    # Set to False in production
ALLOWED_HOSTS = []             # Add your domain
DATABASES = {                  # SQLite in development
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_URL = '/static/'        # Static files URL
MEDIA_URL = '/media/'          # Media files URL
INSTALLED_APPS = [            # Installed applications
    'main',
    'user',
    'adminuser',
]
```

## 📝 Available URLs

### Main App
```
/                          - Home page
/about/                    - About page
/contact/                  - Contact page
/collections/              - Products collection
/register/                 - User registration
/login/                    - User login
/logout/                   - User logout
```

### User App
```
/user/register/            - User registration
/user/login/               - User login
/user/products/            - Product list
/user/order/<id>/          - Place order
/user/my-orders/           - Order history
/user/cart/                - Shopping cart
/user/cart/add/<id>/       - Add to cart
/user/cart/remove/<id>/    - Remove from cart
/user/cart/update/<id>/    - Update cart item
/user/checkout/            - Checkout
```

### Admin App
```
/adminuser/login/          - Admin login
/adminuser/dashboard/      - Admin dashboard
/adminuser/users/          - User management
/adminuser/add-product/    - Add products
/adminuser/orders/         - Order management
/adminuser/sales-report/   - Sales analytics
/adminuser/logout/         - Admin logout
```

## 🚨 Error Handling

- **Authentication Errors**: Clear error messages for failed login
- **404 Errors**: User-friendly not found pages
- **Form Validation**: Client and server-side validation
- **Permission Errors**: Admin-only pages with redirect

## 🔄 Workflow

### Customer Workflow
1. Browse → Login/Register → Add to Cart → Checkout → Order Confirmation → Track Order

### Admin Workflow
1. Login → Dashboard → Manage Products/Orders/Users → View Sales Report

## 📊 Admin Features

- **Real-time Statistics**: Total revenue, order count
- **Product Management**: Add, edit, view products
- **Order Tracking**: Update delivery status, view details
- **User Directory**: View all registered customers
- **Sales Analytics**: Revenue tracking and reporting

## 🎯 Future Enhancements

- Payment gateway integration (Stripe, PayPal)
- Email notifications for orders
- Product reviews and ratings
- Search and filtering
- Wishlist functionality
- Multiple payment methods
- Inventory management
- Order tracking notifications
- Advanced analytics dashboard

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💼 Support

For issues, questions, or suggestions, please contact the development team or open an issue in the repository.

## 🙏 Acknowledgments

- Django Framework
- Font Awesome Icons
- Google Fonts
- Modern CSS techniques
- Community contributions

---

