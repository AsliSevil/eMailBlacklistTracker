import requests


class Service:
    def __init__(self, url, params, ip, domain='\0'):
        self.url = url
        self.params = params
        self.ip = ip
        self.domain = domain

    # for dnsblService--adding img controll
    def searchService(self):
        req = requests.get(self.url, params=self.params)
        res_url = req.url

        res_img = res_url.split('/')[4] #img 'in olduğu .gif adresi
        final_img = res_img.split('_')[1]  #result image'teki red, green, blue yazısı

        if(final_img == 'red'):
            print('Girmiş olduğunuz ', self.ip, ' adresi ', self.params['bl'], ' servisinde kayıtlı olarak bulunmuştur.')
        elif(final_img == 'blue'):
            print('Girmiş olduğunuz ', self.ip, ' adresi taranırken zaman aşımı hatasına uğradı.')