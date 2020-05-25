<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
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
                          <li><?php session_start();
                              
                              if(isset($_SESSION["login_session"])){
                                echo "<font face='Noto Sans TC'><a href='login.php'>首頁</a></font>";

                              }
                              else{
                                echo "<font face='Noto Sans TC'><a href='index.html'>首頁</a></font>";
                              }
                              ?>
                          </li>
                          <li><a href="Encyclopedia.php"><font face="Noto Sans TC">小百科</font></a></li>
                          <li><a href="#"><font face="Noto Sans TC">個人資料</font></a></li>
                          <li><a href="resultHistoryD.php"><font face="Noto Sans TC">歷史結果</font></a></li>
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
          
          <div class="content">
                          </br>
                          <?php
                          require_once('dbconnect.php');
                          

if($_SESSION['username'] != null)
{
        $id = $_SESSION['login_session'];
        $sql = "SELECT * FROM member_table where username='$id'";
        $result = mysqli_query($link,$sql);
        while ($row = mysqli_fetch_assoc($result)){

          $username=$row['login_session']; $password=$row['password'];
          $email=$row['email']; 
        }
        echo "<br>";
  echo "<form action='update_finish.php' method='post'>";
    echo "<font face='Noto Sans TC'>使用者名稱: $username <input type='hidden' value='$username' name='username' style='width:50px;'></font>";
    echo "<br//>";

  echo " <font face='Noto Sans TC'>使用者密碼: <input type='password' value='' name='password' style='width:200px;'></font>";
    echo "<br//>";
  echo " <font face='Noto Sans TC'>請再一次輸入使用者密碼: <input type='password' value='' name='password2' style='width:200px;'></font>";
  echo "<br//>";
  echo "<font face='Noto Sans TC'>電子信箱 <input type='text' value='$email' name='email' style='width:200px;'></font>";
  echo "<br//>";

  echo "<input type='submit' value='更新'></br>";
  echo "</form>";

  }

else
{
        echo '您無權限觀看此頁面!';
        echo '<meta http-equiv=REFRESH CONTENT=2;url=index.html>';
}
                          
                          
                          ?>

                

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