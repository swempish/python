from sys import exit
print('***Register System***')
hesap = input('Type User Name:')
print('Username succesfuly saved as', hesap)
sifre = input('Type Password:')
print('Password succesfuly saved.')
print('')
print('')
print('***Login System***')
hesap_g = input('Username:')

if hesap_g == hesap:
    sifre_g = input('Password:')

    if sifre_g == sifre:
            print("You've been logged as", hesap)
            print('************', hesap, '************') 
    else:
            print('Password is wrong. Try again later.')
else:
      print('Username not found.')
