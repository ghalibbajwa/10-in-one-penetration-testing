
from multiprocessing.pool import ThreadPool
from apps.home.libs.CMSScan.plugins.scanners import (
    wpscan,
    droopescan,
    joomscan,
    vbscan
)


def scan_wp(url):
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(wpscan, (url,))
    result = async_result.get()
    return result

def scan_drupal(url):
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(droopescan, (url,))
    result = async_result.get()
    return result

def scan_joomla(url):
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(joomscan, (url,))
    result = async_result.get()
    return result

def scan_vbulletin(url):
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(vbscan, (url,))
    result = async_result.get()
    return result

def scan(id,cms,url):
    data=""
    if cms == "wordpress":
        data = scan_wp(url)
    elif cms == "drupal":
        data = scan_drupal(url)
    elif cms == "joomla":
        data = scan_joomla(url)
    elif cms == "vbulletin":
        data = scan_vbulletin(url)

    return data
