import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Ultra-Low Latency Trading Simulator", layout="wide")
st.title("⚡ Velocis")
st.write("Simulates trades, strategy, and PnL tracking in real-time, with ultra-low latency")

# ================================
# PARAMETERS
# ================================
NUM_TICKS = st.sidebar.slider("Number of ticks to simulate", 500, 5000, 1000)
SLEEP_TIME = st.sidebar.slider("Trade speed (seconds)", 0.01, 0.5, 0.05)
START_PRICE = st.sidebar.number_input("Starting Price", value=100.0)

# ================================
# SIMULATE TICK DATA
# ================================
np.random.seed(42)
prices = START_PRICE + np.cumsum(np.random.randn(NUM_TICKS) * 0.1)

# ================================
# LSTM MODEL FOR SIGNALS
# ================================
X, y = [], []
for i in range(20, len(prices)):
    X.append(prices[i-20:i])
    y.append(1 if prices[i] > prices[i-1] else 0)

X = np.array(X)
y = np.array(y)
X = X.reshape(X.shape[0], X.shape[1], 1)

model = Sequential([
    LSTM(32, input_shape=(20,1)),
    Dense(1, activation="sigmoid")
])
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, y, epochs=3, batch_size=32, verbose=0)

# ================================
# TRADING SIMULATION
# ================================
trades = []
cash, position = 0.0, 0
latencies = []

progress_bar = st.progress(0)
chart_placeholder = st.empty()
pnl_placeholder = st.empty()

for i in range(20, NUM_TICKS-1):
    # Prediction
    pred = model.predict(X[i-20].reshape(1, 20, 1), verbose=0)[0][0]
    price = prices[i]

    # Measure latency (simulated)
    start = time.time_ns()

    if pred > 0.6:
        # BUY
        position += 1
        cash -= price
        trades.append((price, "BUY"))
    elif pred < 0.4 and position > 0:
        # SELL
        position -= 1
        cash += price
        trades.append((price, "SELL"))

    latency = time.time_ns() - start
    latencies.append(latency)

    # Update PnL
    pnl = cash + position * price
    sharpe = np.mean(np.diff(prices[max(0, i-50):i])) / np.std(np.diff(prices[max(0, i-50):i]) + 1e-6)
    
    # Plot chart live
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(prices[:i], label="Price", color="blue")
    buys = [p for p, s in trades if s == "BUY"]
    sells = [p for p, s in trades if s == "SELL"]
    ax.scatter([x for x, s in enumerate(trades) if s[1]=="BUY"], buys, color="green", label="Buys", marker="^")
    ax.scatter([x for x, s in enumerate(trades) if s[1]=="SELL"], sells, color="red", label="Sells", marker="v")
    ax.set_title("Live Price & Trade Signals")
    ax.legend()
    chart_placeholder.pyplot(fig)

    pnl_placeholder.metric("Live PnL", f"${pnl:.2f}", delta=f"Sharpe: {sharpe:.2f}")
    progress_bar.progress(int((i / NUM_TICKS) * 100))
    time.sleep(SLEEP_TIME)

# Final Results
st.subheader("Final Metrics")
st.write(f"**Final PnL:** ${pnl:.2f}")
st.write(f"**Total Trades:** {len(trades)}")
st.write(f"**Mean Latency:** {np.mean(latencies)/1e6:.3f} ms")
st.write(f"**Sharpe Ratio:** {sharpe:.2f}")
