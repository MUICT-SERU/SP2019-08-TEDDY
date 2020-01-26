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

    public void addIdiomatic(int id, int sim, ArrayList<Document> results) {
        JSONArray jarray = new JSONArray();
        for (crest.siamese.document.Document r: results) {

            if(r.isIdiomatic()) { jarray.add(createClone(r)); }

        }
        jIdiomatic.add(jarray);
    }

    public void addNonidiomatic(int id, int sim, ArrayList<Document> results) {
        JSONArray jarray = new JSONArray();
        for (crest.siamese.document.Document r: results) {

            if(!r.isIdiomatic()) {jarray.add(createClone(r)); }

        }
        jNonidiomatic.add(jarray);
    }

    private JSONObject createClone(crest.siamese.document.Document d) {
        String file = d.getFile().split(".java_")[0]; //+ ".java";
        JSONObject item = new JSONObject();
        item.put("file", file);
        item.put("start", String.valueOf(d.getStartLine()));
        item.put("end", String.valueOf(d.getEndLine()));
        item.put("license", d.getLicense());
        item.put("originalSrc", d.getOriginalSource());

        //More representations of the clone (not used for now)
        item.put("tokenizedSrc", d.getTokenizedSource());
        item.put("t2Src", d.getT2Source());
        item.put("t1Src", d.getT1Source());
        item.put("src", d.getSource());

        //For Python3 idiom (not used for now)
        item.put("recommendIdiom", d.getRecommendIdiom());
        item.put("idiomatic", d.isIdiomatic());

        return item;
    }

//    Expected Result in JSON Format
//    {
//        "idiomatic" : 2 ,
//            "non-idiomatic" : 1 ,
//            "idiomatic_hits" : [
//        {
//            "file" : ,
//            "start" : ,
//            "end" : ,
//            "src" : ,
//            "t2src" : ,
//            "t1src" : ,
//            "tokenizedSrc" : ,
//            "origsrc" : ,
//            "license" : ,
//            "url" : ,
//            "idiomatic" : ,
//            "recommend" : ,
//        } , {
//        "file" : ,
//        "start" : ,
//        "end" : ,
//        "src" : ,
//        "t2src" : ,
//        "t1src" : ,
//        "tokenizedSrc" : ,
//        "origsrc" : ,
//        "license" : ,
//        "url" : ,
//        "idiomatic" : ,
//        "recommend" : ,
//    }
//	] ,
//        "non-idiomatic_hits" : [
//        {
//            "file" : ,
//            "start" : ,
//            "end" : ,
//            "src" : ,
//            "t2src" : ,
//            "t1src" : ,
//            "tokenizedSrc" : ,
//            "origsrc" : ,
//            "license" : ,
//            "url" : ,
//            "idiomatic" : ,
//            "recommend" : ,
//        }
//	]
//    }
    public String getJSONString() {
        jsonObject.put("idiomatic", String.valueOf(jIdiomatic.size()));
        jsonObject.put("non-idiomatic", String.valueOf(jNonidiomatic.size()));
        jsonObject.put("idiomatic_hits", jIdiomatic);
        jsonObject.put("non-idiomatic_hits", jNonidiomatic);
        return jsonObject.toString();
    }


}
