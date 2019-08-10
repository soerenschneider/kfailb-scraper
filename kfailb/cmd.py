#!/usr/bin/env python3

import random
import time
import logging
import configargparse

from kfailb import InfoPageParser, ClosingHours, StreamEmitter, Scraper
from kfailb import resource_reader


class KFailB:
    """
    Downloads website data, parses it and emits transformed data.
    """
    def __init__(self, args, closing_hours_impl=None):
        if args is None:
            raise ValueError("No args to parse")

        if args.urls:
            urls = args.urls
        else:
            urls = resource_reader.parse_urls()

        logging.info("Using urls: %s", str(urls))

        user_agents = resource_reader.read_user_agents()

        self._scraper = Scraper(urls=urls, user_agents=user_agents)
        self._parser = InfoPageParser()
        self._cache = StreamEmitter(args)

        if closing_hours_impl is None:
            closing_hours_impl = ClosingHours()
        self._closing_hours = closing_hours_impl

    @staticmethod
    def sleep_random():
        """
        Staying stealthy. Sleep for a random time in a given interval to
        not fire a request each x seconds.
        :return:
        """
        sleeping_time = random.randint(55, 120)
        logging.debug("Sleeping for %ss...", sleeping_time)
        time.sleep(sleeping_time)

    def producer(self):
        """
        Performs the program logic until a signal is received.
        :param parser:
        :return:
        """
        user_exit = False
        while not user_exit:
            try:
                if self._closing_hours.is_opened():
                    content = self._scraper.fetch_website()
                    incidents = self._parser.parse_data(content)
                    for incident in incidents:
                        logging.debug("Sending message %d, %s", incident.line, incident.problem)
                        self._cache.dispatch(incident.line, incident.problem)
                else:
                    logging.info("Not performing query during closing hours")

                self.sleep_random()
            except KeyboardInterrupt:
                user_exit = True

def parse_args():
    """
    Parses the arguments given to the program.
    :return: parsed Namespace with the arguments.
    """
    parser = configargparse.ArgumentParser(prog='k-fail-b')
    parser.add_argument('-d', '--debug', action="store_true", env_var="KFAILB_DEBUG",
                        default=False)
    parser.add_argument('--prometheus-port', type=int, dest="prometheus_port",
                        action="store", env_var="KFAILB_PROMPORT", default=8080)
    parser.add_argument('-m', '--metrics-prefix', dest='metrics_prefix', action='store',
                        env_var='KFAILB_METRICS_PREFIX', default='kfailb_scraper')
    parser.add_argument('-p', '--redis-port', type=int, dest="redis_port",
                    action="store", env_var="KFAILB_PORT", default=6379)
    parser.add_argument('-r', '--redis-host', dest="redis_host", action="store",
                        env_var="KFAILB_REDIS", default="localhost")
    parser.add_argument('-s', '--stream-name', dest="stream_name", action="store",
                        env_var="STREAM_NAME", default="kfailb_scrape")
    parser.add_argument('--urls', dest="urls", action="append", env_var="KFAILB_URLS")

    return parser.parse_args()


def setup_logging(args):
    """ Sets up the logging. """
    loglevel = logging.INFO
    if args.debug:
        loglevel = logging.DEBUG

    logging.basicConfig(level=loglevel, format='%(levelname)s\t %(asctime)s %(message)s')
    logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(loglevel)


if __name__ == '__main__':
    args = parse_args()
    setup_logging(args)
    KFailB(args).producer()
