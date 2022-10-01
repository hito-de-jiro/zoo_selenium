import os
import requests

from bs4 import BeautifulSoup

HOST = 'https://www.zooplus.de'
URL = 'https://www.zooplus.de/tierarzt/results?animal_99=true'
HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}
COOKIES = {
    'cookie': 'ctid_ch_adv_ss=1353727nh:0|1353727nn:0^1663763632181; sid=ebd591d8-b6ca-4ad1-9972-dd0b87c89f52; CHKSESSIONID=C48F9695BA6E07A4BE7F8D04932B643B; MZPSID=4D7EFE4B1D2E08A9BD4178E10E1C5F47; zt_id=215b9194-ceff-4a61-ab01-33252fea4bf0; hopps.session=Hopps search engine functional cookie.; OptanonAlertBoxClosed=2022-09-21T11:36:34.738Z; OneTrust_PerformanceCookies=YES; at_check=true; OneTrust_FunctionalCookies=YES; OneTrust_TargetingCookies=YES; ctid_ch_adv_ss=1353727nh:0^1663760194784; _dcmn_p=qnU0Y2lkPUNRaG5lR01xOTBPdEZNNlNBRlk; _dcmn_p=qnU0Y2lkPUNRaG5lR01xOTBPdEZNNlNBRlk; _dcmn_p=qnU0Y2lkPUNRaG5lR01xOTBPdEZNNlNBRlk; AMCVS_BD7F317853C3F61D0A490D4E%40AdobeOrg=1; AMCV_BD7F317853C3F61D0A490D4E%40AdobeOrg=-1124106680%7CMCIDTS%7C19257%7CMCMID%7C56961190512255610432355776956207687216%7CMCAAMLH-1664364995%7C6%7CMCAAMB-1664364995%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1663767395s%7CNONE%7CvVersion%7C5.2.0; adb_MrktCloudId=56961190512255610432355776956207687216; s_pfs=%5B%5BB%5D%5D; s_cc=true; cto_bundle=ubHQ2l9sTEM0aXBjOGdQd3pYOXFXYmlSeXhYbzIlMkY3bW1BY3VOVkZBZ2dkN3Y0U2RoNWg0TEp4SXlWQmtsWEprOXpxaU1venZuSVlveXd4c08yNURpSlByaU95Ym5UbDVQUDJKOU01Z09yZ0t2NnV0TUhuaFlqT01rTUQwSFdESWxOTUNJOEFxeTRGanIxU0M3MlpUYjk5azUyUSUzRCUzRA; vetsearch.sid=s%3AcNFiLdcvgKnw2-C0mqAzaBlyYvcsYzaw.8qivUMwAiqS68mAvtqVY0slHIY2ex0%2F9mR021lpBcz0; _hjShownFeedbackMessage=true; _hjSessionUser_720357=eyJpZCI6ImYzNjIxMzNhLThkMzUtNWU1Mi1hZWE2LTk1NjBmYjRmZTc4NyIsImNyZWF0ZWQiOjE2NjM3NjAyMDc3NjQsImV4aXN0aW5nIjp0cnVlfQ==; s_sq=%5B%5BB%5D%5D; s_ips=947; mbox=PC#cd7e10aec47b48dfbedec16e1908cf26.37_0#1727008433|session#7938a0b1a4cf4d708da14e00cc58456f#1663765493; ctid_chain=1353727|1353727; ctid_ch_adv=1353727:0|1353727:0; visit_ctid=1353727; OptanonConsent=isIABGlobal=false&datestamp=Wed+Sep+21+2022+15%3A33%3A52+GMT%2B0300+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D0%BB%D0%B5%D1%82%D0%BD%D0%B5%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.9.0&hosts=&consentId=a01bb100-7191-41a0-9605-b04114a9d807&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=UA%3B18&AwaitingReconsent=false; s_tp=947; s_ppv=www.zooplus.de%2Ftierarzt%2Fresults%2C100%2C100%2C947%2C1%2C1; s_vnum=1666352195130%26vn%3D2; s_invisit=true; s_lv_s=Less%20than%201%20day; _hjIncludedInSessionSample=1; _hjSession_720357=eyJpZCI6ImQwODFmZjBiLWIwNjctNGMyNC1iNDczLTFkN2ViMjU5NGExYyIsImNyZWF0ZWQiOjE2NjM3NjM2MzI1MzMsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; s_plt=1.15; s_pltp=www.zooplus.de%2Ftierarzt%2Fresults; s_getNewRepeat=1663763633424-Repeat; s_lv=1663763633425'
}


def get_html():
    # get response from url
    res = requests.get(url=URL, headers=HEADERS, cookies=COOKIES)
    res.raise_for_status()
    print(res.json)


    # save response as HTML
    with open('get_html.html', 'w', encoding='utf-8') as file:
        file.write(res.text)


def get_content():
    # get loading HTML from file
    with open('get_html.html', 'r', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    print(soup)
    items = soup.find_all('div', class_="search-results")
    print(items)


def main():
    get_html()
    #get_content()


if __name__ == "__main__":
    main()

