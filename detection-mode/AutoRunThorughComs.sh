#!/bin/bash
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
if [ "$3" != "" ]; then
	echo 'Elasticsearch index name =' $3
else
    echo "parameter 3 is empty"
fi
git clone $1 
cd */.
#ls -l
gitclonedhead=$(git symbolic-ref --short HEAD)
commit=$(git log --oneline --pretty=format:"%h;")
commitarray=(${commit//;/})
for ((i=${#commitarray[@]};i>0;i--))
do
echo "Commit#$i ID:${commitarray[$i]} >> Starting search"

git checkout ${commitarray[$i]}
# Calling shell script that runs Siamese.jar, perform indexing and searching
#=====================================
./../CallSiamese.sh $PWD ./../../python-idioms $2 $3 ${commitarray[$i]} $i
#=====================================

## Uncomment for manual iteration of commit versions
echo "Press any Key to Continue to the next commit"
read -n 1
git checkout $gitclonedhead
done
## Deleting the repo folder after iteration is completed
cd ..
rm -r */
## echo or run tatts scrip