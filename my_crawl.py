# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings("ignore")

from crawler import write_crawl_results

the_data = write_crawl_results(["fall foliage", "steelhead fishing"], 20)
