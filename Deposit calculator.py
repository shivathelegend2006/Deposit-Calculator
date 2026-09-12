
def convert(ma):
    if ma >= 10**7:
        return f"{round(ma/1e7,2)} Crores"
    elif ma >= 10**5:
        return f"{round(ma/1e5,2)} Lakhs"
    elif ma >= 1000:
         return f"{round(ma/1e3,2)} Thousand"    
    else:
        return float(ma)
    
def check_for_num(value):
    
    while True:
        check = input(value)
        if check.isdigit():
             return float(check)
        else :
            print("Please enter only numbers")
           
def rd():
    p = check_for_num("Enter the monthly deposited amount (without any commas): ")
    r = check_for_num("Enter the annual rate of interest (example enter 6 if the interest is 6%): ")
    y = check_for_num("Enter the total number of years for the reccuring payments: ")
    n = y*12
    
    rdr = round((p*((n*(n+1))/2)*(r/400))+(p*n))
    tot = round(p*n)
    ma = convert(rdr)
    pro = round(rdr-tot)
    print(f"your total investment is {tot} with an annual interest of {r} fpr a total of {n} months ")
    print(f"the maturity amount is {ma} with a total profit of {pro}")
    

def fd():
    fdp = float(check_for_num("Enter the principle amount (without any commas): "))
    fdr = float(check_for_num("Enter the rate of interest (example enter 6 if the interest is 6%): "))
    fdf = round((1+(fdr/100))*fdp)
    ma = convert(fdf)
    pro = round(fdf-fdp) 

    print(f"Your initial investment is {fdp}, with an interest of {fdr}%")
    print(f"the maturity amount is {ma} with a profit of {pro}")

def cd():
    fdp = float(check_for_num("Enter the principle amount (without any commas): "))
    fdr = float(check_for_num("Enter the rate of interest (example enter 6 if the interest is 6%): "))
    n = float(check_for_num("Enter the number of Years to continue the FD: "))
    rr = fdr/100
    cdc = round(fdp*((1+rr)**n))
    ma = convert(cdc)
    pro = round(cdc- fdp)
    print(f"If you invest {fdp} and leave it to grow for {n} years....\n The maturity amount is {ma}")
    

def sip():
    p = check_for_num("Enter your monthly SIP installment without commas: ")
    rr = check_for_num("Enter the annual rate of interest (example enter 6 if the interest is 6%): ")
    y = check_for_num("Enter the total number of years for the monthly payments: ")
    n = y*12
    r = float((rr/100)/12)
    sip = round(p*((((1+r)**n)-1)/r)*(1+r))
    if sip >= 10**7:
        ma = f"{round(sip/1e7,2)} Crores"
        
    elif sip >= 10**5:
        ma =f"{round(sip/1e5,2)} Lakhs"
    elif sip >= 1000:
        ma =f"{round(sip/1e3,2)} Thousand"
    tot = round(p*n)
    pro = round(sip-tot)
    print(f"your total investment is {tot} with a annaul interest of {rr} for a total of {n} months ")
    print(f"the maturity amount is {ma} with a total profit of {pro}")
    

def sipmm():
    def mat(p,rr,target):
            
        r = float((rr/100)/12)
        n = 1
        while True:
            a = round(p*((((1+r)**n)-1)/r)*(1+r))
            if a >= target:
             return n
            n +=1

    p =  check_for_num("Enter your monthly SIP installment without commas: ")
    rr = check_for_num("Enter the annual rate of interest (example enter 6 if the interest is 6%): ") 
    target = check_for_num("Enter the final Maturity Amount: ")

    months = mat(p,rr,target)
    years = months//12
    extra = months%12

    print(f"For a Maturity Amount of {round(target)} with monthly investment of {round(p)}\n"
          f"you need to invest for {months} months\nwhich is {years} years and {extra} months with an interest of {rr}%")

def prince():
    a = check_for_num("Enter your target Maturity Amount without commas: ")
    rr = check_for_num("Enter the annual rate of interest (example enter 6 if the interest is 6%): ")
    y = check_for_num("Enter the total number of years for the monthly payments: ")
    n = y*12
    r = float((rr/100)/12)
    tar = round(a/((((1+r)**n)-1)/r)*(1+r))
    ma = convert(tar)
    yer = convert(tar*12) 
    print(f"For a maturity amount of {a} in a span of {y} years\nwith an interest of {rr}%\nYou need to invest {ma} monthly\nwhich is {yer} yearly ")

def tf():
    p = check_for_num("Enter the one time FD amount: ")
    r = check_for_num("Enter the annual rate of interest (example enter 6 if the interest is 6%): ")
    rr = r/100
    t = check_for_num("Enter the targeted maturity amount without commas: ")
    n = 1
    while True:
        a = p*((1+rr)**n)
        if a >= t:
            break
        n += 1

    print(f"""For a maturity amount of {t}
with a one time investment of {p} and yearly interest rate of {r}%
You will have to hold the fd for {n} years""")


def fd_cats():
    print("""For continuous FD over a number of years(COMPOUNDING) type 'N'
For finding how long to hold an FD for a target maturity amount type 'T'
For One time FD returns type  'F'""")
    while True:
        print("Kindly enter only from options given")
        re = input("")
        if re.lower() in ["n","f","t"]:

            if re.lower() =="n":
                cd()
            elif re.lower() =="f":
                fd()
            elif re.lower() =="t":
                tf()
            break
        
            
def pri(): 
    print("For Fixed Deposits(FD) returns type 'FD'\n" \
    "For Reccuring Deopsit(RD) returns type'RD'\n" \
    "For Systenatic Investment Plan(SIP) returns type 'SIP'\n" \
    "For finding how long to invest for a specific target amount through SIP type 'T'\n" \
    "For finding how much to invest per month for a targeted maturity amount through SIP type 'P'")
    while True:
        print("Kindly enter only from the options given ")
        ch = input("")
        if ch.lower() in ["fd","rd","sip","t","p"]:
             if ch.lower() =="fd":
                fd_cats()
             elif ch.lower()=="rd":
                rd()
             elif ch.lower()=="sip":
                sip()
             elif ch.lower()=="t":
                sipmm()
             elif ch.lower()=="p":
                prince()
             break

   
         
while True:
    pri()
    rep = input("Would you like to find the return of anything else?? (y/n) ")
    if rep.lower() !="y":
     print("Have a nice day")
     break 

    