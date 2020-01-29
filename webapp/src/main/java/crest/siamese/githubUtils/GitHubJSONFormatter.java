package crest.siamese.githubUtils;

import crest.siamese.document.Document;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import crest.siamese.githubUtils.Commit;
import crest.siamese.githubUtils.Hunk;
import crest.siamese.githubUtils.PullRequest;

import java.util.ArrayList;

public class GitHubJSONFormatter {

    JSONArray jIdiomatic;
    JSONArray jNonidiomatic;
    JSONObject jsonObject;

    public GitHubJSONFormatter() {
        this.jIdiomatic = new JSONArray();
        this.jNonidiomatic = new JSONArray();
        this.jsonObject = new JSONObject();
    }

    public void addHunktoArray(JSONObject hunkResult) {

         if (hunkResult.get("idiomatic").equals("true")) {
             jIdiomatic.add(hunkResult);
         } else {
             jNonidiomatic.add(hunkResult);
         }

    }

    public JSONObject createHunkResult(HunkResult r) {

        JSONObject item = new JSONObject();

        String file = r.getFileName().split(".py_")[0];

        item.put("chunknum", String.valueOf(r.getHunkNum()));
        item.put("filename", file);
        item.put("startline", String.valueOf(r.getStartLine()));
        item.put("endline", String.valueOf(r.getEndLine()));
        item.put("source", r.getSource());
        item.put("idiomatic", String.valueOf(r.isIdiomatic()));
        item.put("recommend", r.getRecommendIdiom());

        return item;
    }

    public JSONObject createCommitResult(long commitID) {

        this.jsonObject.put("commitID", String.valueOf(commitID));
        this.jsonObject.put("totalIdiomatic", String.valueOf(jIdiomatic.size()));
        this.jsonObject.put("totalNonidiomatic", String.valueOf(jNonidiomatic.size()));
        this.jsonObject.put("idiomaticCommits", jIdiomatic);
        this.jsonObject.put("nonidiomaticCommits", jNonidiomatic);

        return this.jsonObject;

    }

    public String getJSONString() {
        jsonObject.put("idiomatic", String.valueOf(jIdiomatic.size()));
        jsonObject.put("non-idiomatic", String.valueOf(jNonidiomatic.size()));
        jsonObject.put("idiomatic_hits", jIdiomatic);
        jsonObject.put("non-idiomatic_hits", jNonidiomatic);
        return jsonObject.toString();
    }


}
