for file in *.png; do
 convert -resize 50% $file "${file%.png}.png"
done


