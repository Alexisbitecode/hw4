import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Add this import statement

# Load the data from a CSV file
df = pd.read_csv("StudentsPerformance.csv")
df1 = df.groupby("parental level of education")[["math score", "reading score"]].mean()


fig = plt.figure(figsize=(10, 6))
sns.scatterplot(x="math score", y="reading score", hue="parental level of education", data=df1)
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.title("Scatter Plot of Math Score vs. Reading Score (Colored by Parental Education)")
# Display the plot in Streamlit
st.pyplot(fig)
