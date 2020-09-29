# this script will use manual inputs from user according to choosen
# stock chart to trade and then suggest if its profitable to trade or not
# mainly depending on chart trend, candle pattern, volume, rsi and 
# risk-reward ratio
# ======================================================================

# TODO(kwattorama)
# - add FIBO, support and resistane input
# - make decision based on user input
# - calculate reward, risk and RR ratio
# - add more elif condition for average buy/sell



indicators = {
    "time_frames": ["Hourly", "Daily", "Weekly", "Monthly"],
    "ema": ["5ema > 13ema > 26ema", "5ema < 13ema < 26ema", "No ema crossing"],
    "volume": ["Good/Huge", "Average", "below Average"],
    "candle_pattern":
    {
        "Bullish_candle": ["Plain green", "Bullish Piercing",
                           "Bullish Engulf", "Morning star",
                           "Inverted hammer"],
        "Bearish_candle": ["Plain red", "Bearish Piercing",
                           "Bearish Engulf", "Evening star", "Hammer"],
        "Neutral_candle": ["Bullish Harami", "Bearish Harami",
                           "Hanging man", "Spinning top", "Doji"]
    },
    "trend": ["Uptrend", "Downtrend", "Sideway"],
    "rsi": ["Overbrought", "Oversold", "Average"],
    "chart_pattern": ["Double Top", "Head & Shoulders", "Inverted H & S",
                      "Cup & Handle", "Double bottom", "No comfirm pattern"],
    "breakdown": ["Triangle breakdown", "Rectangular breakdown",
                  "Flag breakdown", "Trendline breakdown"],
    "divergence": ["Bullish div (price higher high & indicatior lower high)",
                   "Bearish div (price lower high & indicator higher low)", "No divergence"]
}

script_name = input("Enter the stcok name: ")
print("\n")
for tf_idx, time_frames in enumerate(indicators["time_frames"], start=1):
  print(f"{tf_idx}. {time_frames}")

your_tf = int(input("Choose your time frame >>> "))
print("\n")
# ltp = last traded price
ltp = int(input("Enter the close of the last candle >>> "))
print(f"{'*' * 50}")

for ema_idx, ema in enumerate(indicators["ema"], start=1):
  print(f"{ema_idx}. {ema}")

ema = input("Choose the ema crossing type if any >>> ")
print(f"{'*' * 50}")

for volume_idx, volume in enumerate(indicators["volume"], start=1):
  print(f"{volume_idx}. {volume}")

volume = input("Volume is... >>> ")
print(f"{'*' * 50}")

for candle_idx, candle_pattern in enumerate(indicators["candle_pattern"].values(), start=1):
  print(f"{candle_idx}.{candle_pattern}\n")
 
candle_pattern = input(
    f"\nIn \"{script_name}\" chart is there any candlestick pattern from any one of the above group? >>> ")
print(f"{'*' * 50}")

for trend_idx, trend in enumerate(indicators["trend"], start=1):
  print(f"{trend_idx}.{trend}")

your_tf_trend = input(f"Which trend is in your time frame[1/2/3] >>> ")
guide_tf_trend = input("Which trend is in guide time frame[1/2/3] >>> ")
lower_tf_trend = input("Which trend is in lower time frame[1/2/3] >>> ")
print(f"{'*' * 50}")


for rsi_idx, rsi in enumerate(indicators["rsi"], start=1):
  print(f"{rsi_idx}.{rsi}")
  
trend = input(f"RSI is..? >>> ")

for chart_idx, chart_pattern in enumerate(indicators["chart_pattern"], start=1):
    print(f"{chart_idx}.{chart_pattern}")
  
rsi = input(f"RSI is..? >>> ")

for breakdown_idx, breakdown in enumerate(indicators["breakdown"], start=1):
  print(f"{breakdown_idx}.{breakdown}")
  
trend = input(f"Choose any breakdown occuring/may occur in guide time frame and your time frame >>> ")

for divergence_idx, divergence in enumerate(indicators["divergence"], start=1):
  print(f"{divergence_idx}.{divergence}")
  
divergence = input(f"Any divergence? >>> ")

if ema == "1" and volume == "1" and candle_pattern == "1" and trend == "1" and divergence == "1" and rsi == "2" or rsi == "3":
    print("Strong BUY")
elif (ema, volume, candle_pattern, trend, divergence == "2" or rsi == "1" or rsi == "3"):
    print("Strong SELL")
elif (ema, candle_pattern, divergence == 3 or volume, trend == 3):
    print("Wait..No clear signal to trade")
