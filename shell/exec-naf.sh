#!/bin/bash
# author:yongbo.wang
# Date:2016-11-30 16:11:01
#====== get the file name ======
BasePath="/home/newsreader"
SubPath=${BasePath}"/docs"
for fileName in ${SubPath}/input/100-naf/*; do
	# start time
	start=$(date +%s)
	# get filename
	in_file_name=$(basename $fileName)
	echo '===>'"now converting "${in_file_name}" ......"
	# output filename
	out_file_name="$(basename $fileName .naf)_out.naf"
	# converting article to naf
	echo "out_file_name:"${out_file_name}
	
	floder=${SubPath}"/output/100-naf-out"
	if [ ! -d "$folder"]; then
		mkdir "$folder"
	fi

	${BasePath}/pipeline/run_pipeline.sh ${SubPath}/input/100-naf/${in_file_name} > ${floder}/${out_file_name}
	echo "...successfully completed!"
	# end time
	end=$(date +%s)
	# execution time
	time=$(( $end - $start ))
	echo "Execution time:${time}"
done
