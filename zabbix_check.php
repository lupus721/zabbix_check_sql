<?php
	if (empty($_GET['ip'])){
		echo "usage : </br> http://a.com/zabbix_check.php?ip=http://1.1.1.1/</br>";
	}
	else {
		$payload = "python zabbix_session.py";
		$add_port = $_GET['ip'];
		$cmd = system("$payload $add_port",$ret);
	}

?>