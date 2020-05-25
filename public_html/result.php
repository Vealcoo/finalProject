<!DOCTYPE html>
<html lang="zh-Hant-TW ">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
    <title>SKIN AIdentifier</title> 
    <script src="jquery-3.4.1.js"></script>
    <link rel="stylesheet" href="test.css">
    <link href="https://fonts.googleapis.com/css?family=Noto+Sans+TC&display=swap&subset=chinese-traditional" rel="stylesheet">
    <!-- <script src="all.js"></script> -->
</head>
<body>
        <div class="wrap">
                <div class="header">
                  <div id="mobile">
                        <a id="logo">
                        <img src="https://i.imgur.com/kDvJcYp.png" width=30% height=15% /></a>
                      <ul class="menu">
                          <!---<li><a href="" ><font face="Noto Sans TC">首頁</font></a></li> --->
                          <li><?php session_start();
                              session_start();
                              if(isset($_SESSION["login_session"])){
                                echo "<font face='Noto Sans TC'><a href='login.php'>首頁</a></font>";

                              }
                              else{
                                echo "<font face='Noto Sans TC'><a href='index.html'>首頁</a></font>";
                              }
                              ?>
                          </li>
                          <li><a href="Encyclopedia.php"><font face="Noto Sans TC">小百科</font></a></li>
                          <li><a href="update_info.php"><font face="Noto Sans TC">個人資料</font></a></li>
                          <li><a href=""><font face="Noto Sans TC">歷史結果</font></a></li>
                      </ul>
<script>
  if ($(window).width() <= 798){
$(function(){
   var  $mobile = $('#mobile') ,
        $toggle = $mobile.find('#logo') ,
        $menu = $mobile.find('.menu');
     
    $toggle.click(function(e) {
        $menu.slideToggle()
    });
})
  }
</script>
                      <ul class="login">
                      <li><?php session_start();
                            echo 	"<font face='Noto Sans TC'>".$_SESSION["username"]. " 會員您好". "</font>";
                          ?>
                          </li>
                        <li ><a href="logout.php"><font face="Noto Sans TC">登出</font></a></li>
                        <li id="contact"><a href="#"><font face="Noto Sans TC">聯絡我們</font></a></li>
                      </ul>
                      <script>    
                            $(document).ready(function(){
                                 $(function(){ $('#login').click(function(){ 
                                    $('html,body').animate({scrollTop:$('#content1').offset().top}, 500);});  
                                }); 
                            }); 
                            $(document).ready(function(){
                                 $(function(){ $('#contact').click(function(){ 
                                    $('html,body').animate({scrollTop:$('.location').offset().top}, 500);});  
                                }); 
                            });
                            $(document).ready(function(){
                                 $(function(){ $('#intro').click(function(){ 
                                    $('html,body').animate({scrollTop:$('.content').offset().top}, 500);});  
                                }); 
                            }); 
                    </script>
                    </div>
                        </div>
          <div class="BigLogo">
            <img src="./images/cover.jpg" alt="" >
          </div>
          <div class="clear"></div>



    <div class="result">
      <h2>預測報告</h2>
      <?php
        require_once('dbconnect.php');
        mysqli_query("SET NAMES ‘utf8′");

        mysqli_select_db($link,'mydb');

        $his_Num=$_GET["his_Num"];

        $sql = "SELECT * FROM history,disease_info
        where history.D_NO = disease_info.D_NO
        and history.his_Num = $his_Num ";
        $result = mysqli_query($link, $sql);
        while($row = mysqli_fetch_assoc($result)){
        $his_Num=$row['his_Num'];
        $DP_Num=$row['DP_Num'];
        $NO=$row['NO'];        
        $D_cname=$row['D_cname'];

        $summary=$row['summary'];
        $symption=$row['symption'];
        $risk=$row['risk'];
        $treatment=$row['treatment'];
        }

        

        
        $sql2 = "SELECT * FROM history,dis_picture
        where history.DP_Num = dis_picture.DP_Num
        and history.his_Num = $his_Num";
        $result2 = mysqli_query($link, $sql2);
        while($row2 = mysqli_fetch_assoc($result2)){
          $path=$row2['path'];
        }


        echo $his_Name;


      ?>
      

      <div class="report">
        <div class="top">
          <div class="left">
            <ul>
              <li>
                <p><?php 
                echo "紀錄編號： " . $his_Num;
                ?></p>
              </li>
              <li>
                <p><?php 
                echo "上傳會員： " . $NO;
                ?></p>
              </li>
              <li>
                <p><?php 
                echo "圖片編號： " . $DP_Num;
                ?></p>
              </li>
              <li>
                <p><?php 
                echo "預測疾病： " . $D_cname;
                ?></p>
              </li>
            </ul>
          </div>
          <div class="right">
          
          <p><?php 
                echo "<img src=". $path .">";
                ?></p>
          </div>
        </div>
        <div class="down">
        <ul>
              <li>
              <p><?php echo "概述： " . $summary;?></p>
              </li><br><br><br>
              <p><?php echo "病徵： " . $symption;?></p>

              </li><br><br><br>
              <li>
              <p><?php echo "疾病風險： " . $risk;?></p>

              </li><br><br><br>
              <li>
              <p><?php echo "治療方法： " . $treatment;?></p>

              </li>
            </ul>
        </div>    
      </div>
    </div>


    <div class="clear"></div>

    <div class="location">
      <div class="ourlocation">
        <h2>OUR LOCATION</h2>
      </div>
      <!-- <img src="http://fakeimg.pl/1280x250" alt=""> -->
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3679.8410600253987!2d120.28272561478035!3d22.734148232751163!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346e0f114a51d53b%3A0xe6e681ecaffe55f2!2z5ZyL56uL6auY6ZuE5aSn5a24!5e0!3m2!1szh-TW!2stw!4v1576274636387!5m2!1szh-TW!2stw"
        width="600" height="450" frameborder="0" style="border:0;" allowfullscreen=""></iframe>
    </div>
    <div class="clear"></div>
          <div class="contact">
          <div class="c1">
              <h2><font face="Noto Sans TC">CONTACT US</font></h2>
              <p1><font face="Noto Sans TC">高雄市楠梓區高雄大學700號</font></p1>
              <p2><font face="Noto Sans TC">TEL : 0987654321</font></p2>
              <p3><font face="Noto Sans TC">EMAIL : skinaidentifier@gmail.com</font></p3>
            </div>
            <div class="c2">
                <h3><font face="Noto Sans TC">DONATE US</font></h3>
                <a href=""><font face="Noto Sans TC">We need your help!!!</font></a>
            </div>
            <div class="c3">
                      <div class="message">
                      <p><font face="Noto Sans TC">Leave message to us...</font></p>
                      <input id="message" type="text" name="message">
                      </div>
                      <div class="submit">
                      <input type="submit" value="Sumbit">
                      </div>
            </div>             
          </div>
          <div class="clear"></div>
          <div class="footer">
              <div class="footllist">
              <ul>
                <li><font face="Noto Sans TC">MADE BY NUKIM</font></li>
                <li><a href=""><font face="Noto Sans TC">使用說明</font></a></li>
                <li><a href=""><font face="Noto Sans TC">最新消息</font></a></li>
              </ul>
             </div>
             <div class="footrlist">
              <ul>
                <li><a href=""><font face="Noto Sans TC">網站使用條款</font></a></li>
                <li><a href=""><font face="Noto Sans TC">隱私權政策</font></a></li>
                <li><a href=""><font face="Noto Sans TC">免責聲明</font></a></li>
                <li id="webname"><font face="Noto Sans TC">© 2019 Skin AIdentifier</font></li>
              </ul>
             </div>
        </div>
</body>
</html>