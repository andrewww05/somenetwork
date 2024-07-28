# Some Network Project

## Description

This is a simple open-source blog application created for fun while learning Flask. It is a work-in-progress project designed to demonstrate various Flask features and web development concepts.

## Features

- **User Authentication**: Sign up, login, and manage user accounts.
- **Blog Posts**: Create, edit, delete, and view blog posts.
- **Comments**: Add comments to blog posts.
- **Responsive Design**: Accessible on various devices with a responsive layout.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/some-network-project.git
   ```

2. **Navigate to the project directory**:

   ```sh
   cd some-network-project
   ```

3. **Create and activate a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate     # Windows
   ```

4. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

## Environment Configuration

Create a `.env` file in the root of the project directory and add the following environment variables:

- **PORT**: The port on which the Flask application will run. Default is usually 5000.

  ```plaintext
  PORT=5000
  ```

- **DATABASE_URI**: The URI for the database. For SQLite, it would look something like:

  ```plaintext
  DATABASE_URI=sqlite:///instance/database.db
  ```

  For other databases like PostgreSQL or MySQL, it might look like:

  ```plaintext
  DATABASE_URI=postgresql://user:password@localhost/dbname
  ```

- **SECRET_KEY**: A secret key used for session management and security purposes.

  ```plaintext
  SECRET_KEY=your_secret_key_here
  ```

## Running the Application

1. **Install all dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

2. **Run the Flask application**:

   ```sh
   flask run
   ```

   By default, the application will run on `http://127.0.0.1:5000`.

## Usage

- Visit `http://127.0.0.1:5000` in your browser to start using the application.
- You can create new blog posts, add comments, and manage user accounts.

## Contributing

Feel free to open issues and submit pull requests if you have improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
