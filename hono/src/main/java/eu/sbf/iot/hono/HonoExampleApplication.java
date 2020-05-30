/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package eu.sbf.iot.hono;

/**
 *
 * @author Dominik
 */
public class HonoExampleApplication extends HonoExampleApplicationBase {
    public static void main(final String[] args) throws Exception {

        System.out.println("Starting consumer...");
        final HonoExampleApplication honoExampleApplication = new HonoExampleApplication();
        honoExampleApplication.consumeData();
        System.out.println("Finishing consumer.");
    }
}
