from statistics import mean

def get_storm_glass_summary(results):
    summary = dict()

    conditions = ["airTemperature", "windSpeed",
                  "gust", "visibility", "waterTemperature"]

    for condition in conditions:
        values = [result[condition] for result in results]
        avg = mean([value["avg"] for value in values])
        minimum = min([value["min"] for value in values])
        maximum = max([value["max"] for value in values])
        dev = mean([value["stdev"] for value in values])
        result = {"avg": round(avg, 2),
                  "min": round(minimum, 2),
                  "max": round(maximum, 2),
                  "stdev": round(dev, 2)}

        summary[condition] = result

    return summary

def get_summary(storm_glass_results):

    storm_glass_summary = get_storm_glass_summary(storm_glass_results)
    return storm_glass_summary
