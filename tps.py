#! /usr/bin/env python3

import sys
import logging
import yaml

from toniepodcastsync import ToniePodcastSync, Podcast


config = yaml.safe_load(open("config.yaml"))
tps = ToniePodcastSync(config['login']['username'], config['login']['password'])
tps.printToniesOverview()

for name, sync in config['sync'].items():
    print(f"Syncing {sync['podcast']} to {sync['id']}")
    podcast = Podcast(config['podcasts'][sync['podcast']])
    podcast.refreshFeed()
    print(podcast.title)
    tps.syncPodcast2Tonie(podcast, sync['id'])
