DROP TABLE IF EXISTS testTbl;
CREATE EXTERNAL TABLE IF NOT EXISTS testTbl
(
    dimdate BIGINT,
    high Double,
    low Double,
    buy Double,
    sell Double,
    last Double,
    vol Double,
    vwap Double,
    prev_close Double,
    open Double,
    order_timestamp String,
    order_type String,
    order_price Double,
    order_amount Double
)
PARTITIONED BY (Day STRING, Hour STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/';

ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='07') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/07/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='08') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/08/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='09') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/09/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='10') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/10/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='11') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/11/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='12') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/12/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='13') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/13/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='14') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/14/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='15') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/15/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='16') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/16/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='17') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/17/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='18') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/18/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='19') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/19/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='20') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/20/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='21') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/21/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='22') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/22/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-17', Hour='23') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-17/23/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='00') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/00/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='01') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/01/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='02') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/02/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='03') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/03/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='04') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/04/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='05') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/05/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='06') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/06/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='07') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/07/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='08') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/08/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='09') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/09/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='10') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/10/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='11') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/11/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='12') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/12/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='13') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/13/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='14') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/14/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='15') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/15/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='16') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/16/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='17') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/17/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='18') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/18/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='19') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/19/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='20') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/20/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='21') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/21/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='22') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/22/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-18', Hour='23') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-18/23/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='00') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/00/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='01') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/01/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='02') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/02/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='03') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/03/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='04') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/04/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='05') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/05/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='06') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/06/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='07') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/07/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='08') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/08/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='09') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/09/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='10') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/10/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='11') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/11/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='12') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/12/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='13') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/13/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='14') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/14/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='15') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/15/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='16') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/16/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='17') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/17/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='18') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/18/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='19') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/19/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='20') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/20/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='21') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/21/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='22') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/22/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-19', Hour='23') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-19/23/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-20', Hour='00') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-20/00/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-20', Hour='01') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-20/01/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-20', Hour='02') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-20/02/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-20', Hour='03') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-20/03/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-20', Hour='04') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-20/04/';
ALTER TABLE testTbl ADD IF NOT EXISTS PARTITION (Day='2015-11-20', Hour='05') LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/btccny-price-and-order/2015-11-20/05/';
DROP TABLE IF EXISTS outputTbl;
CREATE EXTERNAL TABLE IF NOT EXISTS outputTbl
(
    ID  INT,
    dimdate BIGINT,
    buy Double,
    sell Double,
    last Double
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION 'wasb://btcc@guohaodata.blob.core.windows.net/cooked/';

INSERT OVERWRITE TABLE outputTbl
SELECT
    row_number() over(order by dimdate) as ID,
    dimdate,
    buy,
    sell,
    last
FROM
(
    SELECT
        dimdate,
        MIN(buy) as buy,
        MIN(sell) as sell,
        MIN(last) as last
    FROM testTbl
    GROUP BY dimdate
)g
ORder by dimdate;
