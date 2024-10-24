import pandas as pd
import numpy as np

# Sample Data
data = {
    'Color': ['Red', 'Green', 'Blue', 'Green', 'Red', 'Blue'],
    'Size': ['S', 'M', 'L', 'S', 'L', 'M']
}

# Create DataFrame
df = pd.DataFrame(data)

# Ordinal Encoding Function
def ordinal_encode(column, categories):
    mapping = {category: idx for idx, category in enumerate(categories)}
    return column.map(mapping)

# One-Hot Encoding Function
def one_hot_encode(column):
    unique_values = column.unique()
    encoded_df = pd.DataFrame({f"{column.name}_{value}": (column == value).astype(int) for value in unique_values})
    return encoded_df

# Ordinal Encoding Example
# Define order for sizes
size_order = ['S', 'M', 'L']
df['Size_Ordinal'] = ordinal_encode(df['Size'], size_order)

# One-Hot Encoding Example
color_one_hot = one_hot_encode(df['Color'])
df = pd.concat([df, color_one_hot], axis=1)

# Display the results
print("Original Data:")
print(df)
