from utils.withSQL import withSQL

@withSQL("""
    SELECT ShipCountry, COUNT(*) as OrderCount 
    FROM orders 
    GROUP BY ShipCountry 
    ORDER BY OrderCount DESC;
""")
def orders_per_country(result):
    result.columns = ['Country', 'OrderCount']
    return result

@withSQL("""
    SELECT products.ProductID, products.ProductName, SUM(orderdetails.Quantity) AS TotalQuantitySold 
    FROM products 
    JOIN orderdetails ON products.ProductID = orderdetails.ProductID 
    GROUP BY products.ProductID, products.ProductName 
    ORDER BY TotalQuantitySold DESC 
    LIMIT 10;
""")
def top_selling_products(result):
    return result

@withSQL("""
    SELECT customers.CustomerID, customers.CompanyName, SUM(orderdetails.UnitPrice * orderdetails.Quantity * (1 - orderdetails.Discount)) AS TotalRevenue 
    FROM customers 
    JOIN orders ON customers.CustomerID = orders.CustomerID 
    JOIN orderdetails ON orders.OrderID = orderdetails.OrderID 
    GROUP BY customers.CustomerID, customers.CompanyName 
    ORDER BY TotalRevenue DESC 
    LIMIT 10;
""")
def top_customers_by_revenue(result):
    return result

@withSQL("""
    SELECT products.ProductID, products.ProductName, SUM(orderdetails.UnitPrice * orderdetails.Quantity * (1 - orderdetails.Discount)) AS TotalProfit 
    FROM products 
    JOIN orderdetails ON products.ProductID = orderdetails.ProductID 
    GROUP BY products.ProductID, products.ProductName 
    ORDER BY TotalProfit DESC 
    LIMIT 10;
""")
def most_profitable_product(result):
    return result

@withSQL("""
    SELECT ShipCountry, AVG(DATEDIFF(ShippedDate, OrderDate)) AS AvgProcessTime 
    FROM orders 
    GROUP BY ShipCountry 
    ORDER BY AvgProcessTime ASC;
""")
def order_processing_time_by_country(result):
    return result

@withSQL("""
    SELECT employees.Region, YEAR(orders.OrderDate) AS OrderYear, COUNT(orders.OrderID) AS TotalOrders
    FROM orders
    JOIN employees ON orders.EmployeeID = employees.EmployeeID
    GROUP BY employees.Region, OrderYear
    ORDER BY OrderYear;
""")
def employee_performance_by_region_year(result):
    return result