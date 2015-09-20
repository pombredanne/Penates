# -*- coding: utf-8 -*-
from syslog import LOG_KERN, LOG_USER, LOG_MAIL, LOG_DAEMON, LOG_AUTH, LOG_LPR, LOG_NEWS, LOG_UUCP, LOG_CRON, LOG_SYSLOG, LOG_LOCAL0, LOG_LOCAL1, LOG_LOCAL2, LOG_LOCAL3, LOG_LOCAL4, LOG_LOCAL5, \
    LOG_LOCAL6, LOG_LOCAL7, \
    openlog, syslog, LOG_DEBUG, LOG_INFO, LOG_NOTICE, LOG_WARNING, LOG_ERR, LOG_CRIT, LOG_ALERT, LOG_EMERG
import time

__author__ = 'Matthieu Gallet'


def main():
    for facility in (LOG_KERN, "LOG_KERN"), (LOG_USER, "LOG_USER"), (LOG_MAIL, "LOG_MAIL"), (LOG_DAEMON, "LOG_DAEMON"), (LOG_AUTH, "LOG_AUTH"), (LOG_LPR, "LOG_LPR"), (LOG_NEWS, "LOG_NEWS"), (LOG_UUCP, "LOG_UUCP"), (LOG_CRON, "LOG_CRON"), (LOG_SYSLOG, "LOG_SYSLOG"), (LOG_LOCAL0, "LOG_LOCAL0"), (LOG_LOCAL1, "LOG_LOCAL1"), (LOG_LOCAL2, "LOG_LOCAL2"), (LOG_LOCAL3, "LOG_LOCAL3"), (LOG_LOCAL4, "LOG_LOCAL4"), (LOG_LOCAL5, "LOG_LOCAL5"), (LOG_LOCAL6, "LOG_LOCAL6"), (LOG_LOCAL7, "LOG_LOCAL7"):
        for priority in (LOG_ALERT, "LOG_ALERT"), (LOG_CRIT, "LOG_CRIT"), (LOG_ERR, "LOG_ERR"), (LOG_WARNING, "LOG_WARNING"), (LOG_NOTICE, "LOG_NOTICE"), (LOG_INFO, "LOG_INFO"), (LOG_DEBUG, "LOG_DEBUG"):
            openlog(facility=facility[0])
            syslog(priority[0], 'Message %s %s' % (priority[1], facility[1]))
        time.sleep(1)


if __name__ == '__main__':
    main()
