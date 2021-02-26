curl https://www.naramed-u.ac.jp/university/gaiyo/shokai/documents/vol[21-75].pdf -O
for i in $(find ./*.pdf)
  do
    echo $i"をtxtに変換"
    pdftotext -q $i
  done
cat vol*.txt > united.txt
rm vol*
python3 gakuho_analysis.py
