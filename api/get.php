<?php 
  // create curl resource
  $ch = curl_init();
  // set url 
  //curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/employees/?name=Baron");
  //curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/surveyor/");
  curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/surveyor/registration/sundeo/sundeo@ancywax/");
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); //Return data instead printing directly in Browser
  curl_setopt($ch, CURLOPT_HEADER, 0);
  // $output contains the output json
  $output = curl_exec($ch);
  // close curl resource to free up system resources 
  curl_close($ch);
  echo "<br>";
  echo $output;
  echo "<br>";
  $users = json_decode($output); // decode the JSON feed
  echo $users[0]->lastName . '<br>';
  foreach ($users as $user) {
    echo $user->lastName . '<br>';
  }
?>
<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>
  <h1>API GET DATA</h1>
  <table>
    <tbody>
      <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Username</th>
        <th>Email</th>
        <th>Password</th>
      </tr>
      <?php foreach ($users as $user) : ?>
          <tr>
              <td> <?php echo $user->firstName; ?> </td>
              <td> <?php echo $user->lastName; ?> </td>
              <td> <?php echo $user->userName; ?> </td>
              <td> <?php echo $user->email; ?> </td>
              <td> <?php echo $user->password; ?> </td>
          </tr>
      <?php endforeach; ?>
    </tbody>
  </table>
</body>
</html>
