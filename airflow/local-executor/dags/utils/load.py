from sqlalchemy import create_engine


def load_data(dashboard_data, db_config):
    try:
        engine = create_engine(f'mysql+pymysql://{db_config['user']}:{db_config['password']}@'
                               f'{db_config['host']}/{db_config['database']}')
        with engine.begin() as connection:
            dashboard_data.to_sql(name='dashboard_data', con=connection, if_exists='replace')
    except Exception as e:
        print(f'Error in loading data: {str(e)}')
        raise
