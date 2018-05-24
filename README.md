# DjangoLottery

## Environment

- docker
- docker-compose

## Deployment

```bash
docker-compose up
```

## Email Configure

```bash
EMAIL_TO = ['test@test.com']
```

## Quick Start

```bash
docker-compose run djangolottery_web python manage.py shell
```

Get lucky numbers of DaLeTou and send them to your email. 

```bash
>>> from dlt.predictor import create
>>> create()
```

Get the winning number of DaLeTou and compare with earlier lucky numbers, then send them to your email. 

```bash
>>> from spider.tasks import dlt_spider
>>> dlt_spider.delay()
```

Actually, the spider of DaLeTou will be executed at 12:00 of Sunday, Tuesday and Thursday.

## Todo

- web ui

## License

[MIT](https://github.com/vuejs/vuepress/blob/master/LICENSE)