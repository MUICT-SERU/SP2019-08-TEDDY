package crest.siamese.githubUtils;

public interface Hunk {


    public int getHunkNum();
    public void setHunkNum(int hunkNum);

    public String getFileName();
    public void setFileName(String file);

    public int getStartline();
    public void setStartline(int startline);

    public int getEndline();
    public void setEndline(int endline);

    public String getSource();
    public void setSource(String source);

}
