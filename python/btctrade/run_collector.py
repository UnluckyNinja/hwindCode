import json
import sys
from btcc_trade_collector import bttc_trade_collector
from btcc_client import Market

with open("./collector_config.json") as config_file:
    config = json.load(config_file)

if (len(sys.argv) != 2):
    print ("Usage: python run_collector.py [job name]")
    print ("Optional job names are:")
    print ("  ".join(config["jobs"].keys()))
    sys.exit(1)

common = config["common"]
jobname = sys.argv[1]
job = config["jobs"][jobname]

submit_config = common.copy()
submit_config.update(job)
a = bttc_trade_collector(submit_config)
a.run()