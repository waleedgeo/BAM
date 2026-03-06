# -*- coding: utf-8 -*-
"""
Selected Wildfire Events for BAM Framework.
Contains 15 global events categorized by Development/Validation role.
"""

# Global Dictionary of Selected Events
# Structure: event_id: {fid, name, path, row, start_date, end_date, biome, category, challenge}

SELECTED_EVENTS = {
    # =========================================================================
    # VALIDATION TILES (5 events)
    # =========================================================================
    10: {
        'fid': 1, 'name': '2021_CA_Dixie',
        'path': 44, 'row': 32,
        'start_date': '2021-06-25', 'end_date': '2021-09-29',
        'biome': 'Temperate Conifer',
        'category': 'Validation',
        'challenge': 'Mega-fire Scale'
    },
    2: {
        'fid': 2, 'name': '2016_Chile_Central',
        'path': 1, 'row': 85,
        'start_date': '2016-12-23', 'end_date': '2017-03-13',
        'biome': 'Mediterranean Sclerophyll',
        'category': 'Validation',
        'challenge': 'Rapid Spread'
    },
    28: {
        'fid': 3, 'name': '2023_Aus_WilliWilli',
        'path': 89, 'row': 81,
        'start_date': '2023-07-28', 'end_date': '2023-10-16',
        'biome': 'Temperate Broadleaf',
        'category': 'Validation',
        'challenge': 'Eucalypt Signature'
    },
    13: {
        'fid': 4, 'name': '2022_Canada_QC',
        'path': 18, 'row': 25,
        'start_date': '2022-08-09', 'end_date': '2023-09-29',
        'biome': 'Boreal Forest',
        'category': 'Validation',
        'challenge': 'Peatland/Carbon'
    },
    50: {
        'fid': 5, 'name': '2024_CA_ParkFire',
        'path': 44, 'row': 32,
        'start_date': '2024-07-11', 'end_date': '2024-08-28',
        'biome': 'Chaparral/Oak',
        'category': 'Validation',
        'challenge': 'WUI/Recent'
    },

    # =========================================================================
    # DEVELOPMENT TILES (10 events)
    # =========================================================================
    41: {
        'fid': 6, 'name': '2024_Pak_Margala',
        'path': 150, 'row': 37,
        'start_date': '2024-05-23', 'end_date': '2024-06-16',
        'biome': 'Subtropical Broadleaf',
        'category': 'Development',
        'challenge': 'Steep Topography'
    },
    33: {
        'fid': 7, 'name': '2024_India_Nepal',
        'path': 142, 'row': 41,
        'start_date': '2024-02-25', 'end_date': '2024-04-29',
        'biome': 'Subtropical Pine',
        'category': 'Development',
        'challenge': 'Haze & Smoke'
    },
    46: {
        'fid': 8, 'name': '2024_Siberia',
        'path': 122, 'row': 12,
        'start_date': '2024-06-12', 'end_date': '2024-06-28',
        'biome': 'Boreal Larch',
        'category': 'Development',
        'challenge': 'Cloud & Latitude'
    },
    31: {
        'fid': 9, 'name': '2024_Thailand_CM',
        'path': 131, 'row': 47,
        'start_date': '2024-01-19', 'end_date': '2024-02-20',
        'biome': 'Tropical Deciduous',
        'category': 'Development',
        'challenge': 'Ag-Forest Mix'
    },
    35: {
        'fid': 10, 'name': '2024_SA_TableMtn',
        'path': 175, 'row': 83,
        'start_date': '2024-04-12', 'end_date': '2024-05-14',
        'biome': 'Fynbos Shrubland',
        'category': 'Development',
        'challenge': 'Complex Terrain'
    },
    3: {
        'fid': 11, 'name': '2017_Mongolia',
        'path': 126, 'row': 28,
        'start_date': '2017-06-13', 'end_date': '2017-06-29',
        'biome': 'Temperate Steppe',
        'category': 'Development',
        'challenge': 'Low Biomass'
    },
    25: {
        'fid': 12, 'name': '2023_Italy_Sicily',
        'path': 189, 'row': 34,
        'start_date': '2023-07-17', 'end_date': '2023-08-02',
        'biome': 'Mediterranean Scrub',
        'category': 'Development',
        'challenge': 'Dry Summer'
    },
    36: {
        'fid': 13, 'name': '2024_Spain_Cadiz',
        'path': 201, 'row': 35,
        'start_date': '2024-05-04', 'end_date': '2024-06-05',
        'biome': 'Mediterranean Forest',
        'category': 'Development',
        'challenge': 'Coastal Influence'
    },
    8: {
        'fid': 14, 'name': '2020_CO_Cameron',
        'path': 34, 'row': 32,
        'start_date': '2020-07-02', 'end_date': '2020-10-06',
        'biome': 'Subalpine Conifer',
        'category': 'Development',
        'challenge': 'High Altitude'
    },
    43: {
        'fid': 15, 'name': '2024_Greece',
        'path': 181, 'row': 33,
        'start_date': '2024-06-25', 'end_date': '2024-06-30',
        'biome': 'Mediterranean Pine',
        'category': 'Development',
        'challenge': 'Fragmented Landscape'
    }
}

def get_event(event_id):
    """Returns the dictionary for a specific event ID."""
    return SELECTED_EVENTS.get(event_id, None)

def get_all_ids():
    """Returns a list of all selected event IDs."""
    return list(SELECTED_EVENTS.keys())

def get_ids_by_category(category):
    """Returns list of IDs belonging to a specific category (Development/Validation)."""
    return [k for k, v in SELECTED_EVENTS.items() if v['category'] == category]

if __name__ == "__main__":
    print(f"Loaded {len(SELECTED_EVENTS)} events.")
    val = get_ids_by_category('Validation')
    dev = get_ids_by_category('Development')
    print(f"Validation: {len(val)} | Development: {len(dev)}")