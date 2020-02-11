package com.siamesex.standalone.model;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import org.json.simple.JSONObject;

import java.util.List;

public class Commit {

    private String commitID;
    private List<HunkQuery> hunkList;

    @JsonCreator
    public Commit(@JsonProperty("commitID") String commitID, @JsonProperty("hunkList") List<HunkQuery> hunkList) {
        this.commitID = commitID;
        this.hunkList = hunkList;
    }

    public String getId() {

        return this.commitID;
    }

    public void setId(String id) {
        this.commitID = id;
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


}
