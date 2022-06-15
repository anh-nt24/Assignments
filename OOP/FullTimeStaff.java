class FullTimeStaff extends Staff{
    protected int baseSalary;
    protected double bonusRate;

    public FullTimeStaff(String sID, String sName, int baseSalary, double bonusRate) {
        super(sID, sName);
        setBaseSalary(baseSalary);
        setBonusRate(bonusRate);
    }

    public int getBaseSalary() {
        return this.baseSalary;
    }

    public void setBaseSalary(int baseSalary) {
        this.baseSalary = baseSalary;
    }

    public double getBonusRate() {
        return this.bonusRate;
    }

    public void setBonusRate(double bonusRate) {
        this.bonusRate = bonusRate;
    }

    public double paySalary(int workedDays) {
    	if (workedDays <= 21)
    		return getBaseSalary()*getBonusRate();
        return getBaseSalary()*getBonusRate() + (workedDays-21)*100000;
    }

    public String toString() {
        String num = String.valueOf(getBonusRate());
        return String.format("%s_%s_%s_%d", getsID(), getsName(), num, getBaseSalary());
    }
}
