# Data512, Assignment 2
The purpose of this project was to asses bias of english wikipedia articles on politicians across the globe. This readme contains information on the APIs used to collect and process data, as well as some discoveries and further thoughts on the subject.

#Data

ORES (Objective Revision Evaluation Service) API:
Links:
https://ores.wikimedia.org/v3/
https://ores.wikimedia.org/

License: CC-BY-SA 3.0 and GFDL licenses (https://creativecommons.org/licenses/by-sa/3.0/, https://www.gnu.org/licenses/fdl-1.3.html)

Terms of use: https://foundation.wikimedia.org/wiki/Terms_of_Use/en

## Files
| file name | type | description |
|-----------|------|-------------|
| allqualities.pk| pickle | due to duration of ores request, we ask for the qualities of our articles once and save them. |
| allrevs.pk | pickle | packaging the rev_ids of our articles with the allqulaities.pk so that they can be easily joined |
| Assignment 2.txt | text | Description of the assignment that inspired this project |
| hcds-a2-bias.ipynb | jupyter notebook | jupyter notebook holding all code and documentation needed to reproduce analysis |
| license.md | markdown | describes the permissions of others (such as you) to use this intellectual property |
| wp_pages-no_match.csv | comma seperate value (csv) file | Some ORES calls return 'error' or otherwise failed, this holds those articles |
| data/page_data.csv | csv file | contains revision id, page name, and country affiliated with the political figure in the page in question |
| data/WPDS_2018_data.csv | csv file | contains countries and their popluation in millions |
| wp_wpds_countries-no_match.csv | csv file | Some countries didnt have population data, or some countries didnt show up in our wikipedia pages, these are those files |
| wp_wpds_politicians_by_country.csv | csv file |  holds page, country, rev_id, region, population, and article quality together |
| scoresAndPop.csv | csv file | involves groupby on the wp_wpds_politicians_by_country.csv file and used for country granularity analysis |
| regionAnalysis.csv | csv file | involves groupby on the wp_wpds_politicians_by_country.csv file and used for region granularity analysis |

## primary csv
wp_wpds_politicians_by_country.csv schema
| Column | type | description |
|--------|------|-------------|
| index(country)  | string  | the country name is the index for this csv          |
|   page     |    string  |     the title of the political article in question        |
|     rev_id   |   int  |      revision id that uniquely identifies the wikipedia articles most recent submission       |
| article_quality | string | quality of this page determined by ORES |
| population | float | the population of the country associated with the politician of the page in million |
| region | string | the region associated with this country |

# Discussion
- What biases did you expect to find in the data (before you started working with it), and why?
I expected that since these are all english wikipedia articles, we would find better high quality articles for westernized and english speaking countries. I expect this as these countries hold "english" values, or at least the native english toung making it easier for articles on them to be published on the english site. For example, a native local to the country can create an in depth article on a politician better than an outsider.
- What (potential) sources of bias did you discover in the course of your data processing and analysis?
This is highlighted in the observations in the jupyter notebook, but I mainly believe there are biases to countries in this data to those who are
    1. predominantly english speakers
    2. high in literacy rates
    3. possessing increasingly equitable internet resources
    4. first world countries
    
Of course, this still needs to be investigate more rigorously, but for now this is what my intuition believes to be the bias in the data present
- How might a researcher supplement or transform this dataset to potentially correct for the limitations/biases you observed?
This depends plenty on the context the data is being used in. If the researcher were to use these scores to say, provide funding to countries who are either doing exceedingly well or poor (some kind of fellowship to encourage open political information to the world), they would need to be careful of these biases. Particularly if some machine learning algorithm were used to be an automated decision maker in this setting. To correct for these things, I would suggest some weighting of literacy rates, percentage of english speakers, gdp / wealth distribution. I could imagine some equation that weights these things such that we remove the "trend" and you are left with actual signals of improving article coverage within a country or region. I imagine it almost as "de trending" this bias removal process.
