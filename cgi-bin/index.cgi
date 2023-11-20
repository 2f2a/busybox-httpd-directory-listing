#!/bin/sh
echo -en "Content-Type: text/html\r\n\r\n"

cat << EOH
<!DOCTYPE html>
<html lang="en">
<head>
  <title></title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

</head>
<script>

</script>
<body>

<div class="container">
  <h2>Basic List Group</h2>
  <div id="list" class="list-group">
EOH

function isFolder() {  
  name="$1"
  str=${name: -1}
  # echo $str
  if [ $str == '/' ];then
    echo 1
  else
    echo 0
  fi
}
# isf=`isFolder '../'`
# echo $isf

#create list
#ls -a --group-directories-first ..${REQUEST_URI#${SCRIPT_NAME}}|while read line
ls -a -p "..${REQUEST_URI#${SCRIPT_NAME}}"|while read line
do
  isf=$(isFolder $line)
  if [ $isf == 1 ]; then 
      echo "<br><a href='$line' class='list-group-item' >$line</a>"
  else
     echo "<br><a href='$line' class='list-group-item' target='_blank' >$line</a>"
  fi
done

cat << EOF
  </div>
</div>

</body>
</html>
EOF
