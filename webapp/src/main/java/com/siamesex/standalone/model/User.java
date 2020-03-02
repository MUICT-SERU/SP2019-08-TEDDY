package com.siamesex.standalone.model;

public class User {

    String username;
    String password;

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }
}
