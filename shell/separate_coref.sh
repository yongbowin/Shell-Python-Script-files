#!/bin/bash
# ------------ 1.separate large quantity files --------------
BasePath="/root/sem-out"
BasePath1=${BasePath}/"US-coref-out2"
mkdir ${BasePath}/"sub_folders"
BasePath2=${BasePath}/"sub_folders"
num=1000
# pass param $1 present sub naf numbers
cd ${BasePath1}
floder_cal=$[`ls | wc -l` % $num]
if [ ${floder_cal} == 0 ]; then
	floder_nums=$[ `ls | wc -l` / $num ]
else
	floder_nums=$[ $[ `ls | wc -l` / $num ] + 1 ]
fi

# create sub folder
for (( create_f=0; create_f < ${floder_nums}; create_f++ )); do
        mkdir -p ${BasePath2}/"sub_"${create_f}
       # create_f=`expr $create_f + 1`
done

f=0
count=0
for i in ${BasePath1}/*.coref.xml; do
	if [ $count -lt $num ]; then
		cp $i ${BasePath2}/"sub_"${f}
	else
		count=0
		f=`expr $f + 1`
		cp $i ${BasePath2}/"sub_"${f}
	fi

	count=`expr $count + 1`
done

# ------------- 2.start processing ------------
BaseScript="/usr/soft/en-sem/EventCoreference-master/scripts"
flag="test_flag_"
flag_num=0
for sub_i in ${BasePath2}/*; do
	#${BaseScript}/naf2sem-batch-cluster.sh ${sub_i} ${flag}${flag_num}
	${BaseScript}/naf2sem-batch-nocluster.sh ${sub_i} ${flag}${flag_num}
	flag_num=`expr $flag_num + 1`
done

