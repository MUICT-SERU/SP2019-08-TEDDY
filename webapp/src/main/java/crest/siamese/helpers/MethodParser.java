package src.main.java.crest.siamese.helpers;

import src.main.java.crest.siamese.document.Method;

import java.util.ArrayList;

public interface MethodParser {
    public String getLicense();
    public ArrayList<Method> parseMethods();
    public void configure(String filePath, String prefixToRemove, String mode, boolean isPrint);
}
