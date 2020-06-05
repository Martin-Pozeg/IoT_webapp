package eu.sbf.iot.dineros.repository;
import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.repository.MongoRepository;

import eu.sbf.iot.dineros.model.SensorReading;
public interface SensorRepo extends MongoRepository<SensorReading, String>{

	public List<SensorReading> findByDeviceId(String deviceId);
	public List<SensorReading> findByLocation(String location);
	public List<SensorReading> findByLocationAndParameter(String location, String parameter);
	
	public Page<SensorReading> findByLocationAndParameter(String location, String parameter, Pageable pageable);
	public List<SensorReading> findTop10ByLocationAndParameterOrderByTimestampDesc(String location, String parameter);
		
}
