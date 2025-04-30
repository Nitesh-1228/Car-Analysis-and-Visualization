import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'dataset.csv'
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

if 'df' in locals(): 
    print("Dimensions of the dataset:", df.shape)
    print("\nFirst few rows of the dataset:")
    print(df.head())
    print("\nData types of columns:")
    print(df.dtypes)
    print("\nBasic statistics of the dataset:")
    print(df.describe())
    df.drop_duplicates(subset=['Price_in_thousands'], keep='first', 
       inplace=True)
    df.drop(df[df['sales'] < 10].index, inplace=True)
    df.fillna(df.mean(), inplace=True)  
    price_mean = df['Price_in_thousands'].mean()
    print("\nMean for Price_in_thousands:", price_mean)
    engine_mode = df['Engine_size'].mode()[0]
    print("Mode for Engine_size:", engine_mode)
    sales_sum = df['sales'].sum()
    print("Sum for sales:", sales_sum)
    sales_min = df['sales'].min()
    print("Minimum for sales:", sales_min)
    sales_max = df['sales'].max()
    print("Maximum for sales:", sales_max)

    result = df.groupby('Engine_size')['Price_in_thousands'].mean()
    print("\nAverage Price_in_thousands for each Engine_size:")
    print(result)
    plt.figure(figsize=(5, 5))

    plt.subplot(3, 2, 1)
    plt.hist(df['Price_in_thousands'], bins=20, color='skyblue', 
    edgecolor='black')
    plt.title('Histogram of Price_in_thousands')
    plt.xlabel('Price_in_thousands')
    plt.ylabel('Frequency')
    plt.grid(True)

    plt.subplot(3, 3, 2)
    plt.scatter(df['Engine_size'], df['Price_in_thousands'], 
    color='orange', alpha=0.5)
    plt.title('Scatter plot of Price_in_thousands vs Engine_size')
    plt.xlabel('Engine_size')
    plt.ylabel('Price_in_thousands')
    plt.grid(True)

    price_ranges = [(10, 20), (20, 30), (30, 40)]
    price_counts = [((df['Price_in_thousands'] >= low) & 
    (df['Price_in_thousands'] < high)).sum() for low, 
    high in price_ranges]
    labels = [f'{low}-{high}' for low, high in price_ranges]
    plt.subplot(3, 3, 3)
    plt.pie(price_counts, labels=labels, 
    autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Price_in_thousands')
    plt.legend(labels, loc="upper right")
    plt.subplot(3, 3, 4)
    plt.plot(df['Horsepower'], color='green')
    plt.title('Line graph of Horsepower')
    plt.xlabel('Index')
    plt.ylabel('Horsepower')
    plt.grid(True)
    plt.subplot(3,3,5)
    fuel_efficiency_counts = df.groupby('Fuel_efficiency')['Engine_size'].mean()
    fuel_efficiency_counts.plot(kind='bar', color='orange')
    plt.title('Average Engine Size by Fuel Efficiency')
    plt.xlabel('Fuel Efficiency')
    plt.ylabel('Average Engine Size')
    plt.xticks(rotation=45)
    plt.grid(True)

    plt.show()
