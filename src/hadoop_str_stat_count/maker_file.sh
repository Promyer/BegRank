hdfs dfs -text /user/mi.morozov/2017/*.bz2 > big_file.txt
hdfs dfs -copyFromLocal big_file.txt  /user/miroslav.morozov/2017_dump.txt
rm big_file.txt
