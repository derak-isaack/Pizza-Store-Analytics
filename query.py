import duckdb 

con = duckdb.connect("pizaa.duckdb")

tables = con.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

# Print table names
for table in tables:
    print(table[0])

# Close connection
con.close()


