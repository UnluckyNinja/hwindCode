import pdb

def getEMA(items, n):
    EMA = items[0]
    C_EMA = 2.0 / float(1 + n)

    result = []
    for i in range(0, len(items)):
        EMA = C_EMA * items[i] + (1.0 - C_EMA) * EMA
        result.append(EMA)
    return result

def getMACD(items, fast=12, slow=26, n=9):
    EMA_fast = getEMA(items, fast)
    EMA_slow = getEMA(items, slow)
    delta = []
    for i in range(0, len(items)):
        delta.append(EMA_fast[i] - EMA_slow[i])
    EMA_n = getEMA(delta, n)

    result = []
    for i in range(0, len(items)):
        t = (items[i], EMA_fast[i], EMA_slow[i], delta[i], EMA_n[i], (delta[i] - EMA_n[i])*2)
        result.append(t)
    return result


def testRun(results, low_bar, high_bar, ratio, save_to_file=False):
    need_buy = True
    cur_money = 10000.0
    cur_stock = 0.0
    changes = []
    changes.append(cur_money)

    final = []
    t = (results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5], results[0][6], results[0][7], results[0][8], results[0][9], str(cur_money), "NA")
    final.append(t)

    for i in range(1, len(results)):
        pre_dif = float(results[i-1][9])
        cur_dif = float(results[i][9])
        is_up = True
        operation = "NA"
        if (pre_dif > cur_dif):
            is_up = False

        if (need_buy == True):
            if ((is_up == True) and (pre_dif < low_bar and cur_dif > low_bar)):
                cur_stock = cur_money / float(results[i][4])
                cur_money = 0.0
                need_buy = False
                operation = "BUY"
            else:
                pass
        else:
            if (cur_dif > high_bar or cur_dif < ratio * low_bar):
                cur_money = cur_stock * float(results[i][4])
                cur_stock = 0.0
                need_buy = True
                operation = "SELL"
            else:
                pass
        cur_value = cur_money + cur_stock * float(results[i][4])
        changes.append(cur_value)
        t = (results[i][0], results[i][1], results[i][2], results[i][3], results[i][4], results[i][5], results[i][6], results[i][7], results[i][8], results[i][9], str(cur_value), operation)
        final.append(t)

    if (save_to_file == True):
        filename = "test_macd_{0}_{1}_{2}.txt".format(low_bar, high_bar, ratio)
        with open(filename, "w+") as f:
            for i in range(0, len(final)):
                t = final[i]
                ret = "\t".join(t)
                f.write(ret)
                f.write("\n")
    return final


items = []
price = []
with open("000000_0") as f:
    for line in f:
        line = line.strip()
        cols = line.split('\t')
        items.append((cols[0], cols[1], cols[2], cols[3], cols[4]))
        price.append(float(cols[4]))

results = []
with open("macd.txt", "w+") as f:
    macd = getMACD(price)
    for i in range(0, len(items)):
        item = items[i]
        m = macd[i]
        if (float(item[4]) != m[0]):
            pdb.set_trace()
        t = (str(item[0]), str(item[1]), str(item[2]), str(item[3]), str(item[4]), str(m[1]), str(m[2]), str(m[3]), str(m[4]), str(m[5]))
        results.append(t)
        ret = "\t".join(t)
        f.write(ret)
        f.write("\n")

index = len(results) -1
multi_mode = False
if (multi_mode == True):
    low_bar_start = -0.2
    high_bar_start = 0.2
    ratio_start = 1.1
    max_value = 0
    max_combine = "nothing"


    for i in range(0, 40):
        low_bar = low_bar_start + 0.005*i
        for j in range(0, 40):
            high_bar = high_bar_start + 0.005*j
            for k in range(0, 10):
                ratio = ratio_start + 0.1*k
                run_result = testRun(results, low_bar, high_bar, 1.2)
                if (max_value < float(run_result[index][10])):
                    max_value = float(run_result[index][10])
                    max_combine = "{0}_{1}_{2}".format(low_bar, high_bar, ratio)

    print(max_value)
    print(max_combine)
else:
    run_result = testRun(results, -0.18, 0.19, 19.6, True)
    print(run_result[index][10])