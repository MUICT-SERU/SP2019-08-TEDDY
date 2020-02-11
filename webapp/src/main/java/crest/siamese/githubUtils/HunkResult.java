package crest.siamese.githubUtils;

public class HunkResult implements Hunk {

    private boolean idiomatic = false;
    private String recommendIdiom = "Null";
    private int hunkNum, startLine, endLine;
    private String source, fileName;

    public boolean isIdiomatic() {
        return idiomatic;
    }
    public void setIdiomatic(boolean idiomatic) {
        this.idiomatic = idiomatic;
    }

    public String getRecommendIdiom() {
        return recommendIdiom;
    }
    public void setRecommendIdiom(String recommendIdiom) {
        this.recommendIdiom = recommendIdiom;
    }

    public int getStartLine() {
        return startLine;
    }

    public void setStartLine(int startLine) {
        this.startLine = startLine;
    }

    public int getEndLine() {
        return endLine;
    }

    public void setEndLine(int endLine) {
        this.endLine = endLine;
    }

    public HunkResult(
            int chunknum,
            String fileName,
            int start,
            int end,
            boolean idiom,
            String recommend
            ) {
        this.hunkNum = chunknum;
        this.fileName = fileName;
        this.startLine = start;
        this.endLine = end;
        this.idiomatic = idiom;
        this.recommendIdiom = recommend;
    }

    @Override
    public int getHunkNum() {
        return this.hunkNum;
    }

    @Override
    public void setHunkNum(int hunkNum) {
        this.hunkNum = hunkNum;
    }

    @Override
    public String getFileName() {
        return this.fileName;
    }

    @Override
    public void setFileName(String file) {
        this.fileName = file;
    }

    @Override
    public int getStartline() {
        return this.startLine;
    }

    @Override
    public void setStartline(int startline) {
        this.startLine = startline;
    }

    @Override
    public int getEndline() {
        return this.endLine;
    }

    @Override
    public void setEndline(int endline) {
        this.endLine = endline;
    }

    @Override
    public String getSource() {
        return this.source;
    }

    @Override
    public void setSource(String source) {
        this.source = source;
    }
}
