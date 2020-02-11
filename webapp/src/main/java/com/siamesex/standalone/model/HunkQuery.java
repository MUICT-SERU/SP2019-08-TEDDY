package com.siamesex.standalone.model;

public class HunkQuery implements Hunk {

    private int hunkNum, startLine, endLine;
    private String source, fileName;

    public HunkQuery(int hunkNum, String fileName, int startLine, int endLine, String source) {
        this.hunkNum = hunkNum;
        this.fileName = fileName;
        this.startLine = startLine;
        this.endLine = endLine;
        this.source = source;
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
