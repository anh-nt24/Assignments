#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Employee
{
    char eID[100];
    char firstName[100];
    char lastName[100];
    char gender[100];
    char date[100];
    char department[100];
    char country[100];
};
struct Employee employees[10000];


struct Progress
{
    char employee[100];
    char proj_ID[100];
    char prog[100];
};
struct Progress progress[10000];

int check(char[]);
int size(char[]);  // to get the size of a FILE passed in
float IsFloat(char[]);
int IsInt(char[]);

void _project();  
void _progress();
void _employee();

void lower(char st[])
{
    int i, n=strlen(st);
    for (i=0;i<n;i++)
        if (st[i]>=65 && st[i]<=90)
            st[i]=st[i]+32;
}

void delete_duplicate(struct Progress a[], int *n, int vt)
{
    int i;
	*n=*n-1;
	for (i=vt;i<*n;i++)  
	{
		strcpy(a[i].employee,a[i+1].employee);
	}
}

void error()
{
    FILE *fw;
    fw = fopen("check.txt","w");
    fprintf(fw,"wrong syntax");
    fclose(fw);
}

void count(struct Employee emp[], char parameter[])
{
    FILE *fw;
    fw = fopen("result.csv","w");
    _employee();
    int i,d=0,n=size("Employee.csv");
    for (i=0;i<n;i++)
        if (strcmp(emp[i].department, parameter) == 0)
            d++;
    fprintf(fw,"%d",d);
    fclose(fw);
}

void list(struct Employee emp[], char parameter[])
{
    FILE *fw;
    fw = fopen("result.csv","w");
    _employee();
    int i,n=size("Employee.csv");
    for (i=0;i<n;i++)
    {
        if (strcmp(emp[i].gender, parameter) == 0) 
        {
            fprintf(fw,"%s,",emp[i].eID);
            fprintf(fw,"%s,",emp[i].firstName);
            fprintf(fw,"%s,",emp[i].lastName);
            fprintf(fw,"%s,",emp[i].gender);
            fprintf(fw,"%s,",emp[i].date);
            fprintf(fw,"%s,",emp[i].department);
            fprintf(fw,"%s\n",emp[i].country);
        }
    }
    fclose(fw);
}

void report(struct Progress progress[], char parameter[])
{
    struct Progress a[100];
    FILE *fw = fopen("result.csv","w");
    int i=0,j=0,n;
    char line[1000], *cut;
    FILE *fr;
    fr = fopen("Progress.csv","r");
    while (fgets(line,1000,fr) != NULL)
    {
        cut = strtok(line,",");
        strcpy(progress[i].employee,cut);
        cut = strtok(NULL,",");
        strcpy(progress[i].proj_ID,cut);
        cut = strtok(NULL,",");
        if (cut[strlen(cut)-1] == '\n')
            cut[strlen(cut)-2]='\0';
        strcpy(progress[i].prog, cut);
        if (strcmp(progress[i].prog, parameter)==0)
        {
            //fprintf(fw,"%s\n",progress[i].employee);
            strcpy(a[j].employee, progress[i].employee);
            j++;
        }
        i++;
    }
    n=j;
    for (i=0;i<n-1;i++)
        for (j=i+1;j<n;j++)
            if (strcmp(a[i].employee, a[j].employee) == 0)
                delete_duplicate(a,&n,j);
    for (i=0;i<n;i++)
        fprintf(fw,"%s\n",a[i].employee);
    fclose(fw);
    fclose(fr);
}

void average(struct Progress progress[], char parameter[])
{
    FILE *fw;
    fw = fopen("result.csv","w");
    _progress();
    int i,d=0,n=size("Progress.csv");
    float r,s=0;
    for (i=0;i<n;i++)
        if (strcmp(progress[i].proj_ID, parameter)==0)
        {
            d++;
            r=atof(progress[i].prog);
            s=s+r;
        }
    if (d==0)
        fprintf(fw,"0");
    else
        fprintf(fw,"%0.3f",s/d);
    fclose(fw);
}

void sort(struct Employee emp[], char parameter[])
{
    _employee();
    FILE *fw;
    fw = fopen("result.csv","w");
    int i, j, n=size("Employee.csv"), m;
    struct Employee t;
    for (i=0;i<n-1;i++)
    {
        m=i;
        if (strcmp(parameter,"Asc")==0)
            for (j=i+1;j<n;j++)
                if (strcmp(emp[j].lastName, emp[m].lastName)<0 || (strcmp(emp[j].lastName, emp[m].lastName)==0 && strcmp(emp[j].firstName, emp[m].firstName)<0))
                    m=j;    
        if (strcmp(parameter,"Desc")==0)
            for (j=i+1;j<n;j++)
                if (strcmp(emp[j].lastName, emp[m].lastName)>0 || (strcmp(emp[j].lastName, emp[m].lastName)==0 && strcmp(emp[j].firstName, emp[m].firstName)<0))
                    m=j;
        
        t = emp[i];
        emp[i] = emp[m];
        emp[m] = t;
    }
    for (i=0;i<n;i++)
    {
        fprintf(fw,"%s,",emp[i].eID);
        fprintf(fw,"%s,",emp[i].firstName);
        fprintf(fw,"%s,",emp[i].lastName);
        fprintf(fw,"%s,",emp[i].gender);
        fprintf(fw,"%s,",emp[i].date);
        fprintf(fw,"%s,",emp[i].department);
        fprintf(fw,"%s\n",emp[i].country); 
    }
    fclose(fw);
}

void country(struct Employee emp[], char parameter[])
{
    FILE *fw;
    fw = fopen("result.csv","w");
    FILE *fr;
    fr = fopen("Employee.csv","r");
    char s0[100];
    int i=0;
    char line[1000], *cut;
    while (fgets(line,1000,fr) != NULL)
    {
        strcpy(s0,line);
        cut = strtok(line,",");
        strcpy(employees[i].eID,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].firstName,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].lastName,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].gender,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].date, cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].department, cut);
        cut = strtok(NULL,",");
        if (cut[strlen(cut)-1] == '\n')
            cut[strlen(cut)-2]='\0';
        strcpy(employees[i].country,cut);
        if (strcmp(employees[i].country, parameter) == 0)
        {
            fprintf(fw,"%s,",emp[i].eID);
            fprintf(fw,"%s,",emp[i].firstName);
            fprintf(fw,"%s,",emp[i].lastName);
            fprintf(fw,"%s,",emp[i].gender);
            fprintf(fw,"%s,",emp[i].date);
            fprintf(fw,"%s,",emp[i].department);
            fprintf(fw,"%s\n",emp[i].country);
        }
        i++;
    }
    fclose(fw);
    fclose(fr);
}

//////////////////////////////////////////////////////////////////////////////////
//==================================== MAIN ====================================//
//////////////////////////////////////////////////////////////////////////////////
int main()
{
    char st[30],s[30];
    int i,n;
    float r;
    char *selection, *parameter;
    fgets(st,30,stdin);
    if (st[strlen(st)-1] == 10 || st[strlen(st)-1] == 13)
        st[strlen(st)-1]='\0';
    if (st[strlen(st)-1] == 13 || st[strlen(st)-1] == 10)
        st[strlen(st)-1]='\0';
    strcpy(s,st);
    if (check(s)==0)
        error();
    else
    {
        // in case all parameters are correct
        selection = strtok(st," ");
        parameter = strtok(NULL," ");
        lower(selection);
        if (parameter[0]>=97 && parameter[0]<=122 && strcmp(selection,"country") != 0)
            parameter[0]=parameter[0]-32;
        if (strcmp(selection,"count")==0)
        {
            if (parameter[0]=='-')
                error();
            else
                count(employees, parameter);
        }
        else if (strcmp(selection,"list")==0 && (strcmp(parameter,"Male")==0) || (strcmp(parameter,"Female")==0))
        {
            list(employees, parameter);
        }
        else if (strcmp(selection,"report")==0)
        {
            r = IsFloat(parameter);
            if (r<0 || r>1 || (strcmp(parameter,"0") != 0 && r==0))
                error();
            else
                report(progress, parameter);
        }
        else if (strcmp(selection,"average")==0)
        {
            if (parameter[0]=='-')
                error();
            else
            {
                n = IsInt(parameter);
                if (n==0 && strcmp(parameter,"0") != 0) 
                    error();
                else 
                    average(progress,parameter);
            }
        }
        else if (strcmp(selection,"sort")==0 && ((strcmp(parameter,"Asc")==0) || (strcmp(parameter,"Desc")==0)))
        {
            sort(employees, parameter);
        }
        else if (strcmp(selection,"country")==0)
        {
            country(employees, parameter);
        }
        else                                                                    // WRONG COMMAND //
        {
            error();
        }
    } 
    return 0;
}
/////////////////////////////////////////////////////////////////////////////

float IsFloat(char st[])
{
    float r;
    int i;
    for (i=0;i<strlen(st);i++)
    {
        if (st[i]>=48 && st[i]<=57 || st[i]=='.')
            continue;
        else
            return 0;
    }
    r=atof(st);
    return r;
} 

int IsInt(char st[])
{
    int n,i;
    for (i=0;i<strlen(st);i++)
    {
        if (st[i]>=48 && st[i]<=57)
            continue;
        else
            return 0;
    }
    n=atoi(st);
    return n;
} 

int check(char st[])
{
    int i, kt=1,d=0, n=strlen(st);
    char s[30];
    char *selection;
    for (i=0;i<n;i++)
        if (st[i]==' ')                                     // MORE THAN 1 SPACE // 
            d++;
    if (d>1)
        return 0;
    strcpy(s,st);
    selection = strtok(st," ");
    if (strlen(s) == strlen(selection))                                     // NO PARAMETERS //
        kt=0;
    else if (s[strlen(s)-1] == ' ')                                 // END WITH A SPACE //
        kt=0;
    return kt;
}

int size(char file[])
{
    FILE *fr = fopen(file,"r");
    char st[1000];
    int n=0;
    fgets(st,1000,fr);
    while (fgets(st,1000,fr) != NULL)
        n++;
    return n;
}

void _progress()
{
    FILE *fr;
    fr = fopen("Progress.csv","r");
    char line[1000], *cut;
    int i=0;
    fgets(line,1000,fr);
    while (fgets(line,1000,fr) != NULL)
    {
        cut = strtok(line,",");
        strcpy(progress[i].employee,cut);
        cut = strtok(NULL,",");
        strcpy(progress[i].proj_ID,cut);
        cut = strtok(NULL,",");
        strcpy(progress[i].prog, cut);
        i++;
    }
    fclose(fr);
}

void _employee()
{
    int i=0;
    FILE *fr;
    fr = fopen("Employee.csv","r");
    char line[1000], *cut;
    fgets(line,1000,fr);
    while (fgets(line,1000,fr) != NULL)
    {
        cut = strtok(line,",");
        strcpy(employees[i].eID,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].firstName,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].lastName,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].gender,cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].date, cut);
        cut = strtok(NULL,",");
        strcpy(employees[i].department, cut);
        cut = strtok(NULL,"\n");
        strcpy(employees[i].country,cut);
        i++;
    }
    fclose(fr);
} 