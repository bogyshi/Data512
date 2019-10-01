# Data512, Assignment 1
The purpose of this project was to practice the best practices for open scientific research in the data science setting.
This means that the jupyer notebook, along with the README and license should allow for full reproducibility for others who
stumble along this repository and want to mimic the results and analyses I achieved, while also being able to understand
what assumptions were made and done to any data or results.

In particular, we practice this by publishing a brief analyses on web and mobile traffic on the english wikipedia site over an 11 year period

# Data API

Wikimedia REST API:
Links:
- https://wikitech.wikimedia.org/wiki/Analytics/AQS/Legacy_Pagecounts (does *NOT* discount page spiders/crawlers)
- https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews

License: CC-BY-SA 3.0 and GFDL licenses (https://creativecommons.org/licenses/by-sa/3.0/, https://www.gnu.org/licenses/fdl-1.3.html)

Terms of use: https://www.mediawiki.org/wiki/REST_API#Terms_and_conditions

# Final data
Below is the aggregated data that generated the visual included in this directory
Final csv (en-wikipedia_traffic_200712-201908)
- year : the year data was collected (int)
- month : the month data was collected (int)
- pagecount_all_views: the total views from the legacy pagecount api over desktop and mobile (does *NOT* discount page spiders/crawlers) (real)
- pagecount_desktop_views: the total views from the legacy pagecount api over desktop (does *NOT* discount page spiders/crawlers) (real)
- pagecount_mobile_views: the total views from the legacy pagecount api over mobile (does *NOT* discount page spiders/crawlers) (real)
- pageview_desktop_views: the total views from the pageview api over desktop (discounts page spiders/crawlers) (real)
- pageview_mobile_views:  the total views from the pageview api over mobile (discounts page spiders/crawlers) (real)
- pageview_all_views:  the total views from the pageview api over desktop and mobile (discounts page spiders/crawlers) (real)

# Files
- en-wikipedia_traffic_200712-201908.csv , the csv with aggregated / cleaned api data
- hcds-a1-data-curation.ipynb notebook with all code for api calls, data collection, cleaning, saving, and visualization
- pagecounts_desktop-site_200712-201607.json raw API data for desktop views on legacy tracker
- pagecounts_mobile-site_200712-201607.json raw API data for mobile views on legacy tracker
- pageviews_desktop_201507-201908.json raw API data for desktop views on modern tracker
- pageviews_mobile_app_201507-201908.json raw API data for mobile app views on modern tracker
- pageviews_mobile_web_201507-201908.json raw API data for mobile web views on modern tracker
- EN_WIKI_VIEWS.png the graphic highlighted at the end of the notebook showing traffic on the english wikipedia site
