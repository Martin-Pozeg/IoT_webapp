package eu.sbf.iot.dineros.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import eu.sbf.iot.dineros.model.SensorReading;
import eu.sbf.iot.dineros.repository.SensorRepo;

@Controller
public class DataController {
	
	@Autowired
	private SensorRepo repo;
	private static final Logger LOG = LoggerFactory.getLogger(DataController.class);
	
	
	@PostMapping("/data")
	public ResponseEntity<?> ingestData(@RequestParam(name = "id" ) String deviceId, @RequestParam(name = "l" ) String location, @RequestParam(name = "p" ) String parameter, @RequestParam(name = "v" ) Double value) {
		SensorReading s = new SensorReading(deviceId, location, parameter, value);
		System.out.println("Entity saved to database: " + repo.save(s));
		return ResponseEntity.status(HttpStatus.OK).build();
	}

}
