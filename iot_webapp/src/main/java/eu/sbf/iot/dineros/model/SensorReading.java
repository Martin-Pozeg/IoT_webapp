package eu.sbf.iot.dineros.model;

import java.util.Date;

import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.Id;
import org.springframework.format.annotation.DateTimeFormat;

public class SensorReading {
	
	@Id
	private String id;
	private String deviceId;
	private String location;
	private String parameter;
	private Double value;
	
	@DateTimeFormat(iso = DateTimeFormat.ISO.DATE_TIME)
	public Date timestamp = new Date();
	
	public SensorReading() {}

	public SensorReading(String deviceId, String location, String parameter, Double value) {
		this.deviceId = deviceId;
		this.location = location;
		this.parameter = parameter;
		this.value = value;
	}

	

	public String getDeviceId() {
		return deviceId;
	}

	public void setDeviceId(String deviceId) {
		this.deviceId = deviceId;
	}

	public String getLocation() {
		return location;
	}

	public void setLocation(String location) {
		this.location = location;
	}

	public String getParameter() {
		return parameter;
	}

	public void setParameter(String parameter) {
		this.parameter = parameter;
	}

	public Double getValue() {
		return value;
	}

	public void setValue(Double value) {
		this.value = value;
	}

	public String getId() {
		return id;
	}

	public Date getTimestamp() {
		return timestamp;
	}

	@Override
	public String toString() {
		return "SensorReading [id=" + id + ", deviceId=" + deviceId + ", location=" + location + ", parameter="
				+ parameter + ", value=" + value + ", timestamp=" + timestamp + "]";
	}
	
	
	
	
	
}
