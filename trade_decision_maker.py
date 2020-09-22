# this script will use manual inputs from user according to choosen
# stock to trade and then suggest if its profitable to trade or not in selected time frame
# mainly depending on chart trend, candle pattern, volume, rsi and risk-reward ratio
# To Do
# - add RSI, Fibonacci, support and resistane input
# - calculate reward, risk and RR ration


script_name = input("Enter the stcok name: ")
time_frames = ["Hourly", "Daily", "Weekly", "Monthly"]

for tf_idx, time_frames in enumerate(time_frames, start=1):
    print(f"{tf_idx}. {time_frames}")

your_tf = int(input("Choose your time frame>>> "))
# ltp = last traded price
ltp = int(input("Enter the close of the last candle>>> "))
ema = input("\nIs price above 50 ema?\n1. Yes\n2. No\nEnter[1/2]>>> ")
volume = input("\nVolume is..\n1. Good/Huge\n2. Average\n3. below Average\nEnter[1/2]>>> ")
print("Group-1: Plain green, Bullish Piercing, Bullish Engulf, Morning star, Inverted hammer\n\nGroup-2: Plain red, Bearish Piercing, Bearish Engulf, Evening star, Hammer\n\nGroup-3: Bullish Harami, Bearish Harami, Hanging man, Spinning top, Doji")
candle_pattern = input("\nIs there any candlestick patter from above group?\n1. Yes\n2. No\nEnter[1/2]>>> ")

if candle_pattern == "1":
    candle_group = input("Enter the candle group[1/2/3]>>>")

trend = ["Uptrend", "Downtrend", "Sideway"]

for trend_idx, trend in enumerate(trend, start=1):
    print(f"{trend_idx}. {trend}")

your_tf_trend = input(f"Which trend is in your time frame[1/2/3]>>> ")
guide_tf_trend = input("Which trend is in senior time frame[1/2/3]>>> ")
lower_tf_trend = input("Which trend is in junior time frame[1/2/3]>>> ")
