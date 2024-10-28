
from utils.plots import bar_chart, boxplot, histogram, heatmap, wordcloud
from assignment_5.sql_queries import *

def main():
    df_orders_per_country = orders_per_country()
    bar_chart(
        x_data=df_orders_per_country['Country'], 
        y_data=df_orders_per_country['OrderCount'], 
        x_label="Country", 
        y_label="Number of Orders", 
        title="Orders per Country",
        rotate_labels=True
    )

    df_top_selling_products = top_selling_products()
    bar_chart(
        x_data=df_top_selling_products['ProductName'], 
        y_data=df_top_selling_products['TotalQuantitySold'], 
        x_label="Product", 
        y_label="Total Quantity Sold", 
        title="Most Selling Product",
        rotate_labels=True
    )

    
    df_top_customer_by_revenue = top_customers_by_revenue()
    bar_chart(
        x_data=df_top_customer_by_revenue['CompanyName'],
        y_data=df_top_customer_by_revenue['TotalRevenue'], 
        x_label="Customer", 
        y_label="Total Revenue", 
        title="Top customers by revenue",
        rotate_labels=True
    )

    df_most_profitable_product = most_profitable_product()
    bar_chart(
        x_data=df_most_profitable_product['ProductName'], 
        y_data=df_most_profitable_product['TotalProfit'], 
        x_label="Product", 
        y_label="Total Profit", 
        title="Most Profitable Products",
        rotate_labels=True
    )

    df_order_processing_time = order_processing_time_by_country()
    bar_chart(
        x_data=df_order_processing_time['ShipCountry'],
        y_data=df_order_processing_time['AvgProcessTime'],
        x_label="Country",
        y_label="Time from Order to Shipment (Days)",
        title="Order Processing Time by Country",
        rotate_labels=True
    )

    df_employee_performance = employee_performance_by_region_year()
    heatmap(
        data=df_employee_performance,
        x_column='OrderYear',
        y_column='Region',
        value_column='TotalOrders',
        x_label='Year',
        y_label='Employee Region',
        title='Employee Performance by Region and Year'
    )