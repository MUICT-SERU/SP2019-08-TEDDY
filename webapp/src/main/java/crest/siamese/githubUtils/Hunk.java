package crest.siamese.githubUtils;

public class Hunk {
    private long commitID;
    private String file;
    private int startline;
    private int endline;
    private String source;
    private String t2Source;
    private String t1Source;
    private String tokenizedSource;
    private String originalSource;

    public long getCommitID() {
        return commitID;
    }

    public void setCommitID(long commitID) {
        this.commitID = commitID;
    }

    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }

    public int getStartline() {
        return startline;
    }

    public void setStartline(int startline) {
        this.startline = startline;
    }

    public int getEndline() {
        return endline;
    }

    public void setEndline(int endline) {
        this.endline = endline;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public String getT2Source() {
        return t2Source;
    }

    public void setT2Source(String t2Source) {
        this.t2Source = t2Source;
    }

    public String getT1Source() {
        return t1Source;
    }

    public void setT1Source(String t1Source) {
        this.t1Source = t1Source;
    }

    public String getTokenizedSource() {
        return tokenizedSource;
    }

    public void setTokenizedSource(String tokenizedSource) {
        this.tokenizedSource = tokenizedSource;
    }

    public String getOriginalSource() {
        return originalSource;
    }

    public void setOriginalSource(String originalSource) {
        this.originalSource = originalSource;
    }

    public Hunk(
            long commitID,
            String file,
            int startline,
            int endline,
            String source,
            String t2Source,
            String t1Source,
            String tokenizedSource,
            String originalSource
    ) {
        this.commitID = commitID;
        this.file = file;
        this.startline = startline;
        this.endline = endline;
        this.source = source;
        this.t2Source = t2Source;
        this.t1Source = t1Source;
        this.tokenizedSource = tokenizedSource;
        this.originalSource = originalSource;
    }

    @Override
    public String toString() { return commitID + ":" + file + ": " + originalSource;}

    public String getLocationString() { return commitID + ":" + file + " (" + startline + "," + endline + ")"; }

}
