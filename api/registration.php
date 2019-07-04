<?php
	if ( isset($_POST['firstname']) && !empty($_POST['firstname']) and	isset($_POST['lastname'])	&&	!empty($_POST['lastname']) and
		 isset($_POST['username']) && !empty($_POST['username']) and	isset($_POST['email'])	&&	!empty($_POST['email']) and
		 isset($_POST['password']) ){

		//3.1.1 Assigning posted values to variables.
		$firstname 		= $_POST['firstname'];
		$lastname 		= $_POST['lastname'];
		$username	= $_POST['username'];
		$email 		= $_POST['email'];
		$password 		= $_POST['password'];

		$data = array (
        'firstName' => $firstname,
        'lastName' => $lastname,
        'userName' => $username,
        'email' => $email,
        'password' => $password
        );

        $params = '';

    	foreach($data as $key=>$value){
    		$params .= $key.'='.$value.'&';
    	}
         
        $params = trim($params, '&');

        $ch = curl_init();

		curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8000/surveyor/registration/".$username."/".$email."/"); //Remote Location URL
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); //Return data instead printing directly in Browser
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 7); //Timeout after 7 seconds
		curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)");
		curl_setopt($ch, CURLOPT_HEADER, 0);
		    
		//We add these 2 lines to create POST request
		curl_setopt($ch, CURLOPT_POST, count($data)); //number of parameters sent
		curl_setopt($ch, CURLOPT_POSTFIELDS, $params); //parameters data

		$result = curl_exec($ch);
		curl_close($ch);

		echo $result;
	}
?>