#!/usr/bin/env bash

set -e

OUTDIR=/user/miroslav.morozov/stats/
hadoop fs -rm -r -f $OUTDIR

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-file mapper.py -file reducer.py \
	-input '/tmp/miroslav.morozov/out/' -output $OUTDIR \
	-mapper mapper.py -reducer reducer.py -combiner reducer.py

echo job finished, see output in $OUTDIR
