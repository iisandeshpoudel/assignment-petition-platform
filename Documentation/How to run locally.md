# How to run locally
 This section provides a comprehensive guide on how to run the web application locally on Windows, Linux, and macOS.
### Prerequisites
 - Python 3.12
 - Git
 - Virtual Environment (optional but recommended)

### Steps to Run Locally
### 1. Clone the Repository
First, clone the repository from GitHub:
```sh
git clone https://github.com/iisandeshpoudel/assignment-petition-platform.git
```
Then, navigate to the cloned repository:
```sh
cd assignment-petition-platform
```

### 2. Set Up Virtual Environment (Optional but recommended)
Create a virtual environment to manage your project dependencies:
```sh
python -m venv venv
```
Activate the virtual environment:
    - For Windows:
    ```sh
    venv\Scripts\activate
    ```
    - For macOS or Linux:
    ```sh
    source venv/bin/activate
    ```

### 3. Install Dependencies
Install the required dependencies using pip:
```sh
pip install -r requirements.txt
```
### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```sh
SECRET_KEY=your_secret_key
```
### 5. Apply Migrations
Apply database migrations to set up your database schema:
```sh
python manage.py migrate
```
### 6. Run the Development Server
Start the development server:
```sh
python manage.py runserver
```
### 7. Access the Application
Open your browser and navigate to http://127.0.0.1:8000.
### Additional Notes
Ensure you have the correct Python version installed.
Use `python manage.py runserver` to start the server.
Use `python manage.py migrate` to apply migrations.
Use `python manage.py createsuperuser` to create a superuser.
Use `python manage.py collectstatic` to collect static files.