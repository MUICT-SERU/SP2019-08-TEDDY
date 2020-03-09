#!/bin/bash
STRING="Start"
commit=$(git log --oneline --pretty=format:"%h;")
commitarray=(${commit//;/})
#for i in "${commitarray[@]}"
for ((i=${#commitarray[@]};i>0;i--))
do
echo "$i $STRING"
echo "${commitarray[$i]} $STRING"
#Trigger Purits stuff
git checkout ${commitarray[$i]}
read -n 1
git checkout Master
done
#echo or run tatts script