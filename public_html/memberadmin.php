<?php

$NO=$_GET["NO"];

require_once('dbconnect.php');

echo "<br/>";

mysqli_select_db($link,'mydb');


//查詢資料
$sql="SELECT * FROM member_table WHERE NO='$NO'";
$result = mysqli_query($link,$sql);
while ($row = mysqli_fetch_assoc($result)){

  $NO=$row['NO']; $password=$row['password'];
  $email=$row['email']; 

}

echo "<form action='memberadminDone.php' method='post'>";
echo "<font face='Noto Sans TC'>使用者名稱: $username <input type='hidden' value='$username' name='username' style='width:50px;'></font>";
echo "<br//>";

echo " <font face='Noto Sans TC'>使用者密碼: <input type='password' value='' name='password' style='width:200px;'></font>";
echo "<br//>";
echo " <font face='Noto Sans TC'>請再一次輸入使用者密碼: <input type='password' value='' name='password2' style='width:200px;'></font>";
echo "<br//>";
echo "<font face='Noto Sans TC'>電子信箱 <input type='text' value='$email' name='email' style='width:200px;'></font>";
echo "<br//>";

echo "<input type='submit' value='update'></br>";
echo "</form>";



mysqli_close($link);

?>