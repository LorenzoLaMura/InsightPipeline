import numpy as np


def transform_data(orders, categories, sellers, products):
    orders = fill_empty_cities(orders)
    merged_data = merge_data(orders, categories, sellers, products)
    fixed_merged_data = select_columns(merged_data)
    dashboard_data = rename_columns(fixed_merged_data)
    return dashboard_data


def fill_empty_cities(orders):
    try:
        # Replace 'Idk' with NaN in the city_name column of orders
        orders = orders.replace({'city_name': {'Idk': np.nan}})
        # Find rows with missing city_name
        missing_city_rows = orders['city_name'].isnull()

        # Iterate over each row with missing city_name
        for index, row in orders[missing_city_rows].iterrows():
            # Find rows with matching coordinates
            match = orders[(orders['city_x'] == row['city_x']) & 
                           (orders['city_y'] == row['city_y']) & (~orders['city_name'].isnull())]
            
            # If a match is found, replace missing city_name with matched city_name
            if not match.empty:
                orders.at[index, 'city_name'] = match.iloc[0]['city_name']
        return orders.dropna(subset=['city_name'])
    except Exception as e:
        print(f'Error in transforming data: {str(e)}')
        raise
    

def merge_data(orders, categories, sellers, products):
    try:
        merged_data = orders.merge(products, on='product_id', how='left') \
                        .merge(categories, on='category_id', how='left') \
                        .merge(sellers, on='seller_id', how='left')
        return merged_data
    except Exception as e:
        print(f'Error in transforming data: {str(e)}')
        raise


def select_columns(merged_data):
    try:
        fixed_merged_data = merged_data[[
            'order_id',
            'date',
            'product_id',
            'product_name',
            'category_id',
            'category_name',
            'seller_id',
            'seller_name',
            'city_name',
            'city_x',
            'city_y',
            'product_price'
        ]]
        return fixed_merged_data
    except Exception as e:
        print(f'Error in transforming data: {str(e)}')
        raise


def rename_columns(fixed_merged_data):
    try:
        dashboard_data = fixed_merged_data.rename(columns={
            'order_id': 'Order ID',
            'date': 'Order Date',
            'product_id': 'Product ID',
            'product_name': 'Product Name',
            'category_id': 'Category ID',
            'category_name': 'Category Name',
            'seller_id': 'Seller ID',
            'seller_name': 'Seller Name',
            'city_name': 'City',
            'city_x': 'Latitude',
            'city_y': 'Longitude',
            'product_price': 'Product Price'
        })
        return dashboard_data
    except Exception as e:
        print(f'Error in transforming data: {str(e)}')
        raise
