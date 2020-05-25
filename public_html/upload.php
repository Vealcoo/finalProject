<?php session_start();
ini_set('display_errors','1');
error_reporting(E_ALL);
function exec_timeout($cmd,$timeout=60){
    $start=time();
    $outfile=uniqid('/tmp/out',1);
    $pid=trim(shell_exec("$cmd >$outfile 2>&1 & echo $!"));
    if(empty($pid)) return false;
    while(1){
            if(time()-$start>$timeout){
                    exec("kill -9 $pid",$null);
                    break;
            }
            $exists=trim(shell_exec("ps -p $pid -o pid="));
            if(empty($exists)) break;
            sleep(1);
    }
    $output=file_get_contents($outfile);
    unlink($outfile);
    return $output;
}

require_once('dbconnect.php');
// $link = @mysqli_connect('localhost','marc','ji3g45/4u;6','webTest')or die("Invalid query: " . mysqli_error($link));
# 檢查檔案是否上傳成功
if ($_FILES['uploadfile']['error'] === UPLOAD_ERR_OK){
  // echo '檔案名稱: ' . $_FILES['uploadfile']['name'] . '<br/>';
  // echo '檔案類型: ' . $_FILES['uploadfile']['type'] . '<br/>';
  // echo '檔案大小: ' . ($_FILES['uploadfile']['size'] / 1024) . ' KB<br/>';
  // echo '暫存名稱: ' . $_FILES['uploadfile']['tmp_name'] . '<br/>';

  # 檢查檔案是否已經存在
  // if (file_exists('upload/' . $_FILES['uploadfile']['name'])){
  //   echo '檔案已存在。<br/>';
  // } else {

  $file = $_FILES['uploadfile']['tmp_name'];
  $time=time();

//   $dest = '/home/webber/anaconda2/envs/crp/upload/' .$time."_". $_FILES['uploadfile']['name'];
  $dest = '/home/webber/public_html/upload/' .$time."_". $_FILES['uploadfile']['name'];
  $db_path = 'upload/' .$time."_". $_FILES['uploadfile']['name'];

 # echo $dest;

  $id = $_SESSION['username'];
  $sql2 = "SELECT NO FROM member_table where username = '$id'";
  $result2 = mysqli_query($link,$sql2);
  while ($row2 = mysqli_fetch_assoc($result2)){
    $NO=$row2['NO'];
  }

  $sql = "INSERT INTO `dis_picture` (`NO`, `path`) VALUES ('$NO', '$db_path')";
  // INSERT INTO `img_path` (`NO`, `path`) VALUES (NULL, 'upload/e04');
  $SaveImgPath = mysqli_query($link,$sql)or die("Invalid query: " . mysqli_error($link));

  $sql3 = "SELECT DP_Num FROM dis_picture where dis_picture.path = '$db_path'";
  $result3 = mysqli_query($link,$sql3);
  while ($row3 = mysqli_fetch_assoc($result3)){
    $DP_Num=$row3['DP_Num'];
  }

  # 將檔案移至指定位置/home/webber/
  move_uploaded_file($file, $dest);


  #$output = exec('/home/webber/anaconda2/envs/crp/bin/python /home/webber/anaconda2/envs/crp/predict.py {$dest} {$DP_Num}');  ####
  $output = exec_timeout("/home/webber/anaconda2/envs/crp/bin/python /home/webber/anaconda2/envs/crp/predict.py $dest $DP_Num $NO");
  if($output!=null){
      header("Location: resultHistoryD.php");
   }else{header("Location: member.php");}


    // // 创建socket
    // $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP); 
    // // 连接服务器
    // $connection = socket_connect($socket, '140.127.220.107', '9999');  
    // // 接收返回数据
    // $buffer = socket_read($socket, 1024);
    // echo $buffer;
    // // $socket = fsockopen("127.0.0.1",3434,$errno,$errster,1);
    // // echo fread($socket,128);

   
 } else {
   echo '錯誤代碼：' . $_FILES['uploadfile']['error'] . '<br/>';
 }



?>