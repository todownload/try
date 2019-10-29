Git and VC
=============
*This is s simple project for me to learn something*
---------------------
_____________________

## Some thing about Git
### Something about git repository
##### clone the project to your local directory
```Git
git clone url
```
##### pull from server and renew your local content
```Git
git pull 
```
##### make a local directory as a repository
```Git
git init
```
### Something about commit the change
##### ready to commit
```Git
git add filename 
git add . //add all file
```
##### commit 
```Git
git commit -m "msg"
```
##### push to server
```Git
git push
```
### Something about branch
##### create a new branch
```Git
git branch branch_name
```
##### show all branch
```Git
git branch
```
##### merge another branch
```Git 
git merge branch_name
```
##### delete the branch
```Git
git branch -d branch_name //delete the branch which has been merged
git branch -D branch_name //delete the branch forcibly
```
##### use another branch
```Git
git checkout branch_name
```
### Something about Version Control
##### revert the file which has been deleted
```Git
git checkout - -
```
##### replace your file with the latest file at HEAD
```Git
git checkout -- filename
```
##### go back to previous version
```Git
git reset -- hard verion_code 
```
##### go back to future version that has been delete
```Git
git reflog
```
### Other commands
##### show current status
```Git
git statu
```
##### show confilict
```Git
git diff
```
##### show commit log
```Git
git log
```
##### generate ssh key  use in git bash
```Git
ssh-key 
```

Here is a simple text without any mark oh , I can use \<br> to <br> change a anthone line.<br> I can directly input a url www.baidu.com end

    I am single line text? Yes use four span or two tab
    I am another single line text

```
Hello , I am text block  
yes yes
no no no
```

I am trying to light this   `word`  use \`

Here is *italic* _word_ use \* \*  and \_ and \_  
Here is **bold** __word__ use \*\* \*\* and \_\_ \_\_  
Here is ***italic*** ___bold___ use \*\*\*  \*\*\*    \_\_\_  \_\_\_  
Here is ~~delete word~~ use \~\~ \~\~  

Here is a img with format !\[alt\]\[url "title"\]  
![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")  
[![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")](http:/www.baidu.com "百度")    

Here are two text linkers  
[百度一下](http://www.baidu.com "百度一下")  
[index](/html/index.html "my index")  

Bleow is ul  
* i am a li  
* i am mid li  
    * i am son li  
        * i am grandson li  
        * me too  
    * i am another son li  
* i am another li  

Bleow is ol  
1. i am oli
    1. i am son oli
        1. i am grandson oli
        2. i am also grandson oli
    2. i am father of bleow
        * - [x] i am a checkbox
        * - [x] i am ok
        * - [ ] am i ok?
    3. end
2. i am 2  

Bleow is code  
```C++
#include<iostream>
using namespace std;

int main(){

return 0;
}
```
```Python
name = input("Please input your name : ")
if name != "":
    print(name)
```
| 上句 | 下句 |
| :------: | :------: |
| *明月出天山*     | *苍茫云海间* |
| *月下飞天镜*     | *云深结海楼* |
| *我自横刀向天笑* | *去留肝胆两昆仑* |
| *明月几时有*     | *把酒问青天* |
| *落霞与孤鹜齐飞* | *秋水共长天一色* |

```diff
+ 我本楚狂人
+ 凤歌笑孔丘
- 黄金白璧买歌笑
! 一醉累月轻王侯
# 五云天北是神州
```







It's a simple project for me to learn git .  

