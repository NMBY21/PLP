import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 CORD-19 Research Explorer")
st.write("Interactive exploration of COVID-19 research metadata")

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    return df

df = load_data()

# Sidebar filters
year_range = st.slider("Select year range", 2010, 2025, (2019, 2021))
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

st.subheader("Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, palette="viridis")
st.pyplot(fig)

st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="magma")
st.pyplot(fig)

st.subheader("Sample Data")
st.dataframe(filtered[["title", "authors", "year", "journal"]].head(20))
