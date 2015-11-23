import json
import sys
import pdb
from btcc_trade_collector import btcc_trade_collector
from btcc_trade_collector import huobi_trade_collector
from btcc_client import Market
from btcc_log import create_timed_rotating_log
from btcc_log import set_log_name_prefix



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

set_log_name_prefix(jobname)
logger = create_timed_rotating_log()

submit_config = common.copy()
submit_config.update(job)

a = None
if ("trader" in submit_config and submit_config["trader"] == "huobi"):
    a = huobi_trade_collector(submit_config)
else:
    a = btcc_trade_collector(submit_config)
logger.info("btcc collector started with the following config:")
logger.info(json.dumps(submit_config))
a.run()