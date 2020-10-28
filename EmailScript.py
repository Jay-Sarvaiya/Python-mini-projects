import smtplib as s
obj = s.SMTP("smtp.gmail.com",587)
obj.starttls()
print("Make sure your 'double verification' is enabled or you have enabled 'Less Secure App Access'")
loginAddress = input("Enter the email id from which you want to send the mail")
loginPassword = input(loginAddress+"\nEnter the password of the mentioned email id")
obj.login(loginAddress,loginPassword)
subject = input("Enter the Subject part of the mail")
body = input("Enter the body part of the mail")
addressList = []
address = 1
if(address != 0):
    address = input("Enter the email addresses and press 0 if completed")
    addressList.append(address)
message = "Subject:{}\n\n{}".format(subject,body)
obj.sendmail(loginAddress,addressList,message)
print("Mail Sent Successfully")
obj.quit()