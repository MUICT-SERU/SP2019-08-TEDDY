package com.siamesex.standalone.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

public class PullRequest {

    private List<Commit> PRWhole;

    @JsonCreator
    public PullRequest(@JsonProperty("PRWhole") List<Commit> PRWhole) {
        this.PRWhole = PRWhole;
    }

    public List<Commit> getCommits() {
        return this.PRWhole;
    }

    public void setCommits(List<Commit> PRWhole) {
        this.PRWhole = PRWhole;
    }

    @Override
    public java.lang.String toString() {

        StringBuilder stringBuilder = new StringBuilder();

        stringBuilder.append("{ PRWhole: [");

        for(Commit commit : PRWhole) {
            stringBuilder.append("\n\tcommitID: ").append(commit.getId());
            stringBuilder.append("\n\tcommitData: [");
            stringBuilder.append(commit.toString());
            stringBuilder.append("\n\t]");
        }

        stringBuilder.append("\n ]\n}");

        return stringBuilder.toString();
    }


}
