import numpy as np

sales = np.array([
    [1200, 1500, 1800, 1600, 2000],
    [900, 1100, 1000, 1200, 1300],
    [2500, 2700, 2600, 3000, 3200],
    [700, 800, 750, 900, 950]
])

categories = ["Grocery", "Clothing", "Electronics", "Stationery"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

print("1. Complete sales array:")
print(sales)
print()

print("2. Number of rows and columns:", sales.shape)
print()

print("3. Dimension of sales array:", sales.ndim)
print()

print("4. Sales of Electronics:")
print(sales[2])
print()

print("5. Sales made on Monday:")
print(sales[:, 0])
print()

print("6. Sales of Grocery from Monday to Wednesday:")
print(sales[0, 0:3])
print()

print("7. Sales of Clothing and Electronics:")
print(sales[1:3])
print()

category_total = np.sum(sales, axis=1)
print("8. Total sales of each product category:")
for i in range(4):
    print(categories[i], ":", category_total[i])
print()

day_total = np.sum(sales, axis=0)
print("9. Total sales for each day:")
for i in range(5):
    print(days[i], ":", day_total[i])
print()

category_average = np.mean(sales, axis=1)
print("10. Average daily sales of each product category:")
for i in range(4):
    print(categories[i], ":", category_average[i])
print()

category_max = np.max(sales, axis=1)
print("11. Maximum sales for each product category:")
for i in range(4):
    print(categories[i], ":", category_max[i])
print()

category_min = np.min(sales, axis=1)
print("12. Minimum sales for each product category:")
for i in range(4):
    print(categories[i], ":", category_min[i])
print()

overall_total = np.sum(sales)
print("13. Overall total sales:", overall_total)
print()

overall_average = np.mean(sales)
print("14. Overall average sales:", overall_average)
print()

print("15. Total sales category-wise using axis=1:")
print(np.sum(sales, axis=1))
print()

print("16. Total sales day-wise using axis=0:")
print(np.sum(sales, axis=0))
print()

highest_category = np.argmax(category_total)
print("17. Category having the highest total sales:", categories[highest_category])
print()

lowest_category = np.argmin(category_total)
print("18. Category having the lowest total sales:", categories[lowest_category])
print()

highest_day = np.argmax(day_total)
print("19. Day having the highest total sales:", days[highest_day])
print()

lowest_day = np.argmin(day_total)
print("20. Day having the lowest total sales:", days[lowest_day])
print()

print("21. Highest individual sales value:", np.max(sales))
print()

print("22. Lowest individual sales value:", np.min(sales))
print("Category corresponding to the highest total sales:", categories[highest_category])
print()

print("23. Sales values greater than ₹2,000:")
print(sales[sales > 2000])
print()

print("24. Sales values less than ₹1,000:")
print(sales[sales < 1000])
print()

print("25. Number of sales transactions greater than ₹2,000:")
print(np.sum(sales > 2000))
print()

print("26. Number of sales values less than ₹1,000:")
print(np.sum(sales < 1000))
print()

print("27. Sales values between ₹1,000 and ₹2,000:")
print(sales[(sales >= 1000) & (sales <= 2000)])
print()

classification = np.where(sales >= 2000, "High", "Normal")
print("28. Sales classification:")
print(classification)
print()

print("29. Sales values greater than ₹2,500:")
print(np.where(sales > 2500, sales, 0))
print()

sales_replaced = np.where(sales < 1000, 1000, sales)
print("30. Sales values below ₹1,000 replaced with ₹1,000:")
print(sales_replaced)
print()

print("31. All sales values in ascending order:")
print(np.sort(sales, axis=None))
print()

print("32. Electronics sales in ascending order:")
print(np.sort(sales[2]))
print()

unique_values = np.unique(sales)
print("33. Unique sales values:")
print(unique_values)
print()

unique_values, frequencies = np.unique(sales, return_counts=True)
print("34. Unique sales values and their frequencies:")
for value, frequency in zip(unique_values, frequencies):
    print(value, ":", frequency)
print()

most_frequent = unique_values[np.argmax(frequencies)]
print("35. Sales amount occurring most frequently:", most_frequent)
print()

new_sales = sales * 1.10
print("36. Sales increased by 10%:")
print(new_sales)
print()

print("37. New sales data:")
print(new_sales)
print()

new_total = np.sum(new_sales)
print("38. New total sales:", new_total)
print()

difference = new_total - overall_total
print("39. Difference between old total sales and new total sales:", difference)