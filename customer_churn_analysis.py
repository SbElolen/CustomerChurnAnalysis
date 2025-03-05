import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display some basic information
print("Dataset Shape:", df.shape)
print(df.info())
print(df.isnull().sum())  # Check for missing values

# Since there are no missing values here

# Display first few rows
print(df.head())

# Visualizing Churn Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x=df["Churn"], palette=["green", "red"])
plt.title("Churn Distribution", fontsize=14)
plt.xlabel("Churn", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

# Senior Citizen Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x=df["SeniorCitizen"], palette=["blue", "orange"])
plt.title("Senior Citizen Distribution", fontsize=14)
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

# Tenure vs Churn using a Histogram plot
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="tenure", hue="Churn", multiple="stack", bins=30, palette=["green", "red"])
plt.title("Tenure Distribution by Churn", fontsize=14)
plt.xlabel("Tenure (Months)", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

# Monthly Charges vs Churn using a box plot
plt.figure(figsize=(8, 5))
sns.boxplot(x="Churn", y="MonthlyCharges", data=df, palette=["green", "red"])
plt.title("Monthly Charges Distribution by Churn", fontsize=14)
plt.xlabel("Churn", fontsize=12)
plt.ylabel("Monthly Charges", fontsize=12)
plt.show()

# Saved the cleaned dataset for further analysis
df.to_csv("cleaned_customer_churn.csv", index=False)
