package eu.sbf.iot.hono;

public class HonoExampleApplication extends HonoExampleApplicationBase {

    public static void main(final String[] args) throws Exception {

        System.out.println("Starting consumer...");
        final HonoExampleApplication honoExampleApplication = new HonoExampleApplication();
        honoExampleApplication.consumeData();
        System.out.println("Finishing consumer.");
    }
}
