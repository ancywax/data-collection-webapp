<?php
$myFile = "data.json";
$fh = fopen($myFile, 'w') or die("can't open file");
$stringData = $_GET["data"];
fwrite($fh, $stringData);
fclose($fh)

// $ch = curl_init();
//   // set url 
//   //curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/employees/?name=Baron");
//   //curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/surveyor/");
//   curl_setopt($ch, CURLOPT_URL, "http://192.168.43.233:8080/surveyor/login/sundeo/Password/");
//   curl_setopt($ch, CURLOPT_RETURNTRANSFER, 0); //Return data instead printing directly in Browser
//   curl_setopt($ch, CURLOPT_HEADER, 0);
//   // $output contains the output json
//   $output = curl_exec($ch);
//   // close curl resource to free up system resources 
//   curl_close($ch);
//   echo "<br>";
//   echo $output;
//   echo "<br>";
 
?>