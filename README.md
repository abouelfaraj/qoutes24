# My Flask QOUTES24

## Description

Welcome to "QUOTES," an immersive web application designed to ignite inspiration and foster connections through the power of words. With a seamless integration of front-end accessibility and robust back-end functionality, "QUOTES" offers a comprehensive platform for discovering, sharing, and contributing to a curated collection of insightful quotes.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/abouelfaraj/qoutes24.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd qoutes24
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Create a MySQL database named `quotes_db`.
    - Configure your database connection parameters in `models/engine/db_storage.py`.
    - Run the following command to initialize the database:

        ```bash
        python3 models/engine/db_storage.py
        ```

5. **Run the Flask application:**

    ```bash
    python3 qoutes24/app.py
    ```

## Usage

- Visit `http://localhost:5000` in your web browser to access the application.
- You can register as a new user or log in with existing credentials.
- Once logged in, you can manage quotes, categories, reviews, etc.

## Project Structure

Quotes-24/
│
│ ├── routes/
│ │ └── routes.py
│
├── templates/
│ ├── front/
| ├────── index.html
│ ├────── login.html
│ └────── landing.html
│ ├── admin/
| ├────── index.html
│ ├────── dashboard.html
│ └────── list-quotes.html
│ └────── list-categories.html
│ └────── account.html
|
├── models/
│ ├── init.py
│ ├── base_model.py
│ ├── engine/
│ │ └── db_storage.py
│ ├── quote.py
│ ├── quote_category.py
│ ├── review.py
│ ├── role.py
│ ├── user.py
│ └── user_detail.py
│
├── static/
│ └── css/
│ └── style.css
│ └── bootstrap.css
│ └── ..
|
├── app.py
├── requirements.txt
└── README.md

## Technologies Used

- Python
- Flask
- SQLAlchemy
- MySQL

## Contributors

- [Abou el faraj ayoub](https://github.com/abouelfaraj)

## License

Alx license.
