# Premier League Full-Back Analysis 2025/26

A football analytics project analysing the performance of Premier League full-backs using Python and Power BI.

The project was built to explore how players can be compared using per-90 statistics and percentile rankings.

## Dashboard

The Power BI dashboard allows a user to select any qualifying Premier League full-back and compare their performance against the median Premier League full-back.

The dashboard includes:

- Player selection
- Crosses per 90
- Tackles won per 90
- Interceptions per 90
- Percentile rankings for each metric
- Comparison against the Premier League full-back median
- League-wide full-back rankings
- Automatically generated player insights

## Example: Lewis Hall

The analysis shows Lewis Hall as:

- 85th percentile for crosses
- 73rd percentile for interceptions
- 52nd percentile for tackles won

This suggests that Hall stands out particularly for his crossing output, while his tackles won are much closer to the league median.

## Data Pipeline

The project uses Python to clean, combine and transform football data before loading the resulting dataset into Power BI.

The workflow is:

Raw data → Python cleaning and transformation → Player position matching → Per-90 calculations → Percentile calculations → Processed CSV → Power BI

### Python

The Python scripts use pandas for data processing.

`01_clean_misc.py`

- Loads the raw player statistics
- Selects the required metrics
- Cleans the dataset
- Calculates per-90 statistics

`02_load_positions.py`

- Loads player position information
- Identifies left-backs and right-backs
- Matches players between datasets
- Applies a minimum playing-time threshold
- Calculates percentile rankings
- Exports the final dataset used by Power BI

## Metrics

### Crosses per 90

Number of crosses attempted per 90 minutes.

Used as an indicator of a full-back's involvement in delivering the ball from wide areas.

### Tackles Won per 90

Number of tackles won per 90 minutes.

Used as one measure of defensive involvement and effectiveness.

### Interceptions per 90

Number of interceptions made per 90 minutes.

Used as an indicator of defensive positioning and ability to disrupt opposition possession.

### Percentile Rankings

Players are ranked against the other qualifying Premier League full-backs.

For example, a crossing percentile of 85 means the player records a higher crossing rate than approximately 85% of the comparison group.

## Technologies

- Python
- pandas
- Power BI
- DAX
- Git / GitHub

## Project Structure

    NewcastleAnalytics/
    ├── data/
    │   ├── raw/
    │   └── processed/
    ├── powerbi/
    │   └── Premier_League_Fullback_Analysis.pbix
    ├── python/
    │   ├── 01_clean_misc.py
    │   └── 02_load_positions.py
    ├── .gitignore
    └── README.md

## Limitations

This is a deliberately focused analysis built from publicly available football data.

The current model uses three metrics and therefore does not attempt to provide a complete assessment of player quality. Factors such as progressive passing, chance creation, possession-adjusted defending, team tactical style and expected assists would provide additional context.

Per-90 statistics can also be affected by sample size, so a minimum playing-time threshold is applied before players are included.

## Future Development

Possible extensions include:

- Progressive passing and carrying metrics
- Expected assists and chance creation
- Age and market-value analysis
- Similar-player identification
- Recruitment shortlists based on weighted metrics
- Historical season comparisons
- Analysis across other European leagues

## Purpose

This project was created as a practical demonstration of an end-to-end analytics workflow: sourcing data, cleaning and transforming it with Python, designing comparison metrics and presenting the results through an interactive Power BI dashboard.