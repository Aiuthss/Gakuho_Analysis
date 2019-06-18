for i in `\find . -type f`
  do
    echo $i
    pdftotext $i
  done
