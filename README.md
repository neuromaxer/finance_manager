# Finance Manager

Clever Finance Management Tool

### Prerequisites

-   Python (version 3.8 or above)
-   Node.js and npm
-   Pipenv
-   Django
-   React

### Setup & Installation

1. **Backend Setup**

    a. **Clone the repository**:

    ```bash
    git clone git@github.com:neuromaxer/finance_manager.git
    cd finance_manager
    ```

    b. **Install dependencies using pipenv**:

    ```bash
    pipenv install
    ```

    c. **Activate the pipenv shell**:

    ```bash
    pipenv shell
    ```

    d. **Apply migrations**:

    ```bash
    cd finance_manager/
    python manage.py migrate
    ```

    e. **Start the Django server**:

    ```bash
    python manage.py runserver
    ```

2. **Frontend Setup**

    a. **Navigate to the frontend directory**:

    ```bash
    cd ../frontend
    ```

    b. **Install required packages**:

    ```bash
    npm install
    ```

    c. **Start the React development server**:

    ```bash
    npm start
    ```

### Cleaning up the Database

Over time, you might want to clean up or reset the database of trades. Follow the steps below to do this:

1. **Delete the SQLite Database**:

    - If you're using the default SQLite database, simply delete the `db.sqlite3` file located in the root directory of your project.
        ```bash
        rm db.sqlite3
        ```

2. **Run Migrations Again**:

    - After deleting the SQLite database, you need to recreate the database structure.
        ```bash
        python manage.py migrate
        ```

    Remember to always backup important data before performing destructive operations on the database.

### Usage

1. **Record Trades**:

    - On the web interface, fill in the details in the form: Symbol, Quantity, Price, Time, and Type (Buy/Sell).
    - Click on "Submit" to record the trade.

2. **View Trades and Open Positions**:
    - Below the form, you'll see two tables displaying all recorded trades and netted open positions.
    - Use the "Refresh Data" button to update the tables if needed.

### Testing

-   **Backend Tests**: While inside the main `finance_manager` directory, run `python manage.py test`.
-   **Frontend Tests**: (If you have set up tests for React) Navigate to the `finance_manager/frontend` directory and run `npm test`.

### Contributing

For contributions, please create a new branch, implement your features or fixes, and submit a pull request.

### License

MIT License

### Acknowledgments
