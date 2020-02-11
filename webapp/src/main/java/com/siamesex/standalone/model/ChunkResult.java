package com.siamesex.standalone.model;

import java.util.List;

public class ChunkResult implements Chunk {

    private int chunknum, startline, endline;
    private String filename;
    private List<String> edit;
    private boolean idiomatic = false;
    private String recommendIdiom = "Null";

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
        return startline;
    }

    public void setStartLine(int startLine) {
        this.startline = startLine;
    }

    public int getEndLine() {
        return endline;
    }

    public void setEndLine(int endLine) {
        this.endline = endLine;
    }

    public ChunkResult(
            int chunknum,
            int start,
            int end,
            String fileName,
            List<String> edit,
            boolean idiom,
            String recommend
            ) {
        this.chunknum = chunknum;
        this.filename = fileName;
        this.startline = start;
        this.endline = end;
        this.edit = edit;
        this.idiomatic = idiom;
        this.recommendIdiom = recommend;
    }

    public ChunkResult(
            int chunknum,
            int start,
            int end,
            String fileName,
            boolean idiom,
            String recommend
    ) {
        this.chunknum = chunknum;
        this.filename = fileName;
        this.startline = start;
        this.endline = end;
        this.edit = null;
        this.idiomatic = idiom;
        this.recommendIdiom = recommend;
    }

    @Override
    public int getChunkNum() {
        return this.chunknum;
    }

    @Override
    public void setHunkNum(int hunkNum) {
        this.chunknum = hunkNum;
    }

    @Override
    public String getFileName() {
        return this.filename;
    }

    @Override
    public void setFileName(String file) {
        this.filename = file;
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

    @Override
    public List<String> getEdit() {
        return edit;
    }

    public String getEditString(){
        StringBuilder builder = new StringBuilder();
        builder.append("");

        for(String edit : this.edit) {
            builder.append(edit).append("\n");
        }

        return builder.toString();
    }

    @Override
    public void setEdit(List<String> edit) {
        this.edit = edit;
    }
}
