package crest.siamese.test;
import crest.siamese.Siamese;
import org.junit.Test;

public class SiameseTest {
//    TODO: check why this doesn't work

    @Test
    public void testDelete() {
        Siamese siamese = new Siamese("config_test.properties");
        siamese.startup();

        try {
            siamese.execute();
        } catch (Exception e) {
            e.printStackTrace();
        }

        siamese.shutdown();
    }
}
