package com.siamesex.standalone.model;

import java.util.List;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;

public class Branch {

    private String branchID;
    private User member;
    private List<Item> items;

    public String getBranchID() {
        return branchID;
    }

    public void setBranchID(String branchID) {
        this.branchID = branchID;
    }

    public User getMember() {
        return member;
    }

    public void setMember(User member) {
        this.member = member;
    }

    public Branch(String branchID, User member, List<Item> items) {
        this.branchID = branchID;
        this.member = member;
        this.items = items;
    }

    public List<Item> getItems() {
        return items;
    }

    public void setItems(List<Item> items) {
        this.items = items;
    }
}
