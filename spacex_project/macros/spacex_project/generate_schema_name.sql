{% macro generate_schema_name(custom_schema_name, node) %}
    {% set env = target.name | lower %}
    {% set base_schema = target.schema %}
    
    {% if custom_schema_name is none %}
        {{ base_schema }}_{{ env }}
    {% else %}
        {{ base_schema }}_{{ env }}_{{ custom_schema_name | trim }}
    {% endif %}
{% endmacro %}