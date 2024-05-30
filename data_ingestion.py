import duckdb 

conn = duckdb.connect("pizza.duckdb")

conn.execute("""CREATE table pizza_orders as select * from read_csv('data/orders.csv')""")

conn.execute("""CREATE table pizza_order_details as select * from read_csv('data/order_details.csv')""")

# conn.execute("""
# CREATE TABLE types_pizza (
#     pizza_type_id VARCHAR,
#     name VARCHAR,
#     category VARCHAR,
#     ingredients VARCHAR
# )
# COPY types_pizza FROM 'data/pizza_types.csv', options => '{encoding: "utf-8"}'
# """)


conn.execute("""CREATE table pizza as select * from read_csv('data/pizzas.csv')""")

result = conn.execute("SELECT * FROM pizza")
print(result)

# Close the connection
conn.close()






