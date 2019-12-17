#!/usr/bin/env bash

set -e

OUTDIR=/user/mi.morozov/stats1/
hadoop fs -rm -r -f $OUTDIR

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-file mapper.py -file reducer.py \
	-input '/tmp/empty_test.txt' -output $OUTDIR \
	-mapper mapper.py -reducer reducer.py 

echo job finished, see output in $OUTDIR
