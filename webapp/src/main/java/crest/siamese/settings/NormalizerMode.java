package src.main.java.crest.siamese.settings;

public interface NormalizerMode {
    void configure(char[] normOptions);
    void reset();
}
