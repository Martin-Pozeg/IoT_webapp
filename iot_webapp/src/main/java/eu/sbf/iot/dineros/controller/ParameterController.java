package eu.sbf.iot.dineros.controller;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.data.domain.Sort.Direction;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import eu.sbf.iot.dineros.repository.SensorRepo;

@Controller
public class ParameterController {
	
	@Autowired
	private SensorRepo repo;

	@GetMapping("/sensor/{location}/{parameter}")
	public String getValuesByLocationAndParameter(@PathVariable String location, @PathVariable String parameter, @RequestParam("page") Optional<Integer> page, @RequestParam("size") Optional<Integer> size, Model model) {
		model.addAttribute("location", location);
		model.addAttribute("parameter", parameter);
		int currentPage = page.orElse(1);
        int pageSize = size.orElse(15);
		model.addAttribute("readings", repo.findByLocationAndParameter(location, parameter, PageRequest.of(currentPage-1, pageSize)));
		return "paramTemplate";
	}
	
	
		
	@GetMapping("/sensor/table/{location}/{parameter}")
	public String getTableValuesByLocationAndParameter(@PathVariable String location, @PathVariable String parameter, @RequestParam("page") Optional<Integer> page, @RequestParam("size") Optional<Integer> size, Model model) {
		model.addAttribute("location", location);
		model.addAttribute("parameter", parameter);
		int currentPage = page.orElse(1);
        int pageSize = size.orElse(15);
        model.addAttribute("readings", repo.findTop10ByLocationAndParameterOrderByTimestampDesc(location, parameter));
//		model.addAttribute("readings", repo.findByLocationAndParameter(location, parameter, PageRequest.of(currentPage-1, pageSize)));
		model.addAttribute("param",parameter);
		return "tableFragment :: records";
	}
	
	@GetMapping("/setLocation/{location}/{parameter}")
	public String setLocationFragment(@PathVariable String location, @PathVariable String parameter,Model model) {
		model.addAttribute("location", location);
		model.addAttribute("parameter", parameter);
		return "linkFragment :: link";
	}
	
}
