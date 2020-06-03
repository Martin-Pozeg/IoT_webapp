package eu.sbf.iot.dineros.model;

public enum ParameterEnum {
	
	NephelometricTutrbidity("Nephelometric Tutrbidity [NTU]"),
	OxygenSaturation("Oxygen Saturation [%]"),
	OxygenMgL("Oxygen [mg/L]"),
	OxygenPpm("Oxygen [ppm]"),
	pH("Acidity [pH]"),
	RedoxORP("Redox (ORP) [mV]"),
	Conductivity("Conductivity [µS/cm]"),
	Salinity("Salinity [g/kg]"),
	TDSKcl("Total dissolved solids-Kcl [ppm]"),
	SS("Suspended Solids [mg/L]"),
	ConductivityNCWT("Conductivity (NCWT) [mS/cm]"),
	CDOMfDOM("CDOM / fDOM [ppb]"),
	Temperature("Temperature [°C]");
	
	public final String param;
	
	private ParameterEnum(String param) {
		this.param = param;
	}
	

}
