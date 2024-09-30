input_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "placeholder": {"type": "string"},
        "css_class": {"type": "string"},
        "label": {"type": "string"},
        "type": {"type": "string", "enum": ["text", "number", "float"]},
    },
    "required": ["id", "placeholder", "css_class", "label", "type"],
    "additionalProperties": False,
}
