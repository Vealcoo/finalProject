<?php session_start(); ?>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<?php

//mysql_connect.inc.php
require_once('dbconnect.php');


  $username=$_POST['username']; $password=$_POST['password']; $password2=$_POST['password2'];
  $email=$_POST['email']; 

if($_SESSION['username'] != null && $password != null && $password2 != null && $password == $password2){

        $id = $_SESSION['username'];
    
        $sql = "UPDATE member_table SET username='$username', password='$password', email='$email' 
        where username='$id'";
        if(mysqli_query($link, $sql))
        {
                #echo '修改成功!';
                #echo '<meta http-equiv=REFRESH CONTENT=2;url=member.php>';
                header("Location: member.php");
        }
        else
        {
                echo '修改失敗!';
                echo '<meta http-equiv=REFRESH CONTENT=2;url=member.php>';
        }
}
else
{
        echo '您無權限觀看此頁面!';
        echo '<meta http-equiv=REFRESH CONTENT=2;url=index.html>';
}
?>