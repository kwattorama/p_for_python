# this script will use manual inputs from user according to choosen
# stock chart to trade and then suggest if its profitable to trade or not
# mainly depending on chart trend, candle pattern, volume, rsi and 
# risk-reward ratio
# ======================================================================

# TODO(kwattorama)
# - add RSI, FIBO, support and resistane input
# - calculate reward, risk and RR ratio
# -use dict for the whole details
# indicators = {"time_frames": ["Hourly", "Daily", "Weekly", "Monthly"], "candle_pattern": [{"Bullish_candle": ["Plain green", "Bullish Piercing", "Bullish Engulf", "Morning star", "Inverted hammer"]}, {"Bearish_candle": ["Plain red", "Bearish Piercing", "Bearish Engulf", "Evening star", "Hammer"]}, {"Neutral_candle": ["Bullish Harami", "Bearish Harami", "Hanging man", "Spinning top", "Doji"]}]}, {"trend": ["Uptrend", "Downtrend", "Sideway"]}, {"RSI": ["Overbrought", "Oversold", "Average"]}, {"chart_pattern": ["Double Top", "Head & Shoulders", "Inverted H & S", "Cup & Handle", "Double bottom", "No comfirm pattern"]}, {"breakdown": ["Triangle breakdown", "Rectangular breakdown", "Flag breakdown", "Trendline `breakdown"]},{"divergence":["Bullish div (price higher high & indicatior lower high)", "Bearish div (price lower high & indicator higher low)"]}


script_name = input("Enter the stcok name: ")
time_frames = ["Hourly", "Daily", "Weekly", "Monthly"]

for tf_idx, time_frames in enumerate(time_frames, start=1):
    print(f"{tf_idx}. {time_frames}")

your_tf = int(input("Choose your time frame>>> "))
# ltp = last traded price
ltp = int(input("Enter the close of the last candle>>> "))
ema = input("\nIs there moving avarage cross over ?\n1. Yes\n2. No\nEnter[1/2]>>> ")

if ema == "1":
    ema_type = input("\n1. 5ema > 13ema > 26ema\n2. 5ema < 13ema < 26ema\nChoose the ema cross over type>>> ")

volume = input("\nVolume is..\n1. Good/Huge\n2. Average\n3. below Average\nEnter[1/2/3]>>> ")
print("Group-1: Plain green, Bullish Piercing, Bullish Engulf, Morning star,Inverted hammer\n\nGroup-2: Plain red, Bearish Piercing, Bearish Engulf, Evening star, Hammer\n\nGroup-3: Bullish Harami, Bearish Harami, Hanging man, Spinning top, Doji")
candle_pattern = input("\nIs there any candlestick patter from above group?\n1. Yes\n2. No\nEnter[1/2]>>> ")

if candle_pattern == "1":
    candle_group = input("\nEnter the candle group[1/2/3]>>>")
print("\n")
trend = ["Uptrend", "Downtrend", "Sideway"]

for trend_idx, trend in enumerate(trend, start=1):
    print(f"{trend_idx}. {trend}")

your_tf_trend = input(f"Which trend is in your time frame[1/2/3]>>> ")
guide_tf_trend = input("Which trend is in guide time frame[1/2/3]>>> ")
lower_tf_trend = input("Which trend is in lower time frame[1/2/3]>>> ")
rsi = input("\nRSI is...\n 1. Overbrought\n 2. Oversold\n3. Average\nEnter[1/2/3]>>> ")

chart_pattern = ["Double Top", "Head & Shoulders", "Inverted H & S",
                 "Cup & Handle", "Double bottom", "No comfirm pattern"]

for chart_idx, chart_pattern in enumerate(chart_pattern, start=1):
    print(f"{chart_idx}.{chart_pattern}")

chart_pattern_in = input("type of pattern availabe in chart from above list>>> ")
