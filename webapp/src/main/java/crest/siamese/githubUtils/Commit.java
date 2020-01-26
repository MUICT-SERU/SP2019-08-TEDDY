package crest.siamese.githubUtils;

import java.util.List;

public class Commit {
    private long id;
    private List<Hunk> hunkList;

    public Commit(long id, List<Hunk> hunkList) {
        this.id = id;
        this.hunkList = hunkList;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public List<Hunk> getHunkList() {
        return hunkList;
    }

    public void setHunkList(List<Hunk> hunkList) {
        this.hunkList = hunkList;
    }
}
