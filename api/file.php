<?php
	if ( isset($_POST['submit'])){

		//3.1.1 Assigning posted values to variables.
		//$file 		= $_POST['file'];

		$myObj->name = "John";
		$myObj->age = 30;
		$myObj->city = "New York";

		$myJSON = json_encode($myObj);

		echo $myJSON;
	}
?>