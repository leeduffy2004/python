Bill=int(input("Enter Your Bill:"))
Paid=int(input("How much have you paid:"))
Balance=Paid-Bill
print("Balance:£", Balance)

if Balance>=50:
        fifty=int(Balance/50)
        print("£50 notes:",fifty)
        Balance=Balance-(fifty*50)
if Balance>=20:
        twenty=int(Balance/20)
        print("£20 notes:",twenty)
        Balance=Balance-(twenty*20)
if Balance>=10:
        print("£10 notes:",1)
        Balance=Balance-10
if Balance>=5:
        print("£5 notes:",1)
        Balance=Balance-5
if Balance>=2:
        two=int(Balance/2)
        print("£2 coins:",two)
        Balance=Balance-(two*2)
if Balance>=1:
        print("£1 coins:",1)
        




  