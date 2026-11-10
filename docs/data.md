# Data

The build checks out `gardusi-gustavo/database-stocks` and reads
`data/stocks/YYYY-MM-DD.json`. It copies the selected dataset into
`dist/data/stocks.json` and renders `dist/index.html`.

There is no runtime CORS call. A database merge dispatches
`database-updated`; the Pages workflow rebuilds.
