import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the enhanced dataset from your Colab
df = pd.read_csv('pepperfry_sofas_enhanced.csv')

def generate_heatmap(df):
    # Select only numerical columns for correlation analysis
    numerical_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Calculate correlation matrix
    corr_matrix = numerical_df.corr()
    
    # Plotting
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Feature Correlation Heatmap: Furniture Pricing Factors')
    
    # Save the plot for GitHub
    plt.savefig('plot_12_correlation_heatmap.png')
    print("Heatmap saved as plot_12_correlation_heatmap.png")

if __name__ == "__main__":
    generate_heatmap(df)