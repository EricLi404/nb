	
#### protoc

```
wget https://github.com/protocolbuffers/protobuf/releases/download/v3.10.1/protoc-3.10.1-linux-x86_64.zip

unzip protoc-3.10.1-linux-x86_64.zip

sudo cp bin/protoc /usr/local/bin

sudo cp -r include/google/ /usr/local/include
```

#### python grpc 相关依赖

```
conda install protobuf -y
conda install grpcio -y
conda install grpcio-tools -y
```


#### linux 安装zip

```
apt-get install zip
yum install -y  zip uzip
```

#### protoc & proto-gen-go

```
go get

protoc-gen-go 工具会出现在 $GOPATH/bin`下，
将这个工具 cp到 /usr/local/bin 下即可

go get -u github.com/golang/protobuf/protoc-gen-go

cp  `go env GOPATH`/bin/protoc-gen-go /usr/local/bin
```

#### zsh-autosuggestions

```

git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

```

#### zsh-syntax-highlighting

```

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

#### astro zsh主题

```
git clone https://github.com/iplaces/astro-zsh-theme.git 

cp astro-zsh-theme/astro.zsh-theme ~/.oh-my-zsh/themes/
```


#### conda 导入导出环境

```
# 导出：
conda activate py36_cv
conda env export > py36_cv.yaml

# 导入：
conda env create -f py36_cv.yaml

```

#### pip 导入导出环境

```
# 生成requirements.txt文件
pip freeze > requirements.txt

安# 装requirements.txt依赖
pip install -r requirements.txt

```

#### 僵尸进程

```
# 查找
ps -A -ostat,ppid,pid,cmd | grep -e '^[Zz]'

ps -ef | grep defunct | more

ps aux | grep Z

```

#### 查找一个文件中不在另一个文件中的行

```
# 显示2.l中不在1.l中的行
grep -v -f 1.l 2.l
```

#### git


| zsh alias | cmd | man | e.g. | 
| --- | --- | --- | --- |
| gb | git branch | 查看分支 |  |
| gbr | git branch --remote | 查看远程分支 |  |
| gsta | git stash push | push到暂存区 |  |
| gstp | git stash pop | 从暂存区pop |  |  |
| gm | git merge | 合并分支 |  |
| gp | git push | push | 把本地的test分支push到远程的master：git push origin test:master |
| gfo | git fetch origin |  |  |
| gf | git fetch |  |  |


#### awk

```
判断一列的数字大小

awk '{if ($3 > 0 && $3 <= 10) print $3}' i.txt

```