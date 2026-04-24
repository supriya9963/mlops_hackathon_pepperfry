import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('pepperfry_sofas_enhanced.csv')

def perform_eda(df):
    print("--- Data Summary ---")
    print(df.describe())
    
    # 1. Price Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['discounted_price_inr'], kde=True, color='blue')
    plt.title('Sofa Price Distribution')
    plt.savefig('plot_01_price_distribution.png')
    
    # 2. Brand Popularity vs Price
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='brand_popularity_score', y='discounted_price_inr', hue='brand_tier')
    plt.title('Brand Popularity vs Price')
    plt.savefig('plot_02_popularity_vs_price.png')
    
    print("EDA Visuals saved as .png files.")

if __name__ == "__main__":
    perform_eda(df)