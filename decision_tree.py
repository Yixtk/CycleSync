import pandas as pd
import ast
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import subprocess
import os

# --- 1. Configuration and Data Loading ---
# NOTE: Ensure the file 'Health - Sheet1.csv' is in the same directory as this script.
file_path = '/Users/yixiangtiankai/Documents/DSP_2025Fall/Health  - Sheet1.csv'

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
    print("Please ensure the CSV file is in the same folder as this Python script.")
    exit()

# --- 2. Data Preprocessing: Feature Extraction ---
try:
    # Safely parse the 'Nutrition Label' column from string to dictionary
    nutrition_dicts = df['Nutrition Label'].apply(ast.literal_eval)

    # Convert the list of dictionaries into a DataFrame of features
    df_nutrition = pd.json_normalize(nutrition_dicts)

    # Concatenate the new nutrition columns and drop the original
    df = pd.concat([df.drop('Nutrition Label', axis=1), df_nutrition], axis=1)

except Exception as e:
    print(f"An error occurred during feature extraction: {e}")
    exit()


# --- 3. Define Features (X) and Target (y) ---
feature_cols = [
    'calories', 'protein', 'unsaturated fat', 'trans fat', 'saturated fat',
    'omega 3', 'fiber', 'vitamin C', 'iron', 'magnesium', 'iodine',
    'zinc', 'vitamin K', 'calcium'
]
X = df[feature_cols]
y = df['Menstrual Phase Tag']

# Encode the target variable (y) from text to numerical labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)
target_names = le.classes_ # ['Follicular', 'Luteal', 'Menstrual', 'Ovulation']

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# --- 4. Model Training and Evaluation ---
# Initialize and train the Decision Tree Classifier
dtc = DecisionTreeClassifier(max_depth=4, random_state=42)
dtc.fit(X_train, y_train)

# Calculate and print the model accuracy
y_pred = dtc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Decision Tree Classifier Accuracy on Test Set: {accuracy:.2f}\n")


# --- 5. Visualization and Automatic Opening ---
image_filename = 'decision_tree_visualization.png'

# Create and save the plot
plt.figure(figsize=(25, 10))
tree.plot_tree(
    dtc,
    feature_names=feature_cols,
    class_names=target_names,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Decision Tree for Menstrual Phase Classification (Max Depth 4)", fontsize=16)
plt.savefig(image_filename)
plt.close()

print(f"Decision Tree visualization successfully saved as '{image_filename}'.")

# Attempt to open the saved file automatically using the 'open' command (common on macOS)
try:
    print("Attempting to open the image file...")
    # 'check=True' will raise an error if the command fails
    subprocess.run(['open', image_filename], check=True)
except FileNotFoundError:
    # This usually means the 'open' command itself wasn't found (e.g., running on Windows without a proper shell setup)
    print("Could not find the 'open' command. Please open the PNG file manually.")
except Exception as e:
    # General error during the process
    print(f"Could not automatically open the file. Please open '{image_filename}' manually.")
