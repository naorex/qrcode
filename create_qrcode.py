import qrcode
from datetime import datetime

# URLを入力
my_url = input('QRコード化したいURLを入力 :' )

# QRコードを作成する
img = qrcode.make(my_url)

# 日付を取得し、年月日のみへ加工
now = datetime.now()
date = now.date()

# QRコードを画像ファイルで出力する
img.save(f'./QRcode_output/{date}_link.png')