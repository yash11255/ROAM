import matplotlib.pyplot as plt

# Function to calculate the average of a list
def average(lst):
    total = sum(lst)
    avg = total / len(lst)
    return avg

# Function to perform linear regression and predict sales for given weeks
def predict_sale(x, y):
    # Calculate the average values for x and y
    x_bar = average(x)
    y_bar = average(y)

    # Calculate the necessary values for linear regression formula
    x_sq_bar = average([i**2 for i in x])
    xy_bar = average([x[i]*y[i] for i in range(len(x))])

    # Calculate the slope (al) and y-intercept (a0) for the linear regression line
    al = (xy_bar - (x_bar * y_bar)) / (x_sq_bar - (x_bar**2))
    a0 = y_bar - al * x_bar

    # Get user input for weeks to predict sales
    week_input = input("Enter the week(s) for which you want to predict the sales (separated by commas): ")
    weeks = [int(week) for week in week_input.split(',')]

    # Calculate predicted sales for the input weeks
    week_sales = [a0 + (al * week) for week in weeks]

    # Print the predicted sales for each input week
    for week, sales in zip(weeks, week_sales):
        print(f"Predicted sales for week {week}: {sales}")

    # Plotting the actual values, predicted values, and linear regression line
    plt.scatter(x, y, color='red', label='Actual Values')
    plt.scatter(weeks, week_sales, color='green', label='Predicted Values')
    plt.plot(x, [a0 + al * i for i in x], color='blue', label='Linear Regression')
    plt.plot([x[-1]] + weeks, [y[-1]] + week_sales, linestyle='dashed', color='blue', label='Extended Linear Regression')

    # Set plot settings
    plt.xticks(range(min(x), max(weeks) + 1))
    plt.xlabel('No. of Weeks')
    plt.ylabel('Sales (in thousands)')
    plt.legend()
    plt.show()

# Sample data
x = [1, 2, 3, 4, 5]  # Assuming weeks are represented as integers starting from 1
y = [1.2, 1.8, 2.6, 3.2, 3.8]

# Call the function to predict sales and plot the results
predict_sale(x, y)
