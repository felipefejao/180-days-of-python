import day1.Customer

customer = day1.Customer.Customer()

customer.create_customer("John Doe", "john.doe@example.com", 6000.0)
customer.create_customer("John Doe2", "john.doe@example.com", 2000.0)
customer.create_customer("John Doe3", "john.doe@example.com", 12000.0)

print("Final report:", customer.final_report())