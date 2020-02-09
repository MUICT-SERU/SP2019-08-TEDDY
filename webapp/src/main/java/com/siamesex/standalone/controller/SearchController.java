package com.siamesex.standalone.controller;


import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.siamesex.standalone.model.*;
import crest.siamese.Siamese;
import crest.siamese.githubUtils.*;
import org.apache.commons.lang.exception.ExceptionUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;

@Controller
public class SearchController {
    // Logger
    private static final Logger logger = LoggerFactory.getLogger(SearchController.class);
    // Siamese variable associated with Siamese Java app
    private final Siamese siamese;

    // When spring containers finds @autowired annotation with setter methods,it autowires bean byType .
    // byType – Allows a property to be autowired if exactly one bean of the property type exists in the container.
    // It can be applied with:
    //  On setter methods
    //  On Properties
    //  On Constructors
    //  @Autowired with arguments
    @Autowired
    public SearchController(Siamese siamese)
    {
        this.siamese = siamese;

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
    public JSONObject githubSearchJSON(@RequestBody OverPR JSONReq) {

        logger.info("PR Content : ", JSONReq.getPRWhole().toString());

        PullRequest query = JSONReq.getPRWhole();

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


    // Testing about JSON Serialization-Deserialization
    @PostMapping(path = "/api/commit")
    public void handleCommit(@RequestBody User user) {
        System.out.println("Username: " + user.getUsername());
        System.out.println("Password: " + user.getPassword());
    }

    // Testing about JSON Serialization-Deserialization 2
    @PostMapping(path = "/api/commit2")
    public void handleArray(@RequestBody Branch branch) throws IOException {
        System.out.println("ID: " + branch.getBranchID());
        System.out.println("Username: " + branch.getMember().getUsername());
        System.out.println("Password: " + branch.getMember().getPassword());

        for(Item i : branch.getItems()) {
            System.out.println("Item name: " + i.getName() + " Item price: " + i.getPrice());
        }

        ObjectMapper mapper = new ObjectMapper();
        mapper.configure(JsonParser.Feature.ALLOW_UNQUOTED_FIELD_NAMES, true);

        // User user = mapper.readValue(branch.getMember(),User.class);

        // System.out.println("Username: " + user.getUsername());
        // System.out.println("Password: " + user.getPassword());
    }

}
