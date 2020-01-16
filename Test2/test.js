var text;
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

(async (url) => {
    text = await getScript(url);
    console.log(text+'+5555555');
    text = text + '+55555';
    var parse = require('parse-diff');
    var diff = text; // edit this to access the text on the internet site using POST or Get
    var files = parse(diff);
    console.log(files.length); // number of patched files
    files.forEach(function(file) {
    console.log(file.chunks.length); // number of hunks
    console.log(file.chunks[0].changes.length) // hunk added/deleted/context lines
    console.log(file.deletions); // number of deletions in the patch
    console.log(file.additions); // number of additions in the patch
    console.log(file.chunks[0].changes[0].type);
    
});
})('https://patch-diff.githubusercontent.com/raw/AGS48353/TestingRepoNothing/pull/12.diff');

