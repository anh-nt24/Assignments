public class Manager extends FullTimeStaff{
    private int allowance;

    public Manager(String sID, String sName, int baseSalary, double bonusRate, int allowance) {
        super(sID, sName, baseSalary, bonusRate);
        setAllowance(allowance);
    }

    public int getAllowance() {
        return this.allowance;
    }

    public void setAllowance(int allowance) {
        this.allowance = allowance;
    }

    public double paySalary(int workedDays) {
        return super.paySalary(workedDays) + getAllowance();
    }

    public String toString() {
        String num = String.valueOf(getBonusRate());
        return String.format("%s_%s_%s_%d_%d", getsID(), getsName(), num, getBaseSalary(), getAllowance());
    }
}
