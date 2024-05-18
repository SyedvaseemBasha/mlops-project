from feast import Entity, Feature, FeatureView, ValueType, FileSource
from datetime import timedelta

# Define an entity for the feature store
house = Entity(name="house_id", value_type=ValueType.INT64, description="house id")

# Define a source for feature data
feature_source = FileSource(
    path="data/processed/house_features.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)

# Define a feature view
feature_view = FeatureView(
    name="house_features",
    entities=["house_id"],
    ttl=timedelta(days=1),
    features=[
        Feature(name="num_rooms", dtype=ValueType.INT64),
        Feature(name="area", dtype=ValueType.FLOAT),
        # Add more features as needed
    ],
    online=True,
    input=feature_source,
    tags={"team": "mlops"},
)
