import logging

import redis
import backoff

from prometheus_client import Counter


class StreamEmitter:
    def __init__(self, args):
        if args is None:
            raise ValueError("args not initialized. ")

        logging.info("Trying to connect to redis at %s:%d...", args.redis_host, args.redis_port)
        self._client = self.init(host=args.redis_host, port=args.redis_port)

        self._stream_name = args.stream_name
        self._prom_messages_sent = Counter(f'{args.metrics_prefix}_messages_sent_total', 'Description of counter')

    @backoff.on_exception(backoff.expo,
                          redis.exceptions.ConnectionError,
                          max_time=300)
    def init(self, host="localhost", port=6379, db=0):
        client = redis.Redis(host=host, port=port, db=db, charset="utf-8", decode_responses=True)
        client.get("x")
        logging.info("Successfully connected to redis")
        return client

    @backoff.on_exception(backoff.expo,
                          redis.exceptions.ConnectionError,
                          max_time=300)
    def dispatch(self, line, problem):
        incident_dict = {'line': line, 'problem': problem}
        self._client.xadd(self._stream_name, incident_dict)
        self._prom_messages_sent.inc()
