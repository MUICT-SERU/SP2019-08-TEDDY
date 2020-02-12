package com.siamesex.standalone.controller;

import com.siamesex.standalone.model.EchoText;
import com.siamesex.standalone.model.Search;
import crest.siamese.Siamese;
import crest.siamese.githubUtils.*;
import echotest.EchoTest;
import org.apache.commons.lang.exception.ExceptionUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class SearchController {
    // Logger
    private static final Logger logger = LoggerFactory.getLogger(SearchController.class);
    // Siamese variable associated with Siamese Java app
    private final Siamese siamese;
    private long commitID;
    private final EchoTest echoTest;

    // When spring containers finds @autowired annotation with setter methods,it autowires bean byType .
    // byType – Allows a property to be autowired if exactly one bean of the property type exists in the container.
    // It can be applied with:
    //  On setter methods
    //  On Properties
    //  On Constructors
    //  @Autowired with arguments
    @Autowired
    public SearchController(Siamese siamese, EchoTest echoTest)
    {
        this.siamese = siamese;
        this.echoTest = echoTest;
    }

    // Mapping ------------------------------------

    // Normal form
    @GetMapping("/search")
    public String searchShowForm(Model model){
        logger.info("Access search form");

        // Create model (java data class) to be embed with the return html template
        model.addAttribute("search", new Search());
        return "search";
    }

    // Submit Form with search query
    @PostMapping("/search")
    public String searchSubmit(@ModelAttribute Search search) {
        logger.info("search length: {}", search.getContent().length());

        // use the query content from the model search then trigger siamese to invoke query search
        // display them in result html template
        JSONObject resultJSON = queryResultJSON(search.getContent());
        search.setResult(resultJSON);
        return "result";
    }

    // API ---------------------------------------
    @PostMapping(path = "/api/searchJSON", produces = "application/json; charset=UTF-8")
    @ResponseBody
    public JSONObject searchSubmitJSON(@RequestBody Search search) {
        logger.info("search length: {}", search.getContent().length());

        JSONObject resultJSON = queryResultJSON(search.getContent());
        return resultJSON;
    }

    @PostMapping(path = "/api/echo", produces = "application/json; charset=UTF-8")
    @ResponseBody
    public EchoText searchSubmitJSON(@RequestBody EchoText echoText) {
        logger.info("echoText", echoText.getText());

        String result = echoTest.echoString(echoText.getText());
        EchoText returnEcho = new EchoText();
        returnEcho.setText(result);
        return returnEcho;
    }

    // Invoking search query to Siamese JAVA App
    private JSONObject queryResultJSON(String searchString) {
        JSONObject resultJSON = new JSONObject();

        try {
            // String result = this.siamese.queryWithString(searchString);
            String result = this.siamese.queryWithString(searchString);

            // TODO: Make sure result returned from siamese is JSON!
            // For now, check it in parse exception
            resultJSON = parseStringToJSON(result);

            // TODO: What to Log from the result?
            // Placeholder, clones quantity
            // Current version 9 Mar 19, return clones: [[ { }, { }, { }, ... ]]
            // Comment from Chaiyong mentioned that it should be [ { }, { }, { }, ... ]
            JSONArray clones = (JSONArray) resultJSON.get("clones");
            logger.info("query result: found {} duplications", clones.size());
            logger.info("query result content {}", clones.toString());
        } catch (Exception e) {
            logger.error("exception: {}", ExceptionUtils.getStackTrace(e));
            e.printStackTrace();
        }
        return resultJSON;
    }

    /////////////////// Teddy Implementation ///////////////////

    // Submit the PR query from GitHub
    // This method supposes to handles the API POST and pass the content for further querying
    @PostMapping("/githubSearch")
    public String searchSubmitGithub(@ModelAttribute Commit query) {

        logger.info("commit ID : ", query.getId());
        logger.info("commit content : ", query.toString());

        // use the query content from the model search then trigger siamese to invoke query search
        // display them in result html template
        // TODO: Somehow process the raw query received and extract only the clone snippets
        String actualQuery = "";

        // JSONObject resultJSON = queryResultJSONGithub(query.getHunkList());

        //Keep the commit ID to be used when sending back the JSON response
        // this.commitID = query.getId();
        // query.setResult(resultJSON);
        return "result";
    }

    //--------------------------------------- API ---------------------------------------
    @PostMapping(path = "/api/searchJSONGithub", produces = "application/json; charset=UTF-8")
    @ResponseBody
    public JSONObject githubSearchJSON(@RequestBody PullRequest query) {

        logger.info("PR Content : ", query.toString());

        JSONObject resultJSON = queryResultJSONGithub(query.getCommits());
        return resultJSON;

    }

    private JSONObject queryResultJSONGithub(List<Commit> commits) {

        JSONObject resultJSON = new JSONObject();

        try {

            GitHubJSONFormatter formatter = new GitHubJSONFormatter();

            for (Commit c : commits) {

                List<HunkQuery> hunks = c.getHunkList();
                JSONArray hunkArrays = new JSONArray();     // The array of JSON Hunks for each commit

                for (HunkQuery h : hunks) {

                    /**
                     * Each hunkResult is as this example:
                     *  {
                     *    "chunknum":"1",
                     *    "filename":"gg.py",
                     *    "startline":"2",
                     *    "endline":"5",
                     *    "source":"+print("Hello world")\r"
                     *    "idiomatic":"false",
                     *    "recommend":"Yare yare daze"
                     *    }
                     * **/
                    JSONObject hunkResult = this.siamese.queryWithGitHub(h);
                    hunkArrays.add(hunkResult);
                    // TODO: Combine multiple hunkResults into a collection of Commit
                }

                // Create the JSON Commit for each commit using commit ID and array of JSON Hunks
                JSONObject commitResult = formatter.createCommitResult(c.getId(), hunkArrays);
                formatter.addCommittoArray(commitResult);

            }

            /**The Final JSON Response Object
             *  {
             *      "commitID":"tt3xO1"
             *      "totalIdiomatic":"3"
             *      "totalNonidiomatic":"2"
             *      "idiomaticCommits":
             *          [
             *               {
             *                 "chunknum":"1",
             *                 "filename":"gg.py",
             *                 "startline":"2",
             *                 "endline":"5",
             *                 "source":"+with open()\r"
             *                 "idiomatic":"true",
             *                 "recommend":"N/A" } , ... , {}
             *           ]
             *      "nonidiomaticCommits":
             *          [
             *               {
             *                 "chunknum":"2",
             *                 "filename":"cc.py",
             *                 "startline":"4",
             *                 "endline":"12",
             *                 "source":"+open file()\r\nvar test = 60\n"
             *                 "idiomatic":"false",
             *                 "recommend":"Yare" } , ... , {}
             *           ]
             *  }
             * **/

            JSONObject responseBody = formatter.createPullRequestResult(formatter.getjCommitsResult());

            // Result logging
            // Placeholder, clones quantity
            // Current version 9 Mar 19, return clones: [[ { }, { }, { }, ... ]]
            // Comment from Chaiyong mentioned that it should be [ { }, { }, { }, ... ]
            JSONArray idiomaticCommits = (JSONArray) resultJSON.get("idiomaticCommits");
            JSONArray nonidimaticCommits = (JSONArray) resultJSON.get("nonidiomaticCommits");
            logger.info("Search result: found {} idiomatic commits", idiomaticCommits.size());
            logger.info("Search result: found {} non-idiomatic commits", nonidimaticCommits.size());
            logger.info("Idiomatic commits: {}", idiomaticCommits.toString());
            logger.info("Nonidiomatic commits: {}", nonidimaticCommits.toJSONString());

            return responseBody;

        } catch (Exception e) {
            logger.error("exception: {}", ExceptionUtils.getStackTrace(e));
            e.printStackTrace();
        }
        return resultJSON;
    }

    // Utilities
    private JSONObject parseStringToJSON(String stringToParse) {
        JSONObject jsonObject = new JSONObject();
        try {
            JSONParser parser = new JSONParser();
            jsonObject = (JSONObject) parser.parse(stringToParse);
        } catch (ParseException e) {
            logger.error("exception: {}", ExceptionUtils.getStackTrace(e));
            e.printStackTrace();
        }
        return jsonObject;
    }

}
