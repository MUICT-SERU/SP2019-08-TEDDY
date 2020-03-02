package com.siamesex.standalone.model;

import java.util.List;

public class ChunkQuery implements Chunk {

    private int chunknum, startline, endline;
    private String filename;
    private List<String> edit;

    public ChunkQuery(int chunknum, int startline, int endline, String filename, List<String> edit) {
        this.chunknum = chunknum;
        this.startline = startline;
        this.endline = endline;
        this.filename = filename;
        this.edit = edit;
    }

    @Override
    public int getChunkNum() {
        return this.chunknum;
    }
    @Override
    public void setHunkNum(int chunknum) {
        this.chunknum = chunknum;
    }

    @Override
    public String getFileName() {
        return this.filename;
    }
    @Override
    public void setFileName(String filename) {
        this.filename = filename;
    }

    @Override
    public int getStartline() {
        return this.startline;
    }
    @Override
    public void setStartline(int startline) {
        this.startline = startline;
    }

    @Override
    public int getEndline() {
        return this.endline;
    }
    @Override
    public void setEndline(int endline) {
        this.endline = endline;
    }

    public List<String> getEdit() {
        return edit;
    }

    public void setEdit(List<String> edit) {
        this.edit = edit;
    }

    public String getEditString(){
        StringBuilder builder = new StringBuilder();
        builder.append("");

        for(String edit : this.edit) {
            builder.append(edit).append("\n");
        }

        return builder.toString();
    }
}
