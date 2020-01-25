# SP2019-TEDDY-SiameseX
This is a developing branch for SiameseX (Java Spring Boot) with support of both Java and Python search

## Required Components
- Elasticsearch **2.2.0**
- Apache Maven 3.6.3 or higher

## Setting up Elasticsearch 2.2.0
1. In `.\config\elasticsearch.yml` file of Elasticsearch folder, add `index.query.bool.max_clause_count: 20480` and `action.auto_create_index: .marvel-*` to the file. Save and close the file.

1. Using `cmd` or PowerShell Go to `.\bin` directory of your local Elasticsearch folder.
2. Execute `.\elasticsearch` command to run an Elasticsearch instance.

## Setting up TEDDY
1. Use `git clone` to make a local copy of this branch on your machine, or download this branch as a `.zip` package and extract it.

2. From `.\config\elasticsearch.yml` file in the Elasticsearch folder, check the value of the parameter `cluster.name`, then set the value of the property `cluster` inside `.\webapp\config.properties` in SP2019-TEDDY folder to be the same name.

3. In `config.properties` file, be sure to set the value of property `index` to be the name of an existing index in your local Elasticsearch. (To see the list of index in your Elasticsearch, go to `localhost:9200/_cat/indices?v=pretty` on a web browser).

4. Using another `cmd` or PowerShell instance, go to `.\webbapp` directory of SP2019-TEDDY folder

5. Use the command `mvn spring-boot:run` to launch Spring-boot framework and run TEDDY

6. On any web browser, go to `localhost:8080/search` to start using TEDDY (Google Chrome is recommended).
