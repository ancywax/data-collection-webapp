<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_PORT => "8080",
  CURLOPT_URL => "http://192.168.43.233/survey/",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "{\n\t\"survey\":{\"userName\":\"emuwonge\",\"title\":\"Failure in business\"},\n\t\"surveyQuestion\":[\n\t\t\n\t\t{\"questionID\":\"1\",\"question\":\"Whats your business ?\",\"questionType\":\"Multiple Choice\",\"options\":\"null\"},\n\t\t{\"questionID\":\"2\",\"question\":\"When did start your business ?\",\"questionType\":\"Open ended\",\"options\":\"null\"}\n\t\t\n\t]\n\t\n}",
  CURLOPT_HTTPHEADER => array(
    "Accept: */*",
    "Cache-Control: no-cache",
    "Connection: keep-alive",
    "Content-Type: application/json",
    "Host: 10.42.0.175:8080",
    "Postman-Token: 5177e910-a7ca-492a-a397-cfd00c57c133,457f62d3-79d1-421c-88d4-18aaaa88cc69",
    "User-Agent: PostmanRuntime/7.15.0",
    "accept-encoding: gzip, deflate",
    "cache-control: no-cache",
    "content-length: 316"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
?>