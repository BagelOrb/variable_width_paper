for file in *.svg; do
 filename=$(basename "$file")
 fname="${filename%.*}"
 echo $file;
 inkscape -z -e $fname.png $file
done
