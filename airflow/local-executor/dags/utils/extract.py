import pandas as pd
from sqlalchemy import create_engine

def extract_data(file_path, db_config, **kwargs):
    engine = create_engine(f'mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}')
    orders = extract_from_csv(file_path)
    categories, sellers, products = extract_from_db(engine)
    
    # Push XComs to be used by downstream tasks
    kwargs['ti'].xcom_push(key='orders', value=orders)
    kwargs['ti'].xcom_push(key='categories', value=categories)
    kwargs['ti'].xcom_push(key='sellers', value=sellers)
    kwargs['ti'].xcom_push(key='products', value=products)
    

def extract_from_db(engine):
    try:
        categories = pd.read_sql('SELECT * FROM category', engine)
        sellers = pd.read_sql('SELECT * FROM seller', engine)
        products = pd.read_sql('SELECT * FROM product', engine)
        return categories, sellers, products
    except Exception as e:
        print(f'Error in extracting data from MySQL db: {str(e)}')
        raise


def extract_from_csv(file_path):
    try:
        orders = pd.read_csv(file_path)
        return orders
    except Exception as e:
        print(f'Error in extracting data from CSV file: {str(e)}')
        raise
