from dash.testing.application_runners import import_app

def test_001_header_exists(dash_duo):
    # start the app 
    app = import_app("app")
    dash_duo.start_server(app)

    # Test for Header presence
    # we look for the H1 presence 

    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text == "Pink Morsel Sales Dashboard"

def test_002_visualization_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    
    # Test for the Graph presence
    # We look for the ID we gave our dcc.Graph: 'sales-line-chart'
    graph = dash_duo.find_element("#sales-line-chart")
    
    assert graph is not None

def test_003_region_picker_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    
    # Test for the Region Picker 
    # We look for the ID we gave our dcc.RadioItems: 'region-filter'
    region_picker = dash_duo.find_element("#region-filter")
    
    assert region_picker is not None