<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="post" action="registration.php" enctype="multipart/form-data"  style="text-align: center;">
		<p><b>Registration</b></p>
		<p>Firstname : <input type="text" name="firstname"></p>
		<p>Lastname : <input type="text" name="lastname"></p>
		<p>Username : <input type="text" name="username"></p>
		<p>Email : <input type="text" name="email"></p>
		<p>Password : <input type="password" name="password"></p>
		<input type="submit" name="submit" value="Sign Up">
	</form>
	<a href="get.php">
		<button class = "submit" style = "background-color:green;color:white;border-radius:5px;">
			Get Users
		</button>
	</a>
	<form method="post" action="login.php" enctype="multipart/form-data"  style="text-align: center;">
		<p><b>Sign In</b></p>
		<p>Username : <input type="text" name="username"></p>
		<p>Password : <input type="password" name="password"></p>
		<input type="submit" name="submit" value="Sign In">
	</form>
	<form method="post" action="file.php" enctype="multipart/form-data"  style="text-align: center;">
		<p><b>File</b></p>
		<p style="text-align: center;"><label>File : <br>
			<input type="file" id="file" name="file" /><br>
		</label></p>
		<input type="submit" name="submit" value="Save">
	</form>
</body>
</html>