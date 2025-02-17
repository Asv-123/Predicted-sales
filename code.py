import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



data = {
    'months' : [1,2,3,4,5,6],
    'sales' : [200, 250, 300, 400, 450, 500]
}

# negative index

df = pd.DataFrame(data)

df.to_csv('sales_data.csv',index = False)


df = pd.read_csv('sales_data.csv')
# print(df)

x = df['months']
y = df['sales']

val = np.polyfit(x,y,1)
slope = val[0]
intercept = val[1]
trend_line = np.polyval(val,x)

user_month = int(input('Enter the month: '))

predict = np.polyval(val,user_month)

print(f'Predicted sales for month {user_month} is {predict}')
plt.scatter(user_month, predict, color = 'green', marker = 'x',label = 'Predicted Sales')
plt.scatter(x,y, color ="blue", label ="Actual Sales")
plt.plot(x,trend_line, color ="red",label = "Trend line")
plt.axhline(y = 0, color ="black")
plt.axvline(x = 0, color ='black')
plt.title('Sale Data')
plt.grid()
plt.legend()
plt.show()
