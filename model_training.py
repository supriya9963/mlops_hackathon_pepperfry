import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import joblib

# Load and Prepare Data
df = pd.read_csv('pepperfry_sofas_enhanced.csv')
features = ['brand_popularity_score', 'discount_percent', 'rating', 'associated_brands_count']
X = df[features]
y = df['discounted_price_inr']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save split data for GitHub visibility
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)

# Train Model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
model.fit(X_train, y_train)

# Save Model Artifacts
joblib.dump(model, 'model.pkl')
print("Model training complete. model.pkl saved.")