#!/usr/bin/env bash

set -e

OUTDIR=/user/mi.morozov/stats/
hadoop fs -rm -r -f $OUTDIR

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.reduce.tasks=8 \
	-file src/hadoop_str_stat_count/mapper.py -file src/hadoop_str_stat_count/reducer.py \
	-input '/user/mi.morozov/2017_dump.txt' -output $OUTDIR \
	-mapper src/hadoop_str_stat_count/mapper.py -reducer src/hadoop_str_stat_count/reducer.py

echo job finished, see output in $OUTDIR
