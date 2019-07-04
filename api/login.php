<?php 
  // create curl resource
  $ch = curl_init();
  // set url 
  //curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/employees/?name=Baron");
  //curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/surveyor/");
  curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/surveyor/login/sundeo/Password/");
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); //Return data instead printing directly in Browser
  curl_setopt($ch, CURLOPT_HEADER, 0);
  // $output contains the output json
  $output = curl_exec($ch);
  // close curl resource to free up system resources 
  curl_close($ch);
  echo "<br>";
  echo $output;
  echo "<br>";
  /*
  $users = json_decode($output); // decode the JSON feed
  echo $users->firstName . '<br>';
  echo $users->lastName . '<br>';
  echo $users->userName . '<br>';
  echo $users->email . '<br>';
  echo $users->password . '<br>';
  */
