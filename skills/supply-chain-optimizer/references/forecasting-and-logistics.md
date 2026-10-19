# Forecasting and Logistics Optimization

## Demand Forecasting Methods

| Method              | Best For                   | Horizon      | Data Required         |
| ------------------- | -------------------------- | ------------ | --------------------- |
| Moving Average      | Stable demand              | Short-term   | 3-12 periods history  |
| Exponential Smooth  | Trend detection            | Short-term   | Recent weighted data  |
| Holt-Winters        | Seasonal patterns          | Medium-term  | 2+ years seasonal     |
| Linear Regression   | Trend with causal factors  | Medium-term  | Demand + drivers      |
| ARIMA               | Complex time series        | Short-medium | 50+ data points       |
| Machine Learning    | Multi-variable patterns    | Any          | Large datasets        |
| Delphi / Expert     | New products, disruptions  | Long-term    | Expert panel          |

### Forecast Accuracy Metrics

```
MAD (Mean Absolute Deviation):
MAD = (1/n) x SUM(|Actual - Forecast|)

MAPE (Mean Absolute Percentage Error):
MAPE = (1/n) x SUM(|Actual - Forecast| / Actual) x 100

BIAS (Tracking Signal):
Bias = SUM(Actual - Forecast) / MAD
Target: Between -4 and +4

ACCURACY BENCHMARKS:
| Forecast Horizon | Good MAPE | Acceptable MAPE |
| ---------------- | --------- | --------------- |
| 1 month          | < 15%     | < 25%           |
| 3 months         | < 25%     | < 35%           |
| 6 months         | < 30%     | < 45%           |
| 12 months        | < 35%     | < 50%           |
```

## Logistics Optimization

### Transportation Mode Selection

| Mode     | Cost/Unit | Speed     | Capacity  | Best For                      |
| -------- | --------- | --------- | --------- | ----------------------------- |
| Truck    | Medium    | Fast      | Medium    | Regional, door-to-door        |
| Rail     | Low       | Slow      | Very High | Bulk, long-distance domestic  |
| Ocean    | Very Low  | Very Slow | Very High | International, bulk cargo     |
| Air      | Very High | Very Fast | Low       | High-value, urgent, perishable|
| Intermodal | Low-Med | Medium    | High      | Long-distance, cost-effective |

### Warehouse Layout Optimization

```
SLOTTING STRATEGY:
Fast movers (A items) â†’ Near shipping dock, prime pick locations
Medium movers (B items) â†’ Middle zones
Slow movers (C items) â†’ High racks, far locations

LAYOUT PRINCIPLES:
1. Minimize travel distance for highest-velocity items
2. Group items frequently ordered together
3. Separate receiving and shipping areas
4. Reserve staging areas for cross-docking
5. Maintain clear aisle widths for equipment
```
