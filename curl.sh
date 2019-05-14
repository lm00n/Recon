#!/bin/bash
#script para corroborar size y response, util para validar DEFAULT WEB PAGE
#Usar formato https://WEB:PUERTO
for i in `cat $1`;do
        res=$(curl -IL -ks $i | grep -e "HTTP" | cut -d " " -f 2)
	len=$(curl -IL -ks $i | grep -e "content-length:" | cut -d " " -f 2 | tr '\r' ' ')
	url=$(echo $i | tr '\n' ' ')
	echo $url,$res,$len >> $1-result.csv
done
