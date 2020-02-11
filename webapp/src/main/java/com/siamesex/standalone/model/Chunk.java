package com.siamesex.standalone.model;

import java.util.List;

public interface Chunk {


    public int getChunkNum();
    public void setHunkNum(int chunknum);

    public String getFileName();
    public void setFileName(String filename);

    public int getStartline();
    public void setStartline(int startline);

    public int getEndline();
    public void setEndline(int endline);

    public List<String> getEdit();
    public void setEdit(List<String> source);

}
