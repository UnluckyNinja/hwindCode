import uuid
from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setAppName("test")
sc = SparkContext(conf = conf)

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
                cur_stock = cur_money / float(results[i][3])
                cur_money = 0.0
                need_buy = False
                operation = "BUY"
            else:
                pass
        else:
            if (cur_dif > high_bar or cur_dif < ratio * low_bar):
                cur_money = cur_stock * float(results[i][2])
                cur_stock = 0.0
                need_buy = True
                operation = "SELL"
            else:
                pass
        cur_value = cur_money + cur_stock * float(results[i][2])
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

def _getRunResultsScore(run_result):
    index = len(run_result) - 1
    evaluated_value = float(run_result[index][10])
    operation_cnt = 0
    for i in range(0, len(run_result)):
        if (run_result[i][11] != "NA"):
            operation_cnt = operation_cnt + 1
    return (evaluated_value, operation_cnt)

def evaluateParam(param, items):
    low = param[0]
    high = param[1]
    ratio = param[2]

    price = []
    for i in range(0, len(items)):
        price.append(float(items[i][4]))

    results = []
    macd = getMACD(price)
    for i in range(0, len(items)):
        item = items[i]
        m = macd[i]
        t = (str(item[0]), str(item[1]), str(item[2]), str(item[3]), str(item[4]), str(m[1]), str(m[2]), str(m[3]), str(m[4]), str(m[5]))
        results.append(t)

    index = len(results) - 1
    run_result = testRun(results, low, high, ratio)
    score = _getRunResultsScore(run_result)

    evaluated_value = score[0]
    operation_cnt = score[1]
    return (evaluated_value, (param[0], param[1], param[2], evaluated_value, operation_cnt))

def getArray(start, end, step):
    ret = []
    for i in range(0, int((end-start)/step)):
        ret.append(start + i * step)
    return ret

low = getArray(-10.0, 0, 0.5)
high = getArray(0.1, 10.0, 0.5)
ratio = getArray(1.0, 20.0, 1.0)

tasks = []
for i in range(0, len(low)):
    for j in range(0, len(high)):
        for k in range(0, len(ratio)):
            t = (low[i], high[j], ratio[k])
            tasks.append(t)

src = sc.textFile("wasb://btcc@guohaodata.blob.core.windows.net/cooked/*")
items = src.map(lambda x: x.split("\t")).collect()

print(len(tasks))

params = sc.parallelize(tasks)

results = params.map(lambda x: evaluateParam(x, items)).repartition(1).sortByKey()

path = "wasb://btcc@guohaodata.blob.core.windows.net/evaluateresults/" + str(uuid.uuid4())
print("results will be saved under {0}".format(path))
results.saveAsTextFile(path)