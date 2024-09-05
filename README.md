# Google Books Search App

This is a Flask web application that allows users to search for books using the Google Books API. The user can enter a query (e.g., book title, author) in a search form, and the app will display the matching books with details such as the title, author(s), and description.

## Features

- **Book Search**: Users can search for books by entering a query (e.g., book title or author).
- **Google Books API Integration**: The app fetches book data from the Google Books API.
- **Search Results Display**: Results are displayed on the same page, with book titles, authors, and descriptions.
- **Error Handling**: Displays error messages for issues such as empty queries or failed API requests.
- **Responsive UI**: Clean and simple user interface.

## Requirements

Make sure you have the following installed:

- Python 3.x
- Flask
- Requests

You can install the required Python packages using pip:

```bash
pip install flask
pip install flask requests
