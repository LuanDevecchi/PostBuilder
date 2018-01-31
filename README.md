# Post Builder

Tool that generates scripts for POST attacks

### Prerequisites

Python 3+

```
Requests Module
```
### Examples

For account-checking

This is the list.txt
```
username1:pass1
admin:admin
admin:adminpass123
username2:pass2
```
This is the PHP Script

```php
<?php

$usr = $_POST['username'];
$pss = $_POST['password'];

if($usr=="admin" and $pss=="adminpass123"){
    echo 'welcome';
}else{
    echo 'wrong username or password';
}

?>
```

![Alt Text](https://im4.ezgif.com/tmp/ezgif-4-d666552633.gif)



## Authors

* **Luan Devecchi** - *Initial work* - [LuanDevecchi](https://github.com/LuanDevecchi)


## TODOs

* More Options
