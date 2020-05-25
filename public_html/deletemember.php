<!-- jQuery v1.9.1 -->
<script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
<!-- DataTables v1.10.16 -->
<link href="https://cdn.datatables.net/1.10.16/css/jquery.dataTables.min.css" rel="stylesheet" />
<script src="https://cdn.datatables.net/1.10.16/js/jquery.dataTables.min.js"></script>
<!-- fixedHeader.dataTables v3.1.3 -->
<link href="https://cdn.datatables.net/fixedheader/3.1.3/css/fixedHeader.dataTables.min.css" rel="stylesheet" />
<script src="https://cdn.datatables.net/fixedheader/3.1.3/js/dataTables.fixedHeader.min.js"></script>

<style>
table.tt{
  border:1px solid #cccccc;
  width:100%; 
  border-collapse:collapse;
  font-size: 13px;
  font-family: "Gudea";
}
table.tt tr:nth-child(even) {
  border: 1px solid #cccccc;
  background: white;
}
table.tt tr:nth-child(odd) {
  border: 1px solid #cccccc;
  background-color: #f3f3f3;
}
table.tt th{
  background: #003642; 
  border: 1px solid #cccccc;
  color: white;
  font-size: 18px;
}
table.tt td{
  padding: 20px;
  border: 1px; 
  color: #555555; 
  text-align: center;
  border: 1px solid #cccccc;
  line-height:28px;
}
table.tt tr:hover{
  background-color: #FFF8DC;
}

#sexyborder{
  border:1px solid #0066cc; 
  padding:5px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
}

span{
      vertical-align: baseline;
}
.price{
  color: #ff6a11;
  font-size: 24px;
}

</style>

<?php
require_once('dbconnect.php');


echo "<br/>";

mysqli_select_db($link,'mydb');



$NO=$_GET["NO"];


$sql3 = "DELETE FROM member_table WHERE NO = '$NO'";
$delete = mysqli_query($link, $sql3);



echo '<a href="loginm.php">回管理頁面</a> <br>';

$sql = "SELECT * FROM member_table";
$result = mysqli_query($link, $sql);
echo "<div style='text-align:center;'>";
echo "<table class='tt'>";
echo "<thead>";
  echo "<tr>";
  echo "<th>"."NO"."</th>";
  echo "<th>"."MEMBER"."</th>";
  echo "<th>"."PWD"."</th>";

  echo "<th>"."email"."</th>";

  echo "<th>"."刪除"."</th>";
  echo "<th>"."修改"."</th>";
  echo "</tr>";
echo "</thead>";


  echo "<tbody>";
while($row = mysqli_fetch_assoc($result)){

	echo "<tr>";
	echo "<td>". $row['NO'] . "</td>";
	echo "<td>". $row['username'] . "</td>";
  echo "<td>". $row['password'] . "</td>";

	echo "<td>". $row['email'] . "</td>";

	$NO = $row['NO'];

	echo "<td>"."<a href='deletemember.php?NO=$NO'>DELETE</a>" . "</td>";
	echo "<td>"."<a href='memberadmin.php?NO=$NO'>UPDATE</a>" . "</td>";
	echo "</tr>";
	
}
echo "</tbody>";
echo "</table>";
echo "</div>";
mysqli_close($link);

?>

<script>
  $( ".tt" ).DataTable({
    // 參數設定[註1]
    "bPaginate": false, // 顯示換頁
    "searching": true, // 顯示搜尋
    "info": true, // 顯示資訊
    "fixedHeader": true, // 標題置頂
  });
</script>


