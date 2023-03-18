#Geolocalisation des IP
#Classification des IP


import sys
import os
import re
import pygeoip
import folium
import time

from progress.spinner import PixelSpinner


fmap = folium.Map(location=[55.7353606, 10.822693], tiles='OpenStreetMap', zoom_start=4)
gi = pygeoip.GeoIP("GeoLiteCity.dat", pygeoip.MEMORY_CACHE)
resulantList = [" "]
#good = False
iplist = "access.log.light.txt"
fd = open(str(iplist), "r")
IP = fd.readlines()

def search(resulantList,ip):
	for i in range(0,len(resulantList)):
		if (resulantList[i] == ip):
			return True
	return False
ans=True
while ans: 
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
	#########################     Dev 000Tonio     ##############################
	
	
	
					1. Simple Ip
		
					2. IP list
		
					3. Exit
	""")
	
	print("\n")
	ans=input("Please Select: ") 
	if ans =='1': 
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')
		ip = input("Entrer une ip: ")
		time.sleep(2)
		os.system('cls' if os.name == 'nt' else 'clear')
		for data in IP:
			try:
				
				infoMAP = gi.record_by_addr(str(ip))
				if(infoMAP != None):
					if(search(resulantList, ip) == True):
						continue
					else:
						resulantList.append(ip)
						print("\n")
						print("#################")
						print("#", ip ,"#")
						print("###################################")
						lat = infoMAP["latitude"]
						lon = infoMAP["longitude"]
						print("Latitude = ",lat)
						print("Longitude = ",lon)
						print("###################################")
						folium.Marker([lat,lon],popup=ip,icon=folium.Icon(color='green')).add_to(fmap)
						print("\n")
						time.sleep(5)
						with PixelSpinner('Processing...') as bar:
							for i in range(10):
								time.sleep(0.01)
								bar.next()
							os.system('cls' if os.name == 'nt' else 'clear')
			except AttributeError:
				pass
		fmap.save('/var/www/html/index.html')
		print("save to /var/www/html/index.html")
		print("\n")
		print("Fin")
		fd.close()
		exit()
	elif ans == '2': 
		os.system('cls' if os.name == 'nt' else 'clear')
		iplist = input("Entrer un fichier contenant des ip: ")
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')
		for data in IP:
			try:
				found = re.search(r"(\d+.\d+.\d+.\d+)", data)
				ip = found.group(1)
				infoMAP = gi.record_by_addr(str(ip))
				if(infoMAP != None):
					if(search(resulantList, ip) == True):
						continue
					else:
						resulantList.append(ip)
						print("\n")
						print("#################")
						print("#", ip ,"#")
						print("###################################")
						lat = infoMAP["latitude"]
						lon = infoMAP["longitude"]
						print("Latitude = ",lat)
						print("Longitude = ",lon)
						print("###################################")
						folium.Marker([lat,lon],popup=ip,icon=folium.Icon(color='green')).add_to(fmap)
						print("\n")
						with PixelSpinner('Processing...') as bar:
							for i in range(10):
								time.sleep(0.01)
								bar.next()
							os.system('cls' if os.name == 'nt' else 'clear')
			except AttributeError:
				pass
		fmap.save('/var/www/html/index.html')
		print("save to /var/www/html/index.html")
		print("\n")
		print("Fin")
		fd.close()
		exit()
	elif ans == '3': 
		os.system('cls' if os.name == 'nt' else 'clear')
		break
	else: 
		os.system('cls' if os.name == 'nt' else 'clear')
		print ("Unknown Option Selected!")
		time.sleep(5)
		os.system('cls' if os.name == 'nt' else 'clear')
		

