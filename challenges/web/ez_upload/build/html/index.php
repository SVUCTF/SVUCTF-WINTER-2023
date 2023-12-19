<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>文件上传</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    #upload-container {
      background-color: #fff;
      padding: 60px;
      /* 调整内边距，使白色框更大 */
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    #upload-form {
      margin-top: 20px;
    }

    #message {
      margin-top: 10px;
      color: #333;
    }

    #error-message {
      color: #ff0000;
    }

    #upload-button {
      font-size: 18px;
      padding: 10px 20px;
      cursor: pointer;
    }
  </style>
</head>

<body>

  <div id="upload-container">
    <h2>传上文件</h2>
    <img id="logo" src="zzz.jpg" alt="Logo">
    <form id="upload-form" action="" method="post" enctype="multipart/form-data">
      <input type="file" name="upload" accept="" required>
      <br><br>
      <button id="upload-button" type="submit">上传文件</button>
    </form>
    <div id="message">
      <?php
      if (isset($_FILES['upload'])) {
        $tmp_name = $_FILES['upload']['tmp_name'];
        $dir = "./upload/";
        $filename = $_FILES['upload']['name'];

        if (move_uploaded_file($tmp_name, $dir . $filename)) {
          echo "文件上传成功";
        } else {
          echo "文件上传失败";
        }

        // 输出消息，表示文件不符合要求，开始删除
        echo "<br>文件不符合要求,正在删除中······ <br/>";

        // 等待3秒（sleep），然后尝试删除文件
        sleep(3);
        unlink($dir . $filename);
        
        echo '<div id="error-message">阿祖别传啦，里面全是 Webshell</div>';

      } else {
        // 如果没有上传文件，输出提示消息
        echo "请选择上传文件";
      }
      ?>
    </div>
  </div>
</body>

</html>
