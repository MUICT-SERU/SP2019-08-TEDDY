# SP2019-TEDDY
Development Branch
A repo for the senior project team TEDDY.

## Do note the following
The whole **branch** has many examples and originals soooooooooooooo

Not all mine

There are many useless files everywhere
- same config files
- duplicate .git
- tons of .vscode
- A LOT of index.js 
  - I am create too many projects on vscode

**If you want to know about which is what just send me a message**

# SP2019-TEDDY
This is a developing branch for SiameseX (Java Spring Boot) with support of both Java and Python search

## Required Components
- Apache Maven 3.6.3 or higher

## Setting up Elasticsearch 2.2.0

1. Using `git clone` to make a local copy of this branch on your machine, or download this branch as a `.zip` package and extract it.

2. Open `cmd` or PowerShell, and go to `~\SP2019-TEDDY\elasticsearch-2.2.0\bin`.

3. Execute `.\elasticsearch` command to run an Elasticsearch instance first. DO NOT close this terminal window.

## Setting up SiameseX

4. In file `~\SP2019-TEDDY\webapp\config.properties`, make sure that the value of parameter `cluster` is the same as parameter `cluster.name` in file `~\SP2019-TEDDY\elasticsearch-2.2.0\config\elasticsearch.yml`.

5. In file `~\SP2019-TEDDY\webapp\config.properties`, set the value of property `index` to be the name `teddy` which contains Python3 idioms. (To see the list of index in your Elasticsearch, go to `localhost:9200/_cat/indices?v=pretty` on a web browser).

6. In file `~\SP2019-TEDDY\webapp\config.properties`, set the value of property `elasticsearchLoc` to be the absolute path of your local Elasticsearch folder (`~\SP2019-TEDDY\elasticsearch-2.2.0`).

7. Open new `cmd` or PowerShell instance, and go to `~\SP2019-TEDDY\webbapp` directory

8. Execute the command `mvn spring-boot:run` to launch Spring-boot framework and run TEDDY

9. (Optional) On any web browser, go to `localhost:8080/search` to start using TEDDY (Google Chrome is recommended).
