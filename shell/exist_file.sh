#!/bin/bash
# author:yongbo.wang
# Date:2017-07-19 10:46:01
#====== delete already exist file ======
BasePath="/home/newsreader"
SubPath=${BasePath}"/docs"
for fileName1 in ${SubPath}/output/US_Stock_News-out/*; do
	comp1=$(basename $fileName1 _out.naf)
	
	for fileName in ${SubPath}/input/US_Stock_News/*; do
		comp2=$(basename $fileName .naf)
		
		if [ "${comp1}" == "${comp2}" ];then
			echo ${comp2}"_out.naf already exist!"
			rm ${fileName}
		fi
	done
	echo "...successfully completed!"
done
