import sys, os
sys.path.insert(0, os.path.abspath('../../'))

from draco.spec import Data, Task, Query
from dracolearn.learn.helper import current_weights, count_violations

def test_current_weights():
    assert 'encoding_weight' in current_weights()

def test_count_violations():
    data_path = os.path.join(os.path.dirname(__file__), '../../../data/cars.csv')
    data = Data.from_csv(data_path)
    query_json = {
        'mark': 'bar',
        'data': {
            'url': 'data/cars.csv'
        },
        'encoding': {
            'x': {
                'field': 'origin',
                'type': 'ordinal'
            },
            'y': {
                'field': 'horsepower',
                'type': 'quantitative',
                'aggregate': 'mean'
            }
        }
    }
    violations = count_violations(Task(data, Query.from_vegalite(query_json)))

    assert 'encoding' in violations.keys()
    assert violations.get('encoding') == 2
