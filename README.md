# ⚡ Velocis

**Ultra-Low Latency Trading Simulator with AI-powered signals**  

Velocis is a real-time trading simulator that demonstrates how ultra-low latency strategies, LSTM-driven signals, and live visualization can be combined for quantitative finance experiments.

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/d7d54e25-7018-4f04-91c3-27b8741a371f" />

---

## 🚀 Features
- 📈 **Live Price Simulation** with configurable tick speed & starting price  
- 🤖 **LSTM-powered Trading Signals** trained on generated price series  
- ⚡ **Ultra-Low Latency Trade Execution** tracking nanosecond-level latencies  
- 💰 **Real-time PnL & Sharpe Ratio** calculation  
- 📊 **Dynamic Visualizations** with Streamlit and Matplotlib  

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) for live interactive dashboard  
- [TensorFlow / Keras](https://www.tensorflow.org/) for LSTM signal model  
- [Matplotlib](https://matplotlib.org/) for chart visualization  
- [NumPy & Pandas](https://pandas.pydata.org/) for data handling  

---

## ⚡ Installation

```bash
# Clone the repository
git clone https://github.com/aniketmore-pixel/velocis.git
cd velocis

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

- Adjust parameters (tick count, speed, start price) from the sidebar.  
- Watch the live chart update with **BUY/SELL signals**.  
- Monitor **PnL, Sharpe ratio, and trade latency** in real-time.  

---

## 📈 Future Improvements
- Add support for multiple strategies (Momentum, Mean Reversion, etc.)  
- Integrate real-world market data APIs (e.g., Alpaca, Polygon.io)  
- Extend LSTM model with attention mechanism  
- Optimize further for GPU-based ultra-low latency  

