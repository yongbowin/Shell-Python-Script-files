#!/bin/bash
# author:yongbo.wang
# Date:2016-11-30 16:11:01
#====== get the file name ======
inputPath="/home/wyb/Downloads"
for fileName in ${inputPath}/*; do
	# start time
	start=$(date +%s)
	# get filename
	file_name=$(basename $fileName)
	echo '===>'"now converting "${file_name}" ......"
	# output filename
	new_file_neme="$(basename $fileName .naf)_out.naf"
	# converting article to naf
	echo "new_file_neme:"${new_file_neme}
	#pipeline/run_pipeline.sh docs/input/${file_name} > docs/output/${new_file_neme}
	echo "...successfully completed!"
	# end time
	end=$(date +%s)
	# execution time
	time=$(( $end - $start ))
	echo "Execution time:${time}"
done
