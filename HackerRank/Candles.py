def birthdayCakeCandles(candles):
    tallest = max(candles)

    num = 0
    for i in candles:
        if(candles[i] == tallest):
            num = num + 1
        else:
            continue
    print(num)

def birthdayCakeCandles(candles):
   count = 0
   candle = max(candles)
   for i in range(len(candles)):
     if candles[i] == candle:
        count += 1
   return count 

candles = [3,2,1,3]
birthdayCakeCandles(candles)