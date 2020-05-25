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
                          <!---<li><a href="" ><font face="Noto Sans TC">首頁</font></a></li> --->
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
                          <li><a href="update_info.php"><font face="Noto Sans TC">個人資料</font></a></li>
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
          <div class="BigLogo">
            <img src="./images/cover.jpg" alt="" >
          </div>
          <div class="clear"></div>
          
          <div class="content">
                
          <div class="member">

           <form action="upload.php" method="post" enctype="multipart/form-data">
           <div class="uploadBox">
                   <div class="text">
                       <div class="imgBoard">
                       <img id="preview_uploadImg" src="#" />
                       </div>
                       <!-- <input type="file" id="uploadImg" name="uploadfile" accept="image/jpeg,image/gif,image/png"/> -->
                       <a href="javascript:;" class="a-upload"><font face="Noto Sans TC">
                       <input type="file" id="uploadImg" name="uploadfile" accept="image/jpeg,image/gif,image/png"/>點擊這裡上傳圖片
                       </font></a>
                       <a href="javascript:;" class="s-upload"><font face="Noto Sans TC">
                        <input type="submit" id="upload" name="upload" value="確定上傳" />確定上傳</font>
                        </a>
                       <!-- <input type="submit" id="upload" name="upload" value="確定上傳" /> -->
                   </div>
            </div>
            </form>
            <script>
            $("#uploadImg").change(function(){
            //當檔案改變後，做一些事 
            readURL(this);   // this代表<input id="imgInp">
            });
            function readURL(input){
                if(input.files && input.files[0]){
                    var reader = new FileReader();
                    reader.onload = function (e) {
                    $("#preview_uploadImg").attr('src', e.target.result);
                    }
                    reader.readAsDataURL(input.files[0]);
                }
            }   
            </script>
          <div class="step">

              <h2><font face="Noto Sans TC">Step1 預先拍下需要檢測的部位</font></h2>
              <!-- <div class="stepImg">
                <img src="http://fakeimg.pl/400x80" alt="">
                </div> -->
              
              <h2><font face="Noto Sans TC">Step2 選擇上傳圖檔並確定上傳</font></h2>
              <!-- <div class="stepImg">
                <img src="http://fakeimg.pl/400x80" alt="">
                </div> -->
              
              <h2><font face="Noto Sans TC">Step3 獲取我們為您呈上的預測報告！</font></h2>
              <!-- <div class="stepImg">
                <img src="http://fakeimg.pl/400x80" alt="">
                </div>  -->
              <p><font face="Noto Sans TC">*****系統僅作為初步預測判斷*****</font></p>
              <p><font face="Noto Sans TC">*****如有不適應當儘速就醫！*****</font></p>

          </div>

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