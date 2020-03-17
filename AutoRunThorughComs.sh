#!/bin/bash
STRING="Start"
if [ "$1" != "" ]; then
    echo 'GitHub Repo To Clone =' $1
else
    echo "parameter 1 is empty"
fi
if [ "$2" != "" ]; then
	echo 'Output Result Location =' $2
else
    echo "parameter 2 is empty"
fi
git clone $1 
cd */.
ls -l
gitclonedhead=$(git symbolic-ref --short HEAD)
commit=$(git log --oneline --pretty=format:"%h;")
commitarray=(${commit//;/})
#for i in "${commitarray[@]}"
for ((i=${#commitarray[@]};i>0;i--))
do
echo "$i $STRING"
echo "${commitarray[$i]} $STRING"
#Trigger Purits stuff
git checkout ${commitarray[$i]}
#Purit please add your functions between here
#=====================================
./call_siamese pwd $i 
#=====================================
echo "Press any Key to Continue to the next commit"
read -n 1
git checkout $gitclonedhead
done
#echo or run tatts script
