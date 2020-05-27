package eu.sbf.iot.dineros.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import eu.sbf.iot.dineros.model.SensorReading;
import eu.sbf.iot.dineros.repository.SensorRepo;
import java.util.Comparator;
import java.util.List;

@Controller
public class HomeController {

	@Autowired
	private SensorRepo repo;
	
	@GetMapping("/")
	public String home(Model model) {
//		List<SensorReading> readings = repo.findByDeviceId("636ea23e-45db-4106-b1c7-bdeb14f6861c");
		List<SensorReading> readings = repo.findByLocationAndParameter("Mljet","Temperature");
		readings.sort(Comparator.comparing(SensorReading::getTimestamp).reversed());
		model.addAttribute("readings", readings);
		return "home";
	}
	
}
