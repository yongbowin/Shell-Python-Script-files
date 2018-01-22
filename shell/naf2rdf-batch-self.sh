#!/bin/bash
# start time
start_time=$(date +%s)

BasePath="/root/sem-out"
ScriptPath="/usr/soft/en-sem/EventCoreference-master/scripts"
mkdir ${BasePath}/US-coref-out
# check whether naf file size is 0
for filename in `ls -l ${BasePath}/US-out | awk '$5 < 1 {print $9}'`; do
	rm ${BasePath}/US-out/${filename}
done

# count and time
i=0
j=0
for fileNum in ${BasePath}/US-out/*; do
	i=`expr $i + 1`
done
echo "FileNums:"$i

# naf ==> coref.xml
for f in ${BasePath}/US-out/*.naf;do
	# start time
	start=$(date +%s)

	base=$(basename $f)
	baseshort=$(basename $f .naf)
	echo "File: $base"
	cat ${BasePath}/US-out/${base} | ${ScriptPath}/event-coreference-en.sh > ${BasePath}/US-coref-out/${baseshort}.coref.xml
	echo "...successfully completed!"
	# end time
	end=$(date +%s)
	# execution time
	time=$(( $end - $start ))
	time2now1=$(( $end - $start_time ))
	time2now=$(( $time2now1/60 ))
	echo "From start time to now:"${time2now}"min ,Execution time:${time}s"
	j=`expr $j + 1`
	echo "Execution Rate: "$j"/"$i
done
