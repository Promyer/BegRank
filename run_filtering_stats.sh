#!/usr/bin/env bash

set -e

OUTDIR=/user/mi.morozov/clean_stats/
hadoop fs -rm -r -f $OUTDIR

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-D mapred.reduce.tasks=8 \
	-file src/hadoop_make_features/python/mapper.py -file src/hadoop_make_features/python/reducer.py \
	-file urls.dat -file hosts.dat -file queries.dat \
	-input '/user/mi.morozov/stats' -output $OUTDIR \
	-mapper src/hadoop_make_features/python/mapper.py -reducer src/hadoop_make_features/python/reducer.py

echo job finished, see output in $OUTDIR
