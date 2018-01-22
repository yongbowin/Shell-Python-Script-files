#!/bin/bash
BasePath="/root/sem-out/US-coref-out"
for filename in `ls -l ${BasePath} | awk '$5 < 1 {print $9}'`; do
	rm ${BasePath}/${filename}
done
