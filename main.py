from argparse import ArgumentParser
from os import system, name
from requests import get
from threading import Thread
from time import time

FlagReject = 0
FlagOK     = 0

def GetURL(url):
	global FlagReject
	global FlagOK
	response = get(url)
	if response.status_code == 200:
		FlagOK += 1
	else:
		FlagReject += 1

def ClearScreen():
	if name == "nt":
		system("cls")
	elif name == "posix":
		system("clear")
	else:
		return
		
if __name__ == "__main__":
	try:
		parser = ArgumentParser(description='Menambah jumlah pengunjung di badge github')

		parser.add_argument('-U', '--username', dest='username', type=str, help='Username GitHub kalian.')
		parser.add_argument('-I', '--iterasi', dest='iterasi', type=int, help='Iterasi untuk perulangan berapa x program diulang.')

		args = parser.parse_args()

		if args.username is None:
			args.username = 'syauqqii'
		if args.iterasi is None:
			args.iterasi = 10

		LinkBadge = f"https://visitor-badge.laobi.icu/badge?page_id={args.username}"

		TempThread = []
		WaktuMulai = time()

		for i in range(args.iterasi):
			for j in range(7):
				thread = Thread(target=GetURL, args=[LinkBadge])
				TempThread.append(thread)
				thread.start()

			for thread in TempThread:
				thread.join()

			ClearScreen()

			print(f"\n > Iterasi: [{i+1}/{args.iterasi}] | Username GitHub: @{args.username}\n")
			print(f"   Berhasil Terkirim : {FlagOK}")
			print(f"   Gagal Terkirim    : {FlagReject}")
			TempThread.clear()
		print(f"\n > Berhasil menyelesaikan {args.iterasi*7} request dalam waktu {time()-WaktuMulai:.2f} detik.")
	except KeyboardInterrupt:
		print(f"\n > Program berjalan selama {time()-WaktuMulai:.2f} detik.")
		exit(0)
