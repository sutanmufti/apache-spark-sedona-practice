This location is shared to the docker containers.

`sedona-master` and `sedona-worker` must be able to read the files inside this folder.

Let's use Riyadh's data

```bash
curl -o ./riyadh_places.parquet https://data.source.coop/tabaqat/riyadh-places/riyadh_places.parquet
```