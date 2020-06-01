package eu.sbf.iot.dineros.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;

import com.mongodb.BasicDBObject;

import eu.sbf.iot.dineros.model.SensorReading;
import eu.sbf.iot.dineros.repository.SensorRepo;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.text.Format;
import java.text.SimpleDateFormat;
import java.time.format.DateTimeFormatter;

@Controller
public class HomeController {

	@Autowired
	private SensorRepo repo;
	
	@Autowired
	private MongoTemplate mongo;
	
	@GetMapping("/")
	public String home(Model model) {
		Query query = new Query();
		query.fields().include("location");
		model.addAttribute("locations", mongo.findDistinct(query, "location", "sensorReading", SensorReading.class, String.class));
		query = new Query();
		query.fields().include("parameter");
		model.addAttribute("parameters", mongo.findDistinct(query, "parameter", "sensorReading", SensorReading.class, String.class));
		List<SensorReading> readings = repo.findByLocationAndParameter("Mljet","Temperature");
		readings.sort(Comparator.comparing(SensorReading::getTimestamp).reversed());
		model.addAttribute("readings", readings);
		return "home";
	}
	
	@GetMapping("/chartData/{location}/{parameter}")
	@ResponseBody
	public List<Object> data(@PathVariable String location, @PathVariable String parameter, Model model){
		List<SensorReading> temperatures = repo.findByLocationAndParameter(location, parameter);
		Format formatter = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssZ");
		return temperatures.stream().map(t -> new Object[] {formatter.format(t.getTimestamp()), t.getValue()}).collect(Collectors.toList());
	}
	
		
}
