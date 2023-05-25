import pandas as pd

# Brodcasting -------------------------------------

# s = pd.Series([100, 200, 300])
# print(s + 10)
# print(s * 10)


# Four_Calculate_#1 -------------------------------

# high = pd.Series([51500, 51200, 52500, 51500, 51500])
# low = pd.Series([50700, 50500, 50500, 50800, 50700])
# diff = high - low
# print(diff)


# Four_Calculate_#2 -------------------------------

# high = pd.Series(data = [51500, 51200, 52500], index = ['05/01', '05/02', '05/03'])
# low = pd.Series(data = [50700, 50500, 50500], index = ['05/01', '05/02', '05/04'])
# diff = high - low
# print(diff)


# Boolean -----------------------------------------

# s = pd.Series(data = [100, 200, 300, 400, 500])
# cond = s > 300
# print(cond)


# Filtering ---------------------------------------

s = pd.Series(data = [100, 200, 300, 400, 500])
cond_a = [False, False, False, True, True]
print(s[cond_a])
cond_b = s > 300
print(s[cond_b])

start_price = pd.Series([100, 200, 300, 400, 500])
end_price = pd.Series([100, 300, 400, 500, 600])
gap = start_price >= 300
print(end_price[gap])


# -------------------------------------------------

# low_price = pd.Series([10, 200, 200, 400, 600])
# high_price = pd.Series([100, 300, 400, 500, 600])

# gap = high_price - low_price >= 100
# print(high_price[gap])


# -------------------------------------------------

# end_price = pd.Series(data = [93000, 82400, 99100, 81000, 72300], 
#                       index = ['05/14', '05/15', '05/16', '05/17', '05/18'])

# price_range = (end_price >= 80000) & (end_price < 90000)
# print(end_price[price_range])
# print(end_price[price_range])