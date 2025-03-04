import pandas as pd;

bev={'Price':[200,150,250,200,100,150,350,400,120,230,450,350,100,120,130,140,150,160]}
df1=pd.DataFrame(bev,index=['Latte','Americano','Iced Coffee','Turkish Coffee','Espresso','Cappuccino','Black tea','Green tea','Normal masala tea','Herbal tea','Rooibos tea','Purple tea','Orange juice','Apple Juice','Mango Juice','Grape Juice','Pomegranate Juice','Guava Juice'])

snack={'Price':[100,150,200,230,340,340,500,500,600,400,1000,200,250,300,350,100,700,500]}
df2=pd.DataFrame(snack,index=['Potato Chips','Banana Chips','Sweet Potato','Beet Chips','Yuca Chips','Plantain Chips','Almonds','Walnuts','Cashew','Chia Seeds','Pistachios','Sunflower Seeds','Chocolate','Ice-Cream','Pastries','Cookies','Desserts','Smoothies'])

foodie={'Price':[230,500,300,700,100,100,250,350,279,230,450,340,350,120,400,400,250]}
df3=pd.DataFrame(foodie,index=['Idli-Dosa','Biryani','Curry-Rice','Tandoori-Chicken','Samosa-Kachori','Jalebi','Pasta(Spaghetti)','Pizza(Roman)','Antipasti(Bruschetta)','Dolci(Gelato)','Risotto','Kimchi','Bibimbap','Japchae','Mandu','Tteokbokki','Ramen(Buldak)'])

comboo={'Price':[700,350,450,120,450,350,500,560]}
df4=pd.DataFrame(comboo,index=['Kimchi-Biryani','Naan-kimbap','Bibimbap-Bhaji','Samosa-Kimchi','Palak Paneer-Ravioli','Garlic naan_Pizza','Saffron Risoto-Biryani','Falafel-Panzerotti'])

def c_type(n):
    cust=['Premium','Registered','Not Registered']
    if cust[n]==cust[0]:
        discount=0.25
    elif cust[n]==cust[1]:
        discount=0.1
    else:
        discount=0
    return discount
dis=int(input("Enter c_type \n 0 for Premium \n 1 for Registered \n 2 for Not Registered"))

def Khaane_ka_maal():
    l=['Beverages','Snacks','Food','Combo','Recommendations']
    d1=pd.Series(l,index=[1,2,3,4,5])
    print(d1)


def beverages():
    print("What beverage would you like to have!")
    b=['Coffee','Tea','Juice','Back']
    b1=pd.Series(b,index=[1,2,3,4])
    print(b1)

def coffee():
    print("Coffees")
    c=['Latte','Americano','Iced Coffee','Turkish Coffee','Espresso','Cappuccino']
    c1=pd.Series(c,index=[1,2,3,4,5,6])
    print(c1)
    cn=int(input("Enter your coffee type"))
    user=input(f"Do you want{c[cn-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',c[cn-1])
        print('here is your bill',df1.loc[c[cn-1]-(c_type(dis)*df1.loc[c[cn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")


def tea():
    print("Tea")
    t=['Black tea','Green tea','Normal masala tea','Herbal tea','Rooibos tea','Purple tea']
    t1=pd.Series(t,index=[1,2,3,4,5,6])
    print(t1)
    tn=int(input("Enter your tea type"))
    user=input(f"Do you want{t[tn-1]},Yes or No ")
    if user=='Yes' or user=='yes':
        print('Here is your',t[tn-1])
        print('here is your bill',df1.loc[t[tn-1]-(c_type(dis)*df1.loc[t[tn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")


def juice():
    print("Juices")
    j=['Orange juice','Apple Juice','Mango Juice','Grape Juice','Pomegranate Juice','Guava Juice']
    j1=pd.Series(j,index=[1,2,3,4,5,6])
    print(j1)
    jn=int(input("Enter your juice type"))
    user=input(f"Do you want{j[jn-1]},Yes or No ")
    if user=='Yes' or user=='yes':
        print('Here is your',j[jn-1])
        print('here is your bill',df1.loc[j[jn-1]-(c_type(dis)*df1.loc[j[jn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")





def snacks():
    print("I think you are little bit hungry.\n Let me know please your choice")
    s=['Chips & Crisps','Nuts & Seeds','Sweet Treats','Back']
    s1=pd.Series(s,index=[1,2,3,4])
    print(s1)

def chips_crisps():
    print("Chips & Crisps")
    cc=['Potato Chips','Banana Chips','Sweet Potato','Beet Chips','Yuca Chips','Plantain Chips']
    cc1=pd.Series(cc,index=[1,2,3,4,5,6])
    print(cc1)
    ccn=int(input("Enter your chips type"))
    user=input(f"Do you want{cc[ccn-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',cc[ccn-1])
        print('here is your bill',df2.loc[cc[ccn-1]-(c_type(dis)*df2.loc[cc[ccn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def nuts_seeds():
    print("Nuts & Seeds:")
    ns=['Almonds','Walnuts','Cashews','Chia Seeds','Pistachios','Sunflower Seeds']
    ns1=pd.Series(ns,index=[1,2,3,4,5,6])
    print(ns1)
    nsn=int(input("Enter your requirement"))
    user=input(f"Do you want{ns[nsn-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',ns[nsn-1])
        print('here is your bill',df2.loc[ns[nsn-1]-(c_type(dis)*df2.loc[ns[nsn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")
        
def sweet_treats():
    print("Sweet Treats")
    st=['Chocolate','Ice-Cream','Pastries','Cookies','Desserts','Smoothies']
    st1=pd.Series(st,index=[1,2,3,4,5,6])
    print(st1)
    stn=int(input("Enter number for your choice"))
    user=input(f"Do you want{st[stn-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',st[stn-1])
        print('here is your bill',df2.loc[st[stn-1]-(c_type(dis)*df2.loc[st[stn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")






def food():
    print("we have different variety of food")
    f=['Indian','Italian','Korean']
    f1=pd.Series(f,index=[1,2,3])
    print(f1)

def indian():
    print("We have different Indian Food")
    i=['Idli-Dosa','Biryani','Curry-Rice','Tandoori-Chicken','Samosa-Kachori','Jalebi']
    i1=pd.Series(i,index=[1,2,3,4,5,6])
    print(i1)
    ins=int(input("Enter number for your choice"))
    user=input(f"Do you want{i[ins-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',i[ins-1])
        print('here is your bill',df3.loc[i[ins-1]-(c_type(dis)*df3.loc[i[ins-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def italian():
    print("We have different Italian food")
    it=['Pasta(Spaghetti)','Pizza(Roman)','Antipasti(Bruschetta)','Dolci(Gelato)','Risotto']
    it1=pd.Series(it,index=[1,2,3,4,5,6])
    print(it1)
    itn=int(input("Enter number for your choice"))
    user=input(f"Do you want{it[itn-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',it[itn-1])
        print('here is your bill',df3.loc[it[itn-1]-(c_type(dis)*df3.loc[it[itn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")
 
def korean():
    print("We have different korean food")
    k=['Kimchi','Bibimbap','Japchae','Mandu','Tteokbokki','Ramen(Buldak)']
    k1=pd.Series(k,index=[1,2,3,4,5,6])
    print(k1)
    kn=int(input("Enter number for your choice"))
    user=input(f"Do you want{k[kn-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',k[kn-1])
        print('here is your bill',df3.loc[k[kn-1]-(c_type(dis)*df3.loc[k[kn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")




def combo():
    print("Combos")
    c={'Indian-Korean-Combo':['Kimchi-Biryani','Naan-kimbap','Bibimbap-Bhaji','Samosa-Kimchi'],'Indian-Italian':['Palak Paneer-Ravioli','Garlic naan_Pizza','Saffron Risoto-Biryani','Falafel-Panzerotti']}
    c1=pd.Series(c)
    print(c1)
    for k,v in c.items():
        print(k+":")       
        for v1 in v:
            print(" ",v1)
        print()

def ind_ko():
    print("It is very popular nowadays")
    ik=['Kimchi-Biryani','Naan-kimbap','Bibimbap-Bhaji','Samosa-Kimchi']
    ik1=pd.Series(ik,index=[1,2,3,4])
    print(ik1)
    ikn=int(input("Enter number for your choice"))
    user=input(f"Do you want{ik[ikn-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',ik[ikn-1])
        print('here is your bill',df4.loc[ik[ikn-1]-(c_type(dis)*df4.loc[ik[ikn-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")


def ind_it():
    print("Indian-Italian!!")
    ini=['Palak Paneer-Ravioli','Garlic naan_Pizza','Saffron Risoto-Biryani','Falafel-Panzerotti']
    ini1=pd.Series(ini,index=[1,2,3,4])
    print(ini1)
    inin=int(input("Enter number for your choice"))
    user=input(f"Do you want{ini[inin-1]},'yes' or 'no' ")
    if user=='Yes' or user=='yes':
        print('Here is your',ini[inin-1])
        print('here is your bill',df4.loc[ini[inin-1]-(c_type(dis)*df4.loc[ini[inin-1]]),'Price'])  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")



def recommendations():
    print('Let us know your choice,please!!')
    r=['Mood','Weather','Appetite']
    r1=pd.Series(r,index=[1,2,3])
    print(r1)

def mood():
    print("Let us know how is your mood right now")
    m=['Happy','Sad','Bored']
    m1=pd.Series(m,index=[1,2,3])
    print(m1)
def happy():
    print("How sweet,you are happy.you would take")
    m={'Coffee':'Latte','Food':'Idli-Dosa','Snack':'Almonds'}
    m1=pd.DataFrame(m,index=[1])
    print(m1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or user=='yes':
        print("Okay,here is your")
        for k,v in m.items():
            print(k+":")
            print(" "+v)
        print()
        price=(df1.loc['Latte','Price']+df3.loc['Idli-Dosa','Price']+df2.loc['Almonds','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def sad():
    print("Ohh,you definitely have something to make your mood better")
    s={'Coffee':'Espresso','Food':'Samosa-Kachori','Snack':'Desserts'}
    s1=pd.DataFrame(s,index=[1])
    print(s1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or 'yes':
        print("Okay,here is your")
        for k,v in s.items():
            print(k+":")
            print(" "+v)
        print()
        price=(df1.loc['Espresso','Price']+df3.loc['Samosa-Kachori','Price']+df2.loc['Desserts','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))
    elif user=='No' or 'no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def bored():
    print("You get something to make yourself better")
    b={'Coffee':'Turkish','Food':'Bibimbap','Snack':'Ramen'}
    b1=pd.DataFrame(b,index=[1])
    print(b1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or 'yes':
        print("Okay,here is your")
        for k,v in b.items():
            print(k+":")
            print(" "+v)
        print()
        price=(df1.loc['Turkish','Price']+df3.loc['Bibimbap','Price']+df2.loc['Ramen','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))   
    elif user=='No' or 'no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def weather():
    print("Please let us know how the weather is!!")
    w=['Sunny','Windy','Cloudy']
    w1=pd.Series(w,index=[1,2,3])
    print(w1)

def sunny():
    print("For sunny weather you should have") 
    s={'Coffee':'Iced Coffee','Food':'Pasta(Spaghetti)','Snack':'Sweet'}
    s1=pd.DataFrame(s,index=[1])
    print(s1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or user=='yes':
        print("Okay,here is your")
        for k,v in s.items():
            print(k+":")
            print(" "+v)
        print()
        price=(df1.loc['Iced Coffee','Price']+df3.loc['Pasta(Spaghetti)','Price']+df2.loc['Sweet','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))  
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def windy():
    print("For windy weather you should have") 
    w={'Coffee':'Cappuccino','Food':'Risotto','Snack':'Cashew'}
    w1=pd.DataFrame(w,index=[1])
    print(w1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or user=='yes':
        print("Okay,here is your")
        for k,v in w.items():
            print(k+":")
            print(" "+v)
        print()
        price=(df1.loc['Cappuccino','Price']+df3.loc['Risotto','Price']+df2.loc['Cashew','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))    
    elif user=='No' or user=='no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def cloudy():
    print("For cloudy weather you should have") 
    c={'Coffee':'Americano','Food':'Pav-Bhaji','Snack':'Chocolate'}
    c1=pd.DataFrame(c,index=[1])
    print(c1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or 'yes':
        print("Okay,here is your")
        for k,v in c.items():
            print(k+":")
            print(" "+v)
        print()
        price=(df1.loc['Americano','Price']+df3.loc['Pav-Bhaji','Price']+df2.loc['Chocolate','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))  
    elif user=='No' or 'no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def apettite():
    print("Please let us know about your apettite")
    a=['Physical','Mental']
    a1=pd.Series(a,index=[1,2])
    print(a1)

def physical():
    print("Health Conscious!!")
    p={'Coffee':'Turkish','Food':'Bibimbap','Snack':'Ramen'}
    p1=pd.DataFrame(p,index=[1])
    print(p1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or 'yes':
        print("Okay,here is your")
        for k,v in p.items():
            print(k+":")
            print(" "+v)
        print() 
        price=(df1.loc['Turkish','Price']+df3.loc['Bibimbap','Price']+df2.loc['Ramen','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))          
    elif user=='No' or 'no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")

def mental():
    print("Okay,We have something for you")
    m={'Coffee':'Iced Coffee','Food':'Biryani','Snack':'Sweet Potato'}
    m1=pd.DataFrame(m,index=[1])
    print(m1)
    print()
    print("Would you like to give it a try?")
    user=input("Enter Yes or No ")
    if user=='Yes' or 'yes':
        print("Okay,here is your")
        for k,v in m.items():
            print(k+":")
            print(" "+v)
        print()   
        price=(df1.loc['Iced Coffee','Price']+df3.loc['Biryani','Price']+df2.loc['Sweet Potato','Price'])
        print('here is your total bill',price,"after discount your bill is",price-price*c_type(dis))        
    elif user=='No' or 'no':
        print("Its completely fine!!")
    else:
        print("Please select one of them")


print("Hello Sir/Mam Welcome to machine number 1, What would you like to have!!")
Khaane_ka_maal()
      
n=int(input("Please enter the number for your choice"))
if n==1:
    print("Ohh,You are looking for Beverages")
    beverages()

    n1=int(input("Please enter number for your choice"))
    if n1==1:
        print("Nice,you are looking for Coffee.\nHere are some coffees which are available.")
        coffee()
        print("\n")
    elif n1==2:
        print("Nice,you are looking for Tea.\nHere are some tea which are available.")
        tea()
        print("\n")
    elif n1==3:
        print("Juice is good for health")
        juice()
        print("\n")
    elif n1==4:
        Khaane_ka_maal()
    else:
        print("select one of the given numbers,please!!")
        
elif n==2:
    print("Ohh,You are looking for Snacks")
    snacks()

    n2=int(input("Enter number for your choice"))
    if n2==1:
        print("Ohh,Chips & Crisps")
        chips_crisps()
    elif n2==2:
        print("Nuts & Seeds")
        nuts_seeds()
    elif n2==3:
        print("Sweet Treats")
        sweet_treats()
    elif n2==4:
        Khaane_ka_maal()
    else:
        print("Select one of them given number,please!!")



elif n==3:
    print("Ohh, You are looking for Food")
    food()   
    n3=int(input("Enter numberfor your choice")) 
    if n3==1:
        print("Nice choice")
        indian()
    elif n3==2: 
        print("Italian")
        italian()
    elif n3==3:
        print("Korean")
        korean()
    elif n3==4:
        Khaane_ka_maal()
    else:
        print("Select one of the given number,please!!")

elif n==4:
    print("Which combo would you prefer")
    combo()
    n4=int(input("Enter number for your choice"))
    if n4==1:
        print("Indian-Korean")
        ind_ko()
    elif n4==2:
        print("Indian_Italian")
        ind_it()
    else:
        print("We have only two combo")


elif n==5:
    print("We are here to help you!!!")
    recommendations()
    n5=int(input("Enter,so we can recommend you a food type"))
    if n5==1:
        mood()
        n51=int(input("Enter please"))
        if n51==1:
            happy()
        elif n51==2:
            sad()
        elif n51==3:
            bored()
        else:
            print("Select one of them")


    elif n5==2:
        weather()
        n52=int(input("Enter please"))
        if n52==1:
            sunny()
        elif n52==2:
            windy()
        elif n52==3:
            cloudy()
        else:
            print("Please select one of them")

    elif n5==3:
        apettite()
        n53=int(input("Enter please"))
        if n53==1:
            physical()
        elif n53==2:
            mental()
    else:
        print("Please select one of them")

else:
    print("Select one of the given numbers,please!")






