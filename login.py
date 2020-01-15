from sys import exit
print('***Kayıt Sistemi***')
hesap = input('Kayıt Olmak İçin Kullanıcı Adınızı Girin:')
print('Kullanıcı Adınız Başarı ile', hesap, 'olarak kaydedildi.')
sifre = input('Şifrenizi Girin:')
print('Şifreniz Başarı İle Kaydedildi')
print('***Giriş Yapma Sistemi***')
hesap_g = input('Kullanıcı Adı:')

if hesap_g == hesap:
    sifre_g = input('Şifre:')

    if sifre_g == sifre:
            print(hesap, 'Olarak Oturum Açtınız')
            print('************', hesap, '************') 


    else:
            print('Şifre hatalı.Lütfen tekrar deneyiniz.')
            
            
            
            

else:
      print('Kullanıcı Adı Bulunamadı.')