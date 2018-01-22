#!/bin/bash
BasePath="/root/Desktop"
for filename in `ls -l ${BasePath}/extra-naf | awk '$5 < 1 {print $9}'`; do
	rm ${BasePath}/extra-naf/${filename}
done

for i in ${BasePath}/US_Stock_News1/*; do
	comp1=$(basename $i .naf)

	for j in ${BasePath}/extra-naf/*; do
		comp2=$(basename $j _out.naf)
		
		if [ "${comp1}" == "${comp2}" ];then
			rm ${i}
		fi
	done
done
echo "...successfully completed!"
