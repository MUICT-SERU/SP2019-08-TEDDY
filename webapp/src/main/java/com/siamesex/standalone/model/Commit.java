package com.siamesex.standalone.model;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

public class Commit {

    private String commitID;
    private List<ChunkQuery> commitData;

    @JsonCreator
    public Commit(@JsonProperty("commitID") String commitID, @JsonProperty("commitData") List<ChunkQuery> commitData) {
        this.commitID = commitID;
        this.commitData = commitData;
    }

    public String getId() {

        return this.commitID;
    }

    public void setId(String id) {
        this.commitID = id;
    }

    public List<ChunkQuery> getCommitData() {
        return commitData;
    }

    public void setCommitData(List<ChunkQuery> commitData) {
        this.commitData = commitData;
    }

    public String toString() {
        StringBuilder chunksString = new StringBuilder();

        for (ChunkQuery h : commitData) {
            chunksString.append("\n\t\tchunknum: ").append(h.getChunkNum());
            chunksString.append("\n\t\tstartline: ").append(h.getStartline());
            chunksString.append("\n\t\tendline: ").append(h.getEndline());
            chunksString.append("\n\t\tfilename: ").append(h.getFileName());
            chunksString.append("\n\t\tedit: ");
            chunksString.append("\n\t\t\t").append(h.getEdit());
        }

        return chunksString.toString();
    }


}
