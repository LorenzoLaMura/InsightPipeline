# Data Analysis

This section aims to perform data analysis using a Jupyter Notebook and requires certain environment variables to be set up in a `.env` file. The analysis involves data from a CSV file and the MySQL database, and utilizes multiple Python libraries for data manipulation and visualization.

## Project Structure

```
├── analysis.ipynb                 # Jupyter Notebook containing the analysis
├── requirements.txt               # List of Python libraries required
├── .env                           # Environment variables file (to be created by user)
└── orders.csv                     # The CSV file to analyze
```

## Requirements

- Python 3.8 or higher
- Jupyter Notebook

## Setup

1. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Create a `.env` file in the root directory of the project with the following content:**

    ```env
    MYSQL_DATABASE=ecommerce
    MYSQL_USER=pass
    MYSQL_PASSWORD=pass
    MYSQL_HOST=localhost:3306
    ```

    Replace with the actual values.