package eu.sbf.iot.hono;


/**
 * Class defines where to reach the AMQP network that needs to be accessed for consuming data.
 * This is intentionally done as pure Java constants to provide an example with minimal dependencies (no Spring is
 * used e.g.).
 *
 * Please adopt the values to your needs - the defaults serve for a typical docker swarm setup.
 */
public class HonoExampleConstants {
    /**
     * The default host name to assume for interacting with Hono.
     */
    public static final String HONO_CONTAINER_HOST = "hono.eclipseprojects.io";
    /**
     * The name or IP address of the host to connect to for consuming messages.
     */
    public static final String HONO_AMQP_CONSUMER_HOST = System.getProperty("consumer.host", HONO_CONTAINER_HOST);
    /**
     * Port of the AMQP network where consumers can receive data (in the standard setup this is the port of the qdrouter).
     */
    public static final int HONO_AMQP_CONSUMER_PORT = Integer.parseInt(System.getProperty("consumer.port", "15672"));

    public static final String TENANT_ID = "4082acd7-4e7e-4c3d-b2b5-d9e8e056a147";

    /**
     * For devices signalling that they remain connected for an indeterminate amount of time, a command is periodically sent to the device after the following number of seconds elapsed.
     */
    public static final int COMMAND_INTERVAL_FOR_DEVICES_CONNECTED_WITH_UNLIMITED_EXPIRY = Integer.parseInt(System.getProperty("command.repetition.interval", "5"));

    private HonoExampleConstants() {
        // prevent instantiation
    }
}
