class SeasonalStaff extends Staff {
    private int hourlyWage;

    public SeasonalStaff(String sID, String sName, int hourlyWage) {
        super(sID, sName);
        setHourlyWage(hourlyWage);
    }

    public int getHourlyWage() {
        return this.hourlyWage;
    }

    public void setHourlyWage(int hourlyWage) {
        this.hourlyWage = hourlyWage;
    }

    public double paySalary(int workedHours) {
        return getHourlyWage()*workedHours;
    }
    
    public String toString() {
        return String.format("%s_%s_%d", getsID(), getsName(), getHourlyWage());
    }
}