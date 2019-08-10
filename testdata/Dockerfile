FROM registry.gitlab.com/soerenschneider/mountebank-docker

COPY * /kfailb/

EXPOSE 2525
ENTRYPOINT ["mb"]
CMD ["start", "--pidfile", "/tmp/mb.pid", "--logfile", "/tmp/mb.log", "--configfile", "/kfailb/kfailb.json"]
