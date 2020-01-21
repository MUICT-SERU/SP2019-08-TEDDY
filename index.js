
// A plugin is a Node module that exports a function which takes a `robot` argument
module.exports = robot => {

  
  // Listen for a pull request being opened or synchronized
  robot.on('pull_request', async context => {
    // Just assign a variable to make our life easier
    const pr = context.payload.pull_request;
    const repo = context.payload.repository;

    // Get all the commits in the pull request
   const compare = await context.github.repos.compareCommits(context.repo({
      base: pr.base.sha,
      head: pr.head.sha
    }));

    // const passCheck = compare.data.commits.every(data => {
    //   return data.commit.message.match(/DevelopmentBranchTesting/);
    // });
    var fullreponame = repo.full_name;
    var pullnum = pr.number;
    var finalurl = 'https://patch-diff.githubusercontent.com/raw/'+fullreponame+'/pull/'+pullnum+'.diff'
    
    //This needs to be reworked from issues to pull requst
    //const autocomment = context.pulls({body: 'Probot will autocomment when running :D'})
    //context.github.issues.createComment(autocomment)
    
    console.log(finalurl);
    var text;
    //async'ed for getting scripts
    (async (url) => {
      text = await getScript(url);
      //Testing with only console log
      //console.log(text+'+5555555');
      //text = text + '+55555';
      var parse = require('parse-diff');
      var diff = text; // edit this to access the text on the internet site using POST or Get
      var files = parse(diff);
      console.log(files.length); // number of patched files
      files.forEach(function(file) {
      console.log(file.chunks.length); // number of chunks
      console.log(file.chunks[0].changes.length) // chunk added/deleted/context lines
      //console.log(file.deletions); // number of deletions in the patch
      //console.log(file.additions); // number of additions in the patch
      console.log(file.chunks[0]);
      
  });
  })(finalurl);

  const { exec } = require("child_process");
  //move this up top later with predefined var's 
  var val = "ping www.google.com";
  
  exec(val, (error, stdout, stderr) => {
      if (error) {
          console.log(`error: ${error.message}`);
          return;
      }
      if (stderr) {
          console.log(`stderr: ${stderr}`);
          return;
      }
      console.log(`stdout: ${stdout}`);
  });

    // Parameters for the status API
    /*const params = {
      sha: pr.head.sha,
      context: 'Pass Checked',
      state: passCheck ? 'success' : 'failure',
      description: `Your commits ${passCheck ? 'have' : 'have not'} passed all the checks`
    }*/
    //New Params for issues
    /*const params = {
      
      title: 'Issue Created on PullRQ',
      body: 'Automatically Generated',
      
    }*/
    /*const params = {
      owner: 'AGS48353',
      repo: 'TestingRepoNothing',
      path: 'README.md'
    }*/
    

    // Create the status
    //return context.github.repos.createStatus(context.repo(params));
    //return context.github.issues.create(context.repo(params));

    /*context.github.repos.getContents({
      owner: 'AGS48353',
      repo: 'TestingRepoNothing',
      path: 'BST/insert.java'
    })
    
      .then(result => {
        // content will be base64 encoded
        const content = Buffer.from(result.data.content, 'base64').toString()
        console.log(content)
      })*/

  
    
  });
};
//This is the script for URL
const getScript = (url) => {
  return new Promise((resolve, reject) => {
      const http      = require('http'),
            https     = require('https');

      let client = http;

      if (url.toString().indexOf("https") === 0) {
          client = https;
      }

      client.get(url, (resp) => {
          let data = '';

          // A chunk of data has been recieved.
          resp.on('data', (chunk) => {
              data += chunk;
          });

          // The whole response has been received. Print out the result.
          resp.on('end', () => {
              resolve(data);
          });

      }).on("error", (err) => {
          reject(err);
      });
  });
};