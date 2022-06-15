import java.io.*;
import java.util.*;

public class StoreManagement {
    private ArrayList<Staff> staffs;
    private ArrayList<String> workingTime;
    private ArrayList<Invoice> invoices;
    private ArrayList<InvoiceDetails> invoiceDetails;
    private ArrayList<Drink> drinks;

    public StoreManagement(String staffPath, String workingTimePath, String invoicesPath, String detailsPath, String drinksPath) {
        this.staffs = loadStaffs(staffPath);
        this.workingTime = loadFile(workingTimePath);
        this.invoices = loadInvoices(invoicesPath);
        this.invoiceDetails = loadInvoicesDetails(detailsPath);
        this.drinks = loadDrinks(drinksPath);
    }

    public ArrayList<Staff> getStaffs() {
        return this.staffs;
    }

    public void setStaffs(ArrayList<Staff> staffs){
        this.staffs = staffs;
    }
    
    public ArrayList<Drink> loadDrinks(String filePath) {
        ArrayList<Drink> drinksResult = new ArrayList<Drink>();
        ArrayList<String> drinks = loadFile(filePath);

        for (String drink : drinks) {
            String[] information = drink.split(",");
            drinksResult.add(new Drink(information[0], Integer.parseInt(information[1])));
        }

        return drinksResult;
    }

    public ArrayList<Invoice> loadInvoices(String filePath) {
        ArrayList<Invoice> invoiceResult = new ArrayList<Invoice>();
        ArrayList<String> invoices = loadFile(filePath);

        for (String invoice : invoices) {
            String[] information = invoice.split(",");
            invoiceResult.add(new Invoice(information[0], information[1], information[2]));
        }

        return invoiceResult;
    }

    public ArrayList<InvoiceDetails> loadInvoicesDetails(String filePath) {
        ArrayList<InvoiceDetails> invoiceResult = new ArrayList<InvoiceDetails>();
        ArrayList<String> invoices = loadFile(filePath);

        for (String invoice : invoices) {
            String[] information = invoice.split(",");
            invoiceResult.add(new InvoiceDetails(information[0], information[1], Integer.parseInt(information[2])));
        }

        return invoiceResult;
    }

    // requirement 1
    public ArrayList<Staff> loadStaffs(String filePath) {
        //code here and modify the return value
		ArrayList<Staff> outputStaff = new ArrayList<Staff>();
		ArrayList<String> staffs = loadFile(filePath);
        for (String i: staffs) {
            String[] info = i.split(",");
            if (info.length == 3)
                outputStaff.add(new SeasonalStaff(info[0], info[1], Integer.parseInt(info[2])));
            else if (info.length == 4) 
                outputStaff.add(new FullTimeStaff(info[0], info[1], Integer.parseInt(info[2]), Double.parseDouble(info[3])));
            else
                outputStaff.add(new Manager(info[0], info[1], Integer.parseInt(info[2]), Double.parseDouble(info[3]), Integer.parseInt(info[4])));
        }
        return outputStaff;
    }

    private ArrayList<SeasonalStaff> sortBySalary(ArrayList<SeasonalStaff> s, int[] time) {
        for (int i=0; i<s.size()-1;++i) {
            int maxIndex = i;
            for (int j=i+1; j<s.size();++j)
                if (s.get(j).paySalary(time[j]) > s.get(maxIndex).paySalary(time[maxIndex]))
                    maxIndex = j;

            SeasonalStaff s_temp = s.get(i);
            s.set(i,s.get(maxIndex));
            s.set(maxIndex,s_temp);
            int t = time[i];
            time[i] = time[maxIndex];
            time[maxIndex] = t;
        } 
        while (s.size() > 5) {
            s.remove(s.size()-1);
        }
        return s;
    }

    private int getTimeWorking(String ID, ArrayList<String> workFile) {
        for (String i:workFile) {
            String[] s = i.split(",");
            if (s[0].equals(ID))
                return Integer.parseInt(s[1]);
        }
        return 0;
    }

    // requirement 2
    public ArrayList<SeasonalStaff> getTopFiveSeasonalStaffsHighSalary() {
        //code here and modify the return value
        ArrayList <SeasonalStaff> s = new ArrayList<SeasonalStaff>();
        int[] time = new int[this.staffs.size()];
        int i=0;
        for (Staff staff : this.staffs) {
            if (staff instanceof SeasonalStaff) {
                s.add((SeasonalStaff)staff);
                time[i++] = getTimeWorking(staff.getsID(), this.workingTime);
            }
        }
        return sortBySalary(s,time);
    }

    // requirement 3
    public ArrayList<FullTimeStaff> getFullTimeStaffsHaveSalaryGreaterThan(int lowerBound) {
        //code here and modify the return value
        ArrayList<FullTimeStaff> ftStaff = new ArrayList<FullTimeStaff>();
        int time = 0;
        int i=0;
        for (Staff staff: this.staffs) {
            if (staff instanceof FullTimeStaff) {
                time = getTimeWorking(staff.getsID(), this.workingTime);
                if (((FullTimeStaff)staff).paySalary(time) > lowerBound)
                    ftStaff.add((FullTimeStaff)staff);
            }
            else if (staff instanceof Manager) {
                time = getTimeWorking(staff.getsID(), this.workingTime);
                if (((Manager)staff).paySalary(time) > lowerBound)
                    ftStaff.add((Manager)staff);
            }
        }
        return ftStaff;
    }
    
    // requirement 4
    public double totalInQuarter(int quarter) {
        double total = 0;
        // code here
        for (InvoiceDetails i: this.invoiceDetails) {
            String nameOfDrinks = i.getDName();
            String drinkID = i.getInvoiceID();
            int timeAMonth = 0;
            for (Invoice in: this.invoices) {
                if (in.getInvoiceID().equals(drinkID)) {
                    int getMonth = Integer.parseInt(in.getDate().split("/")[1]);

                    switch (quarter) {
                        case 1:
                            if (getMonth == 1 || getMonth == 2 || getMonth == 3)
                                timeAMonth++;
                            break;
                        case 2:
                            if (getMonth == 4 || getMonth == 5 || getMonth == 6)
                                timeAMonth++;
                            break;
                        case 3:
                            if (getMonth == 7 || getMonth == 8 || getMonth == 9)
                                timeAMonth++;
                            break;
                        case 4:
                            if (getMonth == 10 || getMonth == 11 || getMonth == 12)
                                timeAMonth++;
                            break;
                        default:
                            timeAMonth = 0;
                            break;
                    }
                }
            }
            for (Drink d: this.drinks) {
                if (nameOfDrinks.equals(d.getdName())) {
                    total += i.getAmount()*d.getPrice()*timeAMonth;
                }
            }
        }
        return total;
    }

    // requirement 5
    public Staff getStaffHighestBillInMonth(int month) {
        Staff maxStaff = null;
        //code here
        ArrayList<Invoice> inv = new ArrayList<Invoice>();
        for (int i=0; i<this.invoices.size();++i) {
            int getMonth = Integer.parseInt(this.invoices.get(i).getDate().split("/")[1]);
            if (getMonth == month) {
                inv.add(this.invoices.get(i));
            }
        }
        double max = -1;
        String maxID = "";
        for (Invoice i: inv) {
            String getID = i.getStaffID();
            ArrayList<String> billID = new ArrayList<String>();
            for (int index=0;index<inv.size();++index) {
                if (inv.get(index).getStaffID().equals(getID)) {
                    billID.add(inv.get(index).getInvoiceID());
                }
            }
            if (billID.size() > 0) {
                if (max < getPrice(billID)) {
                    max = getPrice(billID);
                    maxID = getID;
                }
            }
        }
        for (Staff s: this.staffs) {
            if(s.sID.equals(maxID)) {
                if (s instanceof FullTimeStaff)
                    maxStaff = (FullTimeStaff)s;
                if (s instanceof SeasonalStaff)
                    maxStaff = (SeasonalStaff)s;
                if (s instanceof Manager)
                    maxStaff = (Manager)s;
            }
        }
        return maxStaff;
    }

    private double getPrice(ArrayList<String> billID) {
        double payment = 0;
        for (String bill : billID) {
            for (InvoiceDetails ind : this.invoiceDetails) {
                if (ind.getInvoiceID().equals(bill)) {
                    int price = 0;
                    for (Drink d : this.drinks) {
                        if (ind.getDName().equals(d.getdName())) {
                            price = d.getPrice();
                            break;
                        }
                    }
                    payment += price*ind.getAmount();
                } 
            }
        }
        return payment;
    }

    // load file as list
    public static ArrayList<String> loadFile(String filePath) {
        String data = "";
        ArrayList<String> list = new ArrayList<String>();

        try {
            FileReader reader = new FileReader(filePath);
            BufferedReader fReader = new BufferedReader(reader);

            while ((data = fReader.readLine()) != null) {
                list.add(data);
            }

            fReader.close();
            reader.close();

        } catch (Exception e) {
            System.out.println("Cannot load file");
        }
        return list;
    }

    public void displayStaffs() {
        for (Staff staff : this.staffs) {
            System.out.println(staff);
        }
    }

    public <E> boolean writeFile(String path, ArrayList<E> list) {
        try {
            FileWriter writer = new FileWriter(path);
            for (E tmp : list) {
                writer.write(tmp.toString());
                writer.write("\r\n");
            }

            writer.close();
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("Error.");
            return false;
        }

        return true;
    }

    public <E> boolean writeFile(String path, E object) {
        try {
            FileWriter writer = new FileWriter(path);

            writer.write(object.toString());
            writer.close();

            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("Error.");
            return false;
        }

        return true;
    }
}
