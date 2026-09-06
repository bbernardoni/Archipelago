import json
import logging

from ..connections import all_connections, connection_name_to_id
from ..locations import location_name_to_id, location_table

# run as "python -m worlds.toem.scripts.export_rules"
location_dict = {}
for location_name, location_data in location_table.items():
    location_id = location_name_to_id[location_name]
    dict_rule = location_data.rule.to_dict() if location_data.rule is not None else {}
    location_dict[location_name] = {
        "name": location_name,
        "id": location_id,
        "group": location_data.group,
        "region": location_data.region,
        "rule": dict_rule,
    }

connection_dict = {}
for connection_name, connection_data in all_connections.items():
    connection_id = connection_name_to_id.get(connection_name, 0)
    dict_rule = connection_data.rule.to_dict() if connection_data.rule is not None else {}
    connection_dict[connection_name] = {
        "name": connection_name,
        "id": connection_id,
        "group": connection_data.group,
        "src_region_name": connection_data.src_region_name,
        "dst_region_name": connection_data.dst_region_name,
        "rule": dict_rule,
    }

with open("worlds/toem/scripts/locations.json", "w") as f:
    json.dump(location_dict, f, indent=4)
with open("worlds/toem/scripts/connections.json", "w") as f:
    json.dump(connection_dict, f, indent=4)

logger = logging.getLogger("Toem")
logger.setLevel(logging.INFO)
logger.info("Rules exported")
