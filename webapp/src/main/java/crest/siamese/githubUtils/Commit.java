package crest.siamese.githubUtils;

import org.json.simple.JSONObject;

import java.util.List;

public class Commit {

    private long id;
    private List<HunkQuery> hunkList;
    private JSONObject result;

    public Commit(long commit_id, List<HunkQuery> hunkList) {
        this.id = commit_id;
        this.hunkList = hunkList;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public List<HunkQuery> getHunkList() {
        return hunkList;
    }

    public void setHunkList(List<HunkQuery> hunkList) {
        this.hunkList = hunkList;
    }

    public String toString() {
        StringBuilder hunksString = new StringBuilder();

        for (HunkQuery h : hunkList) {
            hunksString.append("\nhunk no.: ").append(h.getHunkNum());
            hunksString.append("\nfile name: ").append(h.getFileName());
            hunksString.append("\nstart: ").append(h.getStartline()).append(", end: ").append(h.getEndline());
            hunksString.append("\nsource: ").append(h.getSource());
        }

        return hunksString.toString();
    }

    public void setResult(JSONObject result) {
        this.result = result;
    }
}
