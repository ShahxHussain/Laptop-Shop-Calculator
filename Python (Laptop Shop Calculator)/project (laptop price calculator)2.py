

def buy():
    buy1=int(input("Do you want to buy? Press 1 for yes and 2 for no"))
    if buy1==1:
        adress=str(input("Enter your adress"))
        payment_method=int(input("Enter payment method:\n 1.Bank Account\n 2.Easypaisa/Jazzcash\n 3.Cash On delivery"))
        if payment_method==1:
            bank_account=int(input("Enter account number"))
            print("Money has been deducted")
            print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
        elif payment_method==2:
            phone_no=int(input("Enter your phone number"))
            print("Money has been deducted")
            print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
        elif payment_method==3:
            print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
            


    else:
        print("Thank You")


def laptop_acessory():
    acessory=int(input("What accessory do you want to buy?\n Press 1 for keyboard, 2 for mouse, 3 for battery, 4 for charger"))
   
    if acessory==1:
        keyboard=int(input("Following are the keyboards available:\n Razer Pro Type Ultra   (To buy press 1)\n Fnatic Streak65 Gaming Keyboard   (press 2 to buy)\n Corsair K100 RGB Gaming Keyboard   (Press 3 to buy)\n Press 0 if you do not want to buy from these available keyboards"))
        if keyboard==1:
            print("------\nThe price of Razer Pro Type Ultra Keyboard is Rs 4,000.")
            buy()

        elif keyboard==2:
            print("------\nThe price of Fnatic Streak65 Gaming Keyboard is Rs 5,500.")
            buy()

        elif keyboard==3:
            print("------\nThe price of Corsair K100 RGB Gaming Keyboard is Rs 7,200.")
            buy()

        else:
            print("------\nThank You")

    elif acessory==2:
        mouse=int(input("Following mouse are available:\n Havit MS871 Optical Mouse   (To buy press 1)\n Logitech Optical USB Mouse B100   (To buy press 2)\n A4Tech FM12 Fstyler 1200 DPI Optical Mouse   (press 3 to buy)\n Press 0 if you do not want to buy from these available mouses"))
        if mouse==1:
            print("------\nThe price of Havit MS871 Optical Mouse is Rs 400.")
            buy()

        elif mouse==2:
            print("------\nThe price of Logitech Optical USB Mouse B100 is Rs 650.")
            buy()

        elif mouse==3:
            print("------\nThe price of A4Tech FM12 Fstyler 1200 DPI Optical Mouse is Rs 900.")
            buy()

        else:
            print("------\nThank You")

    elif acessory==3:
        battery=int(input("Following are the available batteries:\n Sony Vaio BPS26 6 Cell laptop Battery   (Press 1 to buy)\n Dell Inspiron 15-5558 4 Cell Laptop Battery   (To buy press 2)\n HP Pavilion VK04 4 Cell Laptop Battery   (press 3 to buy)\n Press 0 if you do not want to buy from these available batteries"))
        if battery==1:
            print("------\nThe price of Sony Vaio BPS26 6 Cell laptop Battery is Rs 2,850.")
            buy()

        elif battery==2:
            print("------\nThe price of Dell Inspiron 15-5558 4 Cell Laptop Battery is Rs 3,200.")
            buy()

        elif battery==3:
            print("------\nThe price of HP Pavilion VK04 4 Cell Laptop Battery is Rs 2,400.")
            buy()

        else:
            print("------\nThank You")

    else:
        charger=int(input("Following are the available chargers:\n 65 Watt 2.5mm Original Laptop Adapter Charger   (To buy press 1)\n 90 Watt 1.7mmmm Original Laptop Adapter Charger   (To buy press 2)\n 19V 3.42A 1.1*3.0mm Original Laptop Adapter Charger   (To buy press 3)\n Press 0 if you do not want to buy from these available chargers"))
        if charger==1:
            print("------\nThe price of 65 Watt 2.5mm Original Laptop Adapter Charger is Rs 3,200.")
            buy()

        elif charger==2:
            print("------\nThe price of 90 Watt 1.7mmmm Original Laptop Adapter Charger is Rs 3,850.")
            buy()

        elif charger==3:
            print("------\nThe price of 19V 3.42A 1.1*3.0mm Original Laptop Adapter Charger is Rs 2,380.")
            buy()

        else:
            print("------\nThank You")
            
        
        
            
    
def Price_Estimate():

    gen=int(input("Which genration laptop you want: enter 1,2,3....11\n"))

    processor=int(input("Which processor do you want? enter 3 for core i3, 5 for core i5, 7 for core i7, 9 for core i9:\n"))

    while processor==1 or processor==2 or processor==4 or processor==6 or processor==8 or processor>9:
        print("core i",processor,"processor does not exist Enter again")
        processor=int(input("Which processor do you want? enter 3 for core i3, 5 for core i5, 7 for core i7, 9 for core i9:\n"))

    ram=int(input("Enter ram:\n"))

    c=int(input("Do you want ssd? press 1 for yes and 2 for no:\n"))

    
    y=70  #price for 1gb ssd

    z=20 #price for 1gb hdd

    if c==1:

        ssd=int(input("enter ssd:\n"))

        hdd=int(input("enter hdd:\n"))

        totalssdprice=ssd*y

        totalhddprice=hdd*z

    else:

        hdd=int(input("enter hdd:\n"))
        ssd="No ssd"
        totalssdprice==0

        totalhddprice=hdd*z

    graphic_card=int(input("Do you want graphic card? press 1 for yes and 2 for no:\n"))

    if graphic_card==1:
        graphiccard1=int(input("Enter Graphic card memory in GB :\n"))
        graphic_card_price=graphiccard1*5000 #price for 1GB memory graphic card
        z=1
        
    else:
        graphic_card_price=0
        graphiccard2="No Graphic card"
        z=0
            

    x=2000 #price for 1gb ram
      
    generation=8000 #price increment per gen

    totalramprice=x*ram
    processorprice=0

    if processor==3:
        processorprice=5000

    elif processor==5:
        processorprice==8000

    elif processor==7:
        processorprice==12000

    elif processor==9:
        processorprice==19000

    else:
        processorprice==0

    

    generationprice=generation*gen

    totalprice=totalramprice+totalssdprice+totalhddprice+generationprice+processorprice+graphic_card_price

    

    print("The price of your laptop is Rs ",totalprice)
    print("Your laptop will have following specifications:\n --------\n processor: core i",processor,",",gen,"generation \n",ram,"GB Ram\n",ssd,"GB SSD \n",hdd,"GB HDD")
    

    if z==1:
        print(graphiccard1,"GB Graphic Card")

    else:
        print("graphiccard2")
        print("Thank You!")

choice=int(input("What do you want to buy?\n Press 1 for laptop, 2 for accessories:\n"))
import random
random_number = random.randint(10000000,99999999)
if choice==1:
    Price_Estimate()
    buy2=int(input("Do you want to buy? Press 1 for yes and 2 for no"))
    if buy2==1:
        adress=str(input("Enter your adress"))
        payment_method=int(input("Enter payment method:\n 1.Bank Account\n 2.Easypaisa/Jazzcash\n 3.Cash On delivery"))
        if payment_method==1:
            bank_account=int(input("Enter account number"))
            print("Money has been deducted")
            print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
        elif payment_method==2:
            phone_no=int(input("Enter your phone number"))
            print("Money has been deducted")
            print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
        elif payment_method==3:
            print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
        
        decision =0
        
    else:
        decision=int(input("Do you want to calculate again?\npress 1 for yes, 2 for no:"))
    
    
        while decision==1:

            Price_Estimate()
            buy2=int(input("Do you want to buy? Press 1 for yes and 2 for no"))
            if buy2==1:
                adress=str(input("Enter your adress"))

                payment_method=int(input("Enter payment method:\n 1.Bank Account\n 2.Easypaisa/Jazzcash\n 3.Cash On delivery"))
                if payment_method==1:
                    bank_account=int(input("Enter account number"))
                    print("Money has been deducted")
                    print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
                elif payment_method==2:
                    phone_no=int(input("Enter your phone number"))
                    print("Money has been deducted")
                    print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
                elif payment_method==3:
                    print("Your tracking number is ",random_number,"\n""Your product will be delivered within 7 working days \nThankYou")
        
                else:
                
                    decision=int(input("--------\nDo you want to calculate again?\npress 1 for yes, 2 for no:"))
    
        

else:
    laptop_acessory()


    


    





    
    
