package crest.siamese.githubUtils;

import com.sun.org.apache.xpath.internal.operations.String;
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

    @Override
    public java.lang.String toString() {

        StringBuilder stringBuilder = new StringBuilder();

        stringBuilder.append("{ PR Commits: [");

        for(Commit c : commits) {
            stringBuilder.append("\t{\n");
            stringBuilder.append("\tcommitID: ").append(c.getId()).append(",\n");
            stringBuilder.append("\tcommitData: [\n");

            for(HunkQuery h : c.getHunkList()) {
                stringBuilder.append("\t\t{\n");
                stringBuilder.append("\t\thunk no.: ").append(h.getHunkNum()).append(",\n");
                stringBuilder.append("\t\tfilename: ").append(h.getFileName()).append(",\n");
                stringBuilder.append("\t\tstartline: ").append(h.getStartline()).append(",\n");
                stringBuilder.append("\t\tendline: ").append(h.getEndline()).append(",\n");
                stringBuilder.append("\t\tsrc: ").append(h.getSource()).append("\n");
                stringBuilder.append("\t\t}\n");
            }

            stringBuilder.append("\t]\n");
            stringBuilder.append("\t}\n");
        }

        stringBuilder.append("]\n}");

        return stringBuilder.toString();
    }


}
