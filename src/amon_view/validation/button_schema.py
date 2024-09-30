button_schema={
    "type": "object",
    "properties":{
        "url":  {"type": "string"},
        "id": {"type": "string"},
        "label":  {"type": "string"}
    },
    "required": ["id", "label"],
    "additionalProperties": False
}