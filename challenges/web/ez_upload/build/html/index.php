<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset="UTF-8">
    <title>文件上传</title>
</head>
<body>
    <div class="upload-form">
        <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="upload" id="">
        <button tyoe="sumbit">上传</button>
    </div>
    <div class="msg">
        <?php
        if(isset($_FILES['upload'])){
        $tmp_name = $_FILES['upload']['tmp_name'];
        $dir = "./upload/";
        $filename = $_FILES['upload']['name'];
        if(move_uploaded_file($tmp_name,$dir . $filename) === false){
          echo "$filename 文件上传失败啦<br/>";
        }
        echo "文件不符合要求，正在删除中......</br>";
        sleep(3);
        unlink($dir . $filename);
        echo "$filename 删除完成";
    }else{
        echo "请选择上传文件";
    }
    ?>
  </div>
</body>
</html>



