for img in *.png; do
 filename=$(basename "$img")
 fname="${filename%.*}"
 convert $img -crop 637x428+253+40 -transparent white "$fname"_cropped.png
done
