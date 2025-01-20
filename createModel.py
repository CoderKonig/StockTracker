from fetchStockData import *
from dataClean import *
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Build the LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train, y_train, batch_size=32, epochs=50, validation_data=(X_test, y_test), verbose=1)

# Predictions
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

# Actual prices
y_test_scaled = scaler.inverse_transform(y_test.reshape(-1, 1))

# Plot results
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 5))
plt.plot(data.index[-len(y_test):], y_test_scaled, label='Actual Prices')
plt.plot(data.index[-len(predictions):], predictions, label='Predicted Prices')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.show()


model.save('lstm_stock_model.h5')
