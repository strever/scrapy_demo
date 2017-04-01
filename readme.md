# 爬虫

## 概述

爬取一些常规网站

### 已实现功能

- 随机User-Agent请求头
- 随机代理
- 多来源爬取最新免费代理，数据redis落地
- 代理清洗
- 爬虫日志`/data/logs`下
- 数据mysql落地

### todo

- 突破cookie令牌请求机制
- 突破scrapy无法读取\<script\>反爬机制
- 添加代理ip表建立优选机制


### contact

- [@strever](https://weibo.com/strever)
- <strever@qq.com>

:smile:


## 部署（Deploy）

### requirement

- Python 3.6.0 or above
- scrapy 1.3.3 or above

### 安装scrapy

```shell

$ pip install scrapy
$ pip install pymysql

```

### 拉取项目代码
```git

$ git clone git@github.com:strever/scrapy_demo.git

```

### 配置

在根目录新建文件`.env`添加mysql，redis配置信息

```

$ mv .env.example .env

```



## 爬虫

### 爬虫当前设置

- 请求同时并发数：32
- 请求间隔：0.5秒
- 下载超时：30秒
- 重试2次
- user-agents池在/data/useragents.txt
- 重定向follow3次


### 爬虫命令

```shell

//抓取最新代理,每天早上8点执行一次
$ scrapy crawl pull_proxy

//清理无用代理,每天早上8点5分执行一次
$ scrapy crawl clean_proxy

//根据分类全站抓取
$ scrapy crawl category -s JOBDIR=data/crawls/category-1

//根据单个分类抓取
$ scrapy crawl artist -a artist_id=1


//抓取武汉市国有建设用地网上交易系统
$ scrapy crawl category -a start=1 -a end=3


```

### tor

如果部署在国外节点即可开启tor代理，稳定性高于免费代理或付费代理

- [tor](https://www.torproject.org/download/download.html.en)
- [tor-gui](https://people.torproject.org/~erinn/vidalia-standalone-bundles/)
- [polipo(http->sock5)](http://www.pps.univ-paris-diderot.fr/~jch/software/files/polipo/)

### 数据落地



#### 代理

```sql

CREATE TABLE `proxies` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `protocol` varchar(8) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'http' COMMENT '协议',
  `ip` varchar(64) COLLATE utf8_unicode_ci NOT NULL COMMENT 'ip',
  `port` smallint(5) NOT NULL DEFAULT '80' COMMENT '端口',
  `type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '匿名度',
  `region` varchar(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT '中国' COMMENT '区域',
  `speed` double(6,4) NOT NULL DEFAULT '0.0000' COMMENT '速度',
  `req_num` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '请求次数',
  `success_num` int(11) unsigned NOT NULL COMMENT '成功次数',
  `last_succeed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次成功时间',
  `last_failed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次失败时间',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

```

#### 代理池

redis-key： 'scrapy:proxy_ips'

```shell

host:port> zrange 'scrapy:proxy_ips' 0 -1 WITHSCORES

```


### licence

MIT

