#!/bin/sh
# This shell must receive the path of where the GitHub is cloned and stored in $cloneRepoPath


idiomPath = "D:\senior-project\python3-idiom"

# Reading of $indexName variable is optional if Don's script can get ES index's name from the user already
echo "Enter index name for your repository"
read indexName

# Indexing the cloned repo
java -jar siamese.jar -cf ./config.properties -c index -i $cloneRepoPath -n $indexName

# Searching in the newly created ES index using the idiom/non-idiom Python snippets
# '-n' is a new command-line overriding parameter of .jar for index in config.properties
java -jar siamese.jar -cf ./config.properties -c search -i $idiomPath -o $outputResultPath -n $indexName

echo "Search completed"

