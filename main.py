import pandas as pd
import matplotlib.pyplot as plt


la_crime_data = pd.read_csv("LA-CRIME-DATA.csv")

# 10 most common crimes
top_10_crimes = la_crime_data["crime_description"].value_counts().head(10)
plt.bar(top_10_crimes.index, top_10_crimes.values)
plt.title("Top 10 Most Common Crimes")
plt.xlabel("Crime")
plt.xticks(rotation=90)
plt.ylabel("Number of Crimes")
plt.show()

# 5 most common areas for crime
top_10_areas = la_crime_data["area_name"].value_counts().head(5)
plt.bar(top_10_areas.index, top_10_areas.values)
plt.title("Top 10 Areas for Crime")
plt.xlabel("Area")
plt.xticks(rotation=90)
plt.ylabel("Number of Crimes")
plt.show()
