
// A plugin is a Node module that exports a function which takes a `robot` argument

module.exports = robot => {
  

  //variables to be moved here
  
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

    var fullreponame = repo.full_name;
    var pullnum = pr.number;
    var finalurl = 'https://patch-diff.githubusercontent.com/raw/'+fullreponame+'/pull/'+pullnum+'.diff'
    

    
    console.log(finalurl);
    var text;
    //async'ed for getting scripts
    (async (url) => {
      text = await getScript(url);

      var parse = require('parse-diff');
      var diff = text; // edit this to access the text on the internet site using POST or Get
      var files = parse(diff);


      var PRWhole = [];
      var pullRequestJSON = {};
      var Commit = [];
      var hunk=  {};
      var changeline = [];
      var chunkcount = 0;
      var changelncount = 0;

      console.log(files[0].index[0].slice(files[0].index[0].length-8,files[0].index[0].length)); //This cuts the ID of the commmit 
      
      files.forEach(function(file) {
        chunkcount = 0;
      console.log(file);
      file.chunks.forEach(function(chunk){
        
        chunk.changes.forEach(function(change){
          //console.log(change);
          if(change.type == 'add')
          {
            changeline.push(change.content);
            //Create a JSON OBJ here that takes in all the addition 
            changelncount++;
          }
        });
      
        hunk = {
          "chunknum":chunkcount,
          "startline": chunk.newStart,
          "endline": chunk.newStart+chunk.newLines,
          "filename": file.to,
          "edit": changeline
        };
        Commit.push(hunk);
        chunkcount = chunkcount+1;
        changeline =[];
        changelncount = 0;
      });
      pullRequestJSON = { 
        "commitID":file.index[0].slice(file.index[0].length-7,file.index[0].length),
        "commitData":Commit
      }
      PRWhole.push(pullRequestJSON);

      
      
  });
  //console.log((PRWhole));
  console.log("Starting Post");
  
  const axios = require('axios')
  axios.post('http://localhost:8080/api/searchJSONGithub', {
  PRWhole
})
.then((res) => {
  console.log(`statusCodeLogged: ${res.statusCode}`)
  if(res.statusCode == 200)
  {
  Sxresponse = res.data

  console.log(Sxresponse)
  

    // Parameters for the status API
    var passCheck = 'failure';
    console.log(Sxresponse);
    console.log("Starting Passcheck Process");
    const paramsStatus = {
      sha: pr.head.sha,
      context: 'Pythonic Idiom result',
      state: passCheck ? 'success' : 'failure',
      //state: 'success',
      description: `Pass Check Feature Currently Disabled`
      //description: 'An Automated System for the PR '
    }


    console.log("Starting Commenting Process");
    const commentparams = {
      owner: repo.owner.login,
      repo: repo.name,
      
      number: pullnum,
      //body: JSON.stringify(Sxresponse)
      body: 'This version will show the results as a PassCheck Method Detailed information will be shown in later versions :D '
    }


    context.github.repos.createStatus(context.repo(paramsStatus));

    context.github.issues.createComment(context.repo(commentparams));
    

    }
    else
    {
      console.log("ERROR STATUS CODE NOT 200 Currently Error connecting with SiameseX ");
    }

})
.catch((error) => {
  console.error(error)
})


})(finalurl);



  
    
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
