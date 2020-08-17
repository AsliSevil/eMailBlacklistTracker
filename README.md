# eMailBlacklistTracker

dnsblInfo-list.txt dosyasında sadece dnsbl.info sitesinde mevcut olan blacklist servisleri listelenmiştir. 

serviceControll.py dosyasında Service class'ı oluşturulmuştur. Bütün blacklist tarama işlemleri bu class'ta gerçekleştirilecektir. 

trackBlacklist.py dosyasında ip veya domain bilgisi alınıp bu bilgilerle Service objeleri yaratılır.

Projede Requests kütüphanesi kullanıldı.  