# cousera learning materail while the data analysis cousrse is in progress
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# --- PART 1: Data Manipulation (Pandas/NumPy) ---
print("Generating sample data...")
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [25, 40, 30, 55]
}
df = pd.DataFrame(data)
print(df)
print("-" * 30)

# --- PART 2: The F1 Score Math (NumPy) ---
def f1_score(precision, recall):
    # The formula for F1 Score
    score = 2 * precision * recall / (precision + recall)
    # np.nan_to_num handles division by zero at (0,0)
    score = np.nan_to_num(score)
    return score

# Create the coordinate grid for the 3D plot
x = np.linspace(0, 1, 101) # Precision axis
y = np.linspace(0, 1, 101) # Recall axis
X, Y = np.meshgrid(x, y)   # Create the 2D grid
Z = f1_score(X, Y)         # Calculate F1 for every point

# --- PART 3: Visualizing (Matplotlib/Seaborn) ---
# Set the style using Seaborn
sns.set_theme(style="whitegrid")

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=3, cmap='plasma', edgecolor='none')

# Add labels and title
ax.set_title('$F_{1}$ Score Surface (Precision vs Recall)', size=18)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.set_zlabel('F1 Score')

# Change the viewing angle
ax.view_init(35, -65)

# Add a color bar to show the scale
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

print("Displaying graph...")
plt.show()
##--- PART 1: String Object Practice ---
word = "Python is Fun"

print("--- String Methods ---")
print(f"Original: {word}")
print(f"Uppercase: {word.upper()}")         # Method: Makes everything CAPS
print(f"Lowercase: {word.lower()}")         # Method: Makes everything lowercase
print(f"Replaced:  {word.replace('Fun', 'Powerful')}") 
print(f"List version: {word.split()}")      # Turns string into a list of words
print("\n")

# --- PART 2: Pandas Object Practice ---
# Let's create a DataFrame of your favorite snacks or items
data = [
    ['Apple', 50, 'Fruit'],
    ['Chocolate', 200, 'Sweet'],
    ['Pizza', 800, 'Savory'],
    ['Carrot', 30, 'Vegetable']
]
columns = ['Item', 'Calories', 'Type']

# Construct the DataFrame object
snacks = pd.DataFrame(data, columns=columns)

print("--- DataFrame Attributes & Methods ---")
# 1. Attribute: Check dimensions
print(f"Shape of table: {snacks.shape}") 

# 2. Method: Show the top rows
print("\nTop 2 rows:")
print(snacks.head(2))

# 3. Method: Sort the data by Calories (High to Low)
print("\nSorted by Calories:")
print(snacks.sort_values(by='Calories', ascending=False))

# 4. Method: Statistical Summary
print("\nQuick Stats:")
print(snacks.describe())
class Spaceship:
   # Class attribute
   tractor_beam = 'off'

   # Instance attributes
   def __init__(self, name, kind):
       self.name = name
       self.kind = kind
       self.speed = None

  # Instance methods
   def warp(self, warp):
       self.speed = warp
       print(f'Warp {warp}, engage!')

   def tractor(self):
       if self.tractor_beam == 'off':
           self.tractor_beam = 'on'
           print('Tractor beam on.')
       else:
           self.tractor_beam = 'off'
           print('Tractor beam off')
# Create an instance of the Spaceship class (i.e. "instantiate")
ship = Spaceship('Mockingbird','rescue frigate')

# Check ship's name
print(ship.name)

# Check what kind of ship it is
print(ship.kind)

# Check tractor beam status
print(ship.tractor_beam)
# Set warp speed
ship.warp(7)

# Check speed
print(ship.speed)
# Toggle tractor beam
ship.tractor()

# Check tractor beam status
print(ship.tractor_beam)





num = 1000.987123
print(f'{num:.3e}')

decimal = 0.2497856
print(f'{decimal:.4%}')
separator_string = ' '
iterable_of_strings = ['Happy', 'birthday', 'to', 'you']

separator_string.join(iterable_of_strings)
print(separator_string.join(iterable_of_strings))

my_string = 'https://www.google.com/'

my_string.partition('.')
print(my_string.partition('.'))

# # The `in` keyword returns Boolean of whether substring is in string.
# 'banana' in fruit
# # Use iloc to access data using index numbers.
# # Select row 1, column 3.
# df.iloc[1][3]
# Use pd.DataFrame() function to create a dataframe from a dictionary.
# data = {'col1': [1, 2], 'col2': [3, 4]}
# df = pd.DataFrame(data=data)
# print(df)