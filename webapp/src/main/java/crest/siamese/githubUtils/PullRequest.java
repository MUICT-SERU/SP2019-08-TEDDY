package crest.siamese.githubUtils;

import org.json.simple.JSONObject;

import java.util.List;

public class PullRequest {

    private List<Commit> commits;

    // Following Search.java approach
    private String content;
    private JSONObject result;

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public JSONObject getResult() {
        return result;
    }

    public void setResult(JSONObject result) {
        this.result = result;
    }

    public PullRequest() {
        super();
    }

    public PullRequest(List<Commit> commits) {
        this.commits = commits;
    }

    public void addCommit(Commit newCommit) {
        commits.add(newCommit);
    }

    public List<Commit> getCommits() {
        return this.commits;
    }



}
