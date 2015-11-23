import sys
import uuid
from datetime import datetime
from datetime import timedelta
from pyspark import SparkContext, SparkConf

def _get_task_partitions(start, end=None):
    format_str = "%Y-%m-%d/%H"
    start_time = datetime.strptime(start, format_str) 
    if (end == None):
        end_time = datetime.utcnow()
    else:
        end_time = datetime.strptime(end, format_str)

    partitions = []
    cur_time = start_time
    while cur_time <= end_time:
        cur_str = cur_time.strftime(format_str)
        partitions.append(cur_str)
        cur_time = cur_time + timedelta(hours=1)

    return partitions


def pre_process_logs(trader="btcc", start="2015-11-17/07", end=None):
    task_partitions = _get_task_partitions(start, end)
    print(task_partitions)

    conf = SparkConf()
    conf.setAppName("pre-process")
    sc = SparkContext(conf = conf)

    if (trader == "btcc"):
        url_template = "wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/{0}/*"
    else:
        url_template = "wasb://btcc@guohaodata.blob.core.windows.net/huobi-btccny-price/{0}/*"

    union_src = sc.textFile(url_template.format(task_partitions[0]))
    for i in range(1, len(task_partitions)):
        cur_src = sc.textFile(url_template.format(task_partitions[i]))
        union_src = union_src.union(cur_src)
    #src = sc.textFile("wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2*/*/*")

    items = union_src.map(lambda x: x.split("\t")).map(lambda x: (long(x[0]), (long(x[0]), float(x[3]), float(x[4]), float(x[5]))))

    filtered_items = items.filter(lambda x: x[0] >= 1447745420).reduceByKey(lambda x, y : x)

    sorted_items = items.repartition(1).sortByKey().zipWithIndex().map(lambda x: "\t".join((str(x[1]), str(x[0][1][0]), str(x[0][1][1]), str(x[0][1][2]), str(x[0][1][3]))))

    path = "wasb://btcc@guohaodata.blob.core.windows.net/cooked/" + str(uuid.uuid4())
    print("results will be saved under {0}".format(path))
    sorted_items.saveAsTextFile(path)
    return path

if (__name__ == "__main__"):
    start = None
    end = None

    arg_len = len(sys.argv)
    if (arg_len < 3 or arg_len > 4):
        print("Usage: pre-process.py btcc|huobi start [end]")
        sys.exit(0)

    trader = sys.argv[1]
    start = sys.argv[2]
    if (arg_len == 4):
        end = sys.argv[3]

    pre_process_logs(trader, start, end)