button_schema={
    "type": "object",
    "properties":{
        "url":  {"type": "string"},
        "id": {"type": "string"},
        "label":  {"type": "string"},
        "css_class": {"type": "string"}
    },
    "required": ["id", "label", "url", "css_class"],
    "additionalProperties": False
}