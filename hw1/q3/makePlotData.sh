touch zorderCommands
for i in {0..16383}
do
    echo "izorder -n 7 $i" >> zorderCommands
done

touch horderCommands
for i in {0..16383}
do
    echo "ihorder -n 7 $i" >> horderCommands
done

cat zorderCommands | ./q3 > zorderData
cat horderCommands | ./q3 > horderData
rm -f zorderCommands
rm -f horderCommands
