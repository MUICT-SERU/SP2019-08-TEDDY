#!/bin/sh
#receiving of variable arguments to be revised (how to get inputPath and outputPath from DON's part)

idiomPath = "D:\senior-project\python3-idiom"

echo "Enter index name for your repository"
read indexName

#Index the cloned repo
java -jar siamese.jar -cf ./config.properties -c index -i $cloneRepoPath -n $indexName

#Search using the idioms
java -jar siamese.jar -cf ./config.properties -c search -i $idiomPath -o $outputResultPath -n $indexName

echo "Search completed"

