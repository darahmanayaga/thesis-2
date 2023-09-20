import requests
import csv 

headers = {'Accept': 'application/json', 
           'Content-Type':'application/json'}


visayas_url = "https://psgc.gitlab.io/api/island-groups/visayas/provinces/"
response = requests.request('GET',visayas_url,headers= headers , data = {})
visayas = response.json()


provinces=[] #luzon and visayas provinces 
for i in range(0,len(visayas)): 
    provinces.append(visayas[i]['name'].upper())


luzon_url = "https://psgc.gitlab.io/api/island-groups/luzon/provinces/"
response = requests.request('GET',luzon_url,headers= headers , data = {})
luzon = response.json()

for i in range(0,len(luzon)): 
    provinces.append(luzon[i]['name'].upper())




def provinces(): 
    return provinces # returns list of provinces 

def min_provinces(): 
    mindanao_url = "https://psgc.gitlab.io/api/island-groups/mindanao/provinces/"
    response = requests.request('GET',mindanao_url,headers= headers , data = {})
    luzon = response.json()

    min_provinces = []
    for i in range(0,len(luzon)): 
        min_provinces.append(luzon[i]['name'].upper())
    return min_provinces # returns list of mindanao provinces 

def check_province(list1,list2):
    l2 = set(list2)
    not_same= [x for x in list1 if x not in l2] #check what provinces are in the dataset that don't have updated names 
    print(not_same)
