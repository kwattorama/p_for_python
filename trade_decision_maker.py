# this script will use manual inputs from user according to choosen
# stock chart to trade and then suggest if its profitable to trade or not
# mainly depending on chart trend, candle pattern, volume, rsi and 
# risk-reward ratio
# ======================================================================

# TODO(kwattorama)
# - add RSI, FIBO, support and resistane input
# - calculate reward, risk and RR ratio
# -use dict for the whole details



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
    "RSI": ["Overbrought", "Oversold", "Average"],
    "chart_pattern": ["Double Top", "Head & Shoulders", "Inverted H & S",
                      "Cup & Handle", "Double bottom", "No comfirm pattern"],
    "breakdown": ["Triangle breakdown", "Rectangular breakdown",
                  "Flag breakdown", "Trendline breakdown"],
    "divergence": ["Bullish div (price higher high & indicatior lower high)",
                   "Bearish div (price lower high & indicator higher low)"]
}

script_name = input("Enter the stcok name: ")
print("\n")
for tf_idx, time_frames in enumerate(indicators["time_frames"], start=1):
  print(f"{tf_idx}. {time_frames}")

your_tf = int(input("Choose your time frame>>> "))
print("\n")
# ltp = last traded price
ltp = int(input("Enter the close of the last candle>>> "))
print("\n")

for ema_idx, ema in enumerate(indicators["ema"], start=1):
  print(f"{ema_idx}. {ema}")

ema = input("Choose the ema crossing type if any>>> ")
print("\n")

for volume_idx, volume in enumerate(indicators["volume"], start=1):
  print(f"{volume_idx}. {volume}")

volume = input("Volume is... >>>")
print("\n")

for chart_idx, chart_pattern in enumerate(indicators["candle_pattern"].values(), start=1):
  print(f"Group-{chart_idx}.{chart_pattern}\n")
 
candle_pattern = input(
    f"\nIn \"{script_name}\" chart is there any candlestick pattern from the any one of the above group?>>> ")
    print("\n")

for trend_idx, trend in enumerate(indicators["trend"], start=1):
  print(f"Group-{trend_idx}.{trend}\n")

your_tf_trend = input(f"Which trend is in your time frame[1/2/3]>>> ")
guide_tf_trend = input("Which trend is in guide time frame[1/2/3]>>> ")
lower_tf_trend = input("Which trend is in lower time frame[1/2/3]>>> ")
print("\n")
