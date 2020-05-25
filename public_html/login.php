<?php
session_start();
require_once('dbconnect.php');

$uid=$_POST["userid"];
$upwd=$_POST["pwd"];

$sql = "SELECT * FROM member_table where username = '$uid'";
$result = mysqli_query($link, $sql);

$row = @mysqli_fetch_row($result);

$sql2 = "SELECT NO FROM member_table where username = '$uid' and password = '$upwd'";
$result2 = mysqli_query($link, $sql2);
while ($row2 = mysqli_fetch_assoc($result2)){
    $NO=$row2['NO'];
  }


if($NO==1)
{
        $_SESSION['username'] = $uid;
		$_SESSION["login_session"] = true;
		header("Location: loginm.php");	
	}
elseif($uid != null && $upwd != null && $row[1] == $uid && $row[2] == $upwd)
{
        $_SESSION['username'] = $uid;
		$_SESSION["login_session"] = true;
		header("Location: member.php");	
	}
else
{
	$_SESSION["login_session"] = false;
	header("Location: index.html");	
}
?>