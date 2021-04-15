import sys , os ,sys,tqdm
try:
	import requests as rq 
	from bs4 import BeautifulSoup as Bf
except:
	msg=" if u in linux run this command to download the lising library"
	comm="pip3 install requests bs4"
	print(msg)
	print(comm)
#############some
def the_help():
	print("please chose one from this list")
	for i in img_cat:
		print(i)
		help_msg="""
			usage:
				walpaper_tool.py wall_type num_of_start_page num_end_page
 
			ex:
				walpaper_tool.py anime 1 4

				walpaper_tool.py black 2 3


		"""
	print(help_msg)
	sys.exit()


main_url="https://wallpaperscraft.com/catalog/"
img_cat=["anime","art","60_favorites","black","city","dark","fantasy","macro","music","nature","space","hi-tech","vector","words","abstract","3d","smilies","other"]
resolution='1600x900'
try:
	sub=sys.argv[1]
	s=int(sys.argv[2])
	num_page=int(sys.argv[3])

except:
	the_help()
header={
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
the_url=main_url+sub
links=[]
final_links=[]
final_links2=[]

class wal:
	def get_data(self,url):
		return rq.get(url,headers=header)


	def search_in_data(self,data,tag,attr,value):
		soup=Bf(data.text,"html.parser")
		return soup.find_all(tag,{attr:value})


	def downloader(self,img_url):
		data=rq.get(img_url,headers=header)
		img_url=img_url.split('/')
		name=img_url[-1]
		op=open(name,"wb")
		op.write(data.content)
		print(f"was downloades {name}")
		op.close()

if sub in img_cat:
	exc = wal()
	def get_urls_by_page(the_url):
		data = exc.get_data(the_url)
		my_img_url_list=exc.search_in_data(data,"a","class","wallpapers__link")
		for i in my_img_url_list:
			wall_url="https://wallpaperscraft.com"+i["href"]
			if wall_url not in links:
				if 'girl' not in wall_url:
					links.append(wall_url)
					print(wall_url)


	for i in range(s,num_page+1):
		if i>1:
			the_url=f"https://wallpaperscraft.com/catalog/{sub}/page{i}"
		print(the_url)
		get_urls_by_page(the_url)

	def get_url_by_resolution(url,tag,attr,value):
		data = exc.get_data(url)
		final_link_in_html=exc.search_in_data(data,tag,attr,value)
		for i in final_link_in_html:
			if i.text==resolution:
				r=i['href']
				r=r.split("/")
				r="https://images.wallpaperscraft.com/image/"+r[-2]+"_"+r[-1]+".jpg"
				if r not in final_links:
					final_links.append(r)
					print(r)

	for i in links:
		get_url_by_resolution(i,"a","class","resolutions__link")
	print("*"*35)
	print("Start downloading")
	print("*"*35)
	try:
		os.makedirs(sub)
	except:
		pass
	os.chdir(sub)

		#start downloading
	for i in final_links:
		if "girl" not in i :
			exc.downloader(i)

	n=len(final_links)
	print(f"Dont {n}")
	print("*"*35)
		


else:
	the_help()