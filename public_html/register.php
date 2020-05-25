<?php

$noInfo_flag = false;
$duplicate_flag = false;
$success_flag = false;
$fail_flag = false;


// error_reporting(0);
// $link = @mysqli_connect('localhost','root','ji3g45/4u;6','dbdbd');
require_once('dbconnect.php');
// mysqli_select_db($link,'webTest');
// mysql_query("SET NAMES UTF8");

$pwd1=$_POST["pwd1"];
$pwd2=$_POST["pwd2"];
$username=$_POST["username"];
$email=$_POST["email"];


// if(isset($_POST['submit'])==true){

//     if(empty($uid)==true || empty($upwd)==true || empty($uname)==true || empty($uemail)==true){
//         $noInfo_flag = true;
//     }

// }

if($email != null && $username != null && $pwd1 != null && $pwd2 != null && $pwd1==$pwd2){

    $sql_search = "SELECT * FROM member_table WHERE username='$username'";
    $result = mysqli_query($link, $sql_search);
    $row = mysqli_fetch_array($result);
     
    if($row["username"]=="$username"){

        $duplicate_flag = true;

    }else{
 
        $sql = "INSERT INTO member_table (`username`, `password`, `email`) VALUES('$username','$pwd1','$email')";
        $SaveNewData = mysqli_query($link,$sql);

        if(!$SaveNewData){
            $fail_flag = true;
        }else{
            $success_flag = true;
        }
    }
}else{
    $noInfo_flag = true;
}
?>
 <?php if($noInfo_flag){ ?>
 <div class="alert alert-danger alert-dismissible" role="alert">
 <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
 請輸入所有欄位！
 </div>
 <?php }?>

 <?php if($duplicate_flag){ ?>
 <div class="alert alert-danger alert-dismissible" role="alert">
 <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
 此 username 已經註冊過！
 </div>
 <?php }?>

 <?php 
 if($success_flag){
    echo "註冊成功！";
	header("Refresh:2; url='index.html'");	
 }
 ?>

 <?php if($fail_flag){ ?>
 <div class="alert alert-danger alert-dismissible" role="alert">
 <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
 註冊失敗！
 </div>
 <?php }?>