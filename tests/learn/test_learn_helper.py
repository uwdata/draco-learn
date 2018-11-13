import os
import sys

from draco import vl2asp
from malfoy.learn.helper import count_violations, current_weights

def test_current_weights():
    assert "encoding_weight" in current_weights()


def test_count_violations():
    query_json = {
        "mark": "bar",
        "data": {"url": "data/cars.csv"},
        "encoding": {
            "x": {"field": "origin", "type": "ordinal"},
            "y": {"field": "horsepower", "type": "quantitative", "aggregate": "mean"},
        },
    }

    draco_query = vl2asp(query_json)  # add: os.path.dirname(os.path.abspath(__file__))

    print(draco_query)

    violations = count_violations(draco_query)

    print(violations)

    assert "encoding" in violations.keys()
    assert violations.get("encoding") == 2
